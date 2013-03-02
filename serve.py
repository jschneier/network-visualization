import sys
import redis
import os.path
from store import ConsumerProducer
from bottle import route, run, template, static_file

ROOT = os.path.dirname(os.path.abspath(__file__))

redis = redis.StrictRedis()

@route('/')
def index(): 
    return template("index.html")

@route('data')
def data():
    data = redis.lrange('data', 0, -1)
    redis.delete('data')
    return json.dumps(data)

@route('/lib/<filename>')
def serve_lib(filename):
    return static_file(filename, root=ROOT)

@route('/src/<filename>')
def serve_src(filename):
    return static_file(filename, root=ROOT)

if __name__ == '__main__':
    fname = sys.argv[1]
    run(host='localhost', port=8080)
    consumer_producer = ConsumerProducer(fname)
    consumer_producer.start()
