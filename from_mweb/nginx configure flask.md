# nginx configure flask


`ln -s /var/www/flasky/flasky/flasky_nginx.conf /etc/nginx/conf.d`

`uwsgi flasky_uwsgi.ini --plugin python3`

```conf
1 server {
2     listen      80;
3     server_name localhost;
4     charset     utf-8;
5     client_max_body_size 75M;
6
7     location / { try_files $uri @yourapplication; }
8     location @yourapplication {
9         include uwsgi_params;
10     uwsgi_pass 127.0.0.1:9191;
11     }
12 }
```

```ini
[uwsgi]
; 当设定了 max-request 的时候，到达值后 worker 会重启
; http://uwsgi-docs-cn.readthedocs.io/zh_CN/latest/Options.html?highlight=max-requests
; 如果没有 master，重启将不会实现
; http://stackoverflow.com/a/5430522/1542345
master = true
max-requests = 6000
; Simple math like processes = 2 * cpucores will not be enough.
processes = 2
; 如果你想维持 Python 的线程支持同时应用又不启动多个线程，只需要加上 --enable-threads 选项 (或者 enable-threads = true 在 ini 风格配置文件中)。
; http://uwsgi-docs-cn.readthedocs.io/zh_CN/latest/WSGIquickstart.html#python
; enable-threads = true
; http://uwsgi-docs.readthedocs.io/en/latest/ThingsToKnow.html
; 启用了多线程模式后，但自动开启线程支持，因此上面的  enabled-threads 不用设置
threads = 2
; 惊群效应
; http://uwsgi-docs-zh.readthedocs.io/zh_CN/latest/articles/SerializingAccept.html
thunder-lock = true
chmod-socket = 664
; 参见 https://blog.zengrong.net/post/2614.htm
buffer-size = 32768
; 执行的启动文件
wsgi-file = manage.py
; 对应 manage.py 的同名全局变量，是一个 Flask app
callable = app
; 在 ubuntu 下，使用 www-data 权限来执行，其他发行版请自行修改
uid = www-data
gid = www-data
; 虚拟环境的文件夹
#venv = /srv/www/em/venv
; 可以使用魔术变量, %d 代表 uwsgi 工作目录
; venv = %dvenv
; 启动 http 监听，注意不要写成了 socket
;http = 0.0.0.0:5000
; 使用 pidfile，方便用 --stop 或者 --reload
pidfile = %d%n.pid
; 除了 pidfile 也同时使用 Master Fifo 来管理进程
; http://uwsgi-docs-zh.readthedocs.io/zh_CN/latest/MasterFIFO.html
; 如果使用 supervisor 管理进程，是否使用 master-fifo 则可以自行选择，这是对 uwsgi 进行高级管理的好办法
master-fifo = %d%n.fifo

```


