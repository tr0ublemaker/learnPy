#scrapy

###1.在pycharm下调试scrapy

在scrapy工程目录下新建一个_run.py_内容为

    from scrapy import cmdline

    cmdline.execute('scrapy crawl projectname.split(" "))
    
便可使用pycharm运行调试

###2.Scrapy 中 spider文件下spider.py的命名不能与  bot_name相同否则在 import 别的模块时会出现找不到模块

	Scrapy: ImportError: No module named items
        
    Your spider module is named the same as your scrapy project module, so python is trying to import items relative to byub.py spider.

    You are facing a common regret of python imports, see http://www.python.org/dev/peps/pep-0328


quicks fixes:
*	rename your spider module to byub_org.py or similar.
*	or use from __future__ import absolute_import in byub.py spider.
*	or rename your project to something like byubbot.

###3.UnicodeDecodeError: 'ascii' codec can't decode byte 0xef in position 
环境描述：
  在使用`urllib.unquote（）` 进行反编码时获得的为的str并不是`ascii`所以要使用
  
	string.decode('utf-8')  # or:
	unicode(string, 'utf-8')#将字符串转化为 u'str'
    
###4.urllib.quote(url)和urllib.quote_plus(url)

将url数据获取之后，并将其编码，从而适用与URL字符串中，使其能被打印和被web服务器接受。

    >>> urllib.quote('http://www.baidu.com')
    'http%3A//www.baidu.com'
    >>> urllib.quote_plus('http://www.baidu.com')
    'http%3A%2F%2Fwww.baidu.com'

###5.urllib.unquote(url)和urllib.unquote_plus(url)

与4的函数相反。@[]()