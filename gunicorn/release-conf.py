bind = "unix:/run/gunicorn/socket"
backlog = 5
workers = 2
worker_class = "gevent"
worker_connections = 4
max_requests = 0
no_sendfile = True
pid = "/run/gunicorn/pid"
worker_tmp_dir = "/run/gunicorn"
access_logfile = "/var/log/gunicorn/access.log"
error_logfile = "/var/log/gunicorn/error.log"
log_level = "warning"


