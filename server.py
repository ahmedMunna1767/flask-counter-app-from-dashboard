import time
from flask import Flask
import redis

app = Flask(__name__)
db_cache = redis.StrictRedis(host="redis-mogenius-t71j5x", port=6379, db=0, password='123456789')

def get_hit_count():
    retries = 5

    while True:
        try:
            return db_cache.incr(name='hit_count')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                return exc
            retries = retries - 1
            time.sleep(.5)


@app.route('/')
def hello():
    count = get_hit_count()
    return "<div><h1>Hello Adventurer<h1></div><div><h1>This Page is hit  {} times. REFRESH MORE TO SEE MORE !!! &#9786;&#9786;&#9786;</h1></div><div><footer>This is a Simple Test Running Docker, Flask, Redis On The Cloud for free....</footer></div>".format(count)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=1337)
