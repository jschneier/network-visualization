#!/usr/bin/env python
import sys
import time
import os.path

def tail(fname):
    try:
        if not os.path.exists(fname): raise IOError
        with open(fname) as file:
            while True:
                where = file.tell()
                line = file.readline()
                if not line:
                    time.sleep(0.5)
                    file.seek(where)
                else:
                    yield line
    except IOError:
        print >>sys.stderr, 'IOError opening: %s' % fname

if __name__ == '__main__':
    for line in tail(sys.argv[1]):
        print line,
