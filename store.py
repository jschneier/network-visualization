import re
import redis
import threading
from tail import tail

class ConsumerProducer(threading.Thread):

    def __init__(self, fname):
        super(ConsumerProducer, self).__init__()
        self.redis = redis.StrictRedis()
        self.fname = fname
        self.regex = re.compile(u'^.* -> (?:ff\.\S*)? \s* (?P<protocol>\w+)')

    def run(self):
        for line in tail(self.fname):
            self.redis.lpush('data', self.regex.search(line).group('protocol'))
