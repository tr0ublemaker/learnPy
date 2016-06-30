# -*- coding:utf-8 -*-

def log(func):
    def wrapper(*args,**kw):
        print 'call %s :'%func.__name__
        return func(*args,**kw)
    return wrapper

def logg(text = ''):
    def decorator(func = None):
        def warper(*args,**kw):
            print 'begin call'
            print '%s %s():' % (text,func.__name__)
            rst = func(*args,**kw)
            print 'end call'
            return rst
        return warper
    return decorator
import functools

def log2(text = ''):
    def dec(func):
        @functools.wraps(func)
        def warp(*args,**kw):
            print 'begin'

            print 'end'
            return func(*args,**kw)
    return dec

@log2('a')
def ha():
    print 'haha'


@log
def now():
    import time
    print time.time()

if __name__ == '__main__':
    ha()