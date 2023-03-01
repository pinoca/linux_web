from django.shortcuts import render
from django.shortcuts import HttpResponse
import redis
import time


# Create your views here.
def index(req):
    r = redis.StrictRedis(host='172.17.0.2', port=6379, db=0)
    r.set("now_time", int(time.time()))
    return render(req, "index.html", {"time": r.get("now_time")})
