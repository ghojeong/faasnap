import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0,password="password")

import os

resource_dir = "~/faasnap/resources"
for (path, dir, files) in os.walk(resource_dir):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        with open(path+"/"+filename,'rb') as f:
            r.set(filename, f.read())
        print("%s/%s" % (path, filename))

