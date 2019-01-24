#! /usr/bin/env bash
set -e

celery worker -A app.monitor.init_monitor -l info -Q monitor
