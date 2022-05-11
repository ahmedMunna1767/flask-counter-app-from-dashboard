import time
from flask import Flask
import redis

app = Flask(__name__)
db_cache = redis.StrictRedis(host="redis-mogenius-t71j5x", port=6379, db=0, password='Salmaahmed1767')

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
    return "<h1>Page Hit Count {} times. REFRESH MORE!!!</h1>".format(count)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=1337)
