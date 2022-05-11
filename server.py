from flask import Flask
server = Flask(__name__)

count = 0
# def get_hit_count():
#     retries = 5

#     while True:
#         try:
#             return db_cache.incr(name='hit_count')
#         except redis.exceptions.ConnectionError as exc:
#             if retries == 0:
#                 return exc
#             retries = retries - 1
#             time.sleep(.5)


@server.route('/')
def hello():
    count = count + 1 
#     get_hit_count()
    return "<h1>Page Hit Count {} times. REFRESH MORE!!!</h1>".format(count)

if __name__ == "__main__":
   server.run(host='0.0.0.0', port=1337)
