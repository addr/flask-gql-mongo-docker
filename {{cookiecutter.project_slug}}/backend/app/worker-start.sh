#! /usr/bin/env bash
set -e

celery worker -A app.worker.init_worker -l info -Q worker
