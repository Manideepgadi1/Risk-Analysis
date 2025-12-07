# Gunicorn configuration for production deployment
# This is a more robust alternative to running main.py directly

import multiprocessing

# Server socket
bind = "127.0.0.1:8001"
backlog = 2048

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "uvicorn.workers.UvicornWorker"
worker_connections = 1000
timeout = 120
keepalive = 5

# Logging
accesslog = "/var/log/risk-analysis/gunicorn-access.log"
errorlog = "/var/log/risk-analysis/gunicorn-error.log"
loglevel = "info"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# Process naming
proc_name = "risk-analysis-api"

# Server mechanics
daemon = False
pidfile = "/var/run/risk-analysis/gunicorn.pid"
umask = 0
user = None
group = None
tmp_upload_dir = None

# Preload app for better performance
preload_app = True
