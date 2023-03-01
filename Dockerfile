FROM python:3.8

# 本地的挂载目录
ADD . /linux_web

# 设置容器启动后的默认运行目录
WORKDIR /linux_web

# 运行命令，安装依赖
# RUN 命令可以有多个，但是可以用 && 连接多个命令来减少层级。
RUN pip install django
RUN pip install redis

# CMD 指令只能一个，是容器启动后执行的命令，算是程序的入口。
CMD python manage.py runserver 0.0.0.0:8000

