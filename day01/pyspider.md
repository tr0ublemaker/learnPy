#pyspider

##问题1
#####tornado 包不匹配导致下列问题
使用`pip install tornado --upgrage`解决

    Traceback (most recent call last):
          File "/usr/lib/python2.7/site-packages/pyspider/fetcher/tornado_fetcher.py", line 127, in async_fetch
            result = yield gen.maybe_future(self.data_fetch(url, task))
        AttributeError: 'module' object has no attribute 'maybe_future'
