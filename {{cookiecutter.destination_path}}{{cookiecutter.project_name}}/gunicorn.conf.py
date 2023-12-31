# file gunicorn.conf.py
# coding=utf-8

import os
import multiprocessing

_LOGS = '/var/local/{{cookiecutter.project_name}}/logs'
errorlog = os.path.join(_LOGS, '{{cookiecutter.project_name}}_error.log')
accesslog = os.path.join(_LOGS, '{{cookiecutter.project_name}}_access.log')
loglevel = 'info'
bind = '0.0.0.0:{{cookiecutter.port}}'
workers = 2 # multiprocessing.cpu_count() * 2 + 1
timeout = 30  # timeout 30 seconds
keepalive = 60 * 60  # keep connections alive for 1 hour
capture_output = True
