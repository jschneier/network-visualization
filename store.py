import re
import redis
import threading
from tail import tail

class ConsumerProducer(threading.Thread):

    def __init__(self, fname):
        super(ConsumerProducer, self).__init__()
        self.redis = redis.StrictRedis()
        self.fname = fname
        self.regex = re.compile(r'^.* -> (?:\S*)\s*(?P<protocol>\w+)')

    def run(self):
        for line in tail(self.fname):
            match = self.regex.match(line)
            self.redis.lpush('data', match.group('protocol'))
