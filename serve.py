import sys
import redis
from store import ConsumerProducer
from bottle import route, run, template, static_file

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
    return static_file(filename, root='/home/jschneier/hackathon/one-hackathon/lib')

@route('/src/<filename>')
def serve_src(filename):
    return static_file(filename, root='/home/jschneier/hackathon/one-hackathon/src')

if __name__ == '__main__':
    fname = sys.argv[1]
    run(host='localhost', port=8080)
    consumer_producer = ConsumerProducer(fname)
    consumer_producer.start()
