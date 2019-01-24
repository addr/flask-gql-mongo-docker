"""
Shamelessly stolen from https://gist.github.com/chenjianjx/53d8c2317f6023dc2fa0
A python script which starts celery worker and auto reload it when any code
change happens.
"""

import time
from watchdog.observers import Observer  # pip install watchdog
from watchdog.events import PatternMatchingEventHandler
import psutil  # pip install psutil
import os
import sys
import subprocess

current_dir = os.path.dirname(os.path.realpath(__file__))
# code_dir_to_monitor = os.path.join(
#     current_dir, "scx_backend/transformation_engine/monitor")
code_dir_to_monitor = current_dir
# happen to be the same. It may be different on your machine
celery_working_dir = code_dir_to_monitor
celery_cmdline = \
    'celery worker -A app.monitor.init_monitor ' \
    '-l debug ' \
    '-Q monitor ' \
    '-n monitor@%h' \
    ''.split(" ")


class MyHandler(PatternMatchingEventHandler):
    def on_any_event(self, event):
        print("detected change. event = {}".format(event))

        for proc in psutil.process_iter():
            proc_cmdline = self._get_proc_cmdline(proc)
            if not proc_cmdline or len(proc_cmdline) < len(celery_cmdline):
                # print("No proc_cmdline for {0}".format(proc_cmdline))
                continue

            is_celery_worker = 'python' in proc_cmdline[0].lower() \
                and celery_cmdline[0] in proc_cmdline[1] \
                and celery_cmdline[1] in proc_cmdline[2]

            if not is_celery_worker:
                # print("{0} is not a celery worker".format(
                #     proc_cmdline[0].lower()))
                continue

            proc.kill()
            # print("Just killed {} on working dir {}".format(
            #     proc_cmdline, proc.cwd()))

        run_worker()

    @staticmethod
    def _get_proc_cmdline(proc):
        # noinspection PyBroadException
        try:
            return proc.cmdline()
        except Exception:
            return []


def run_worker():
    print(sys.path)
    print("Ready to call {} ".format(celery_cmdline))
    os.chdir(celery_working_dir)
    subprocess.Popen(celery_cmdline)
    print("Done callling {} ".format(celery_cmdline))


if __name__ == "__main__":

    run_worker()

    event_handler = MyHandler(patterns=["*.py"])
    observer = Observer()
    observer.schedule(event_handler, code_dir_to_monitor, recursive=True)
    observer.start()
    print("file change observer started")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
