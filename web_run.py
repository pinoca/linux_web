import os
if __name__ == '__main__':
    os.system("source activate python38")
    os.system("gunicorn linux_web.wsgi -w 2 -k gthread -b 127.0.0.1:8000")