chdir = '/root/savnet_back/savnet'
workers = 1
threads = 1
bind = '0.0.0.0:5000'
daemon = 'false'
worker_connections = 2000
pidfile = '/root/savnet_back/log/gunicorn.pid'
loglevel = 'debug' 
