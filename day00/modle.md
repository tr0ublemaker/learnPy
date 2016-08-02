#模块modle
书写规范 先import 标准库 ，第三方库 ，自己写的中间空一行
安装方式常用 pip install 和esay_install 

##模块搜索路径
默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中：

    >>> import sys
    >>> sys.path
    ['', '/Library/Python/2.7/site-packages/pycrypto-2.6.1-py2.7-macosx-10.9-intel.egg', '/Library/Python/2.7/site-packages/PIL-1.1.7-py2.7-macosx-10.9-intel.egg', ...]

如果我们要添加自己的搜索目录，有两种方法：

一是直接修改sys.path，添加要搜索的目录：

    >>> import sys
    >>> sys.path.append('/Users/michael/my_py_scripts')

这种方法是在运行时修改，运行结束后失效。

第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。

##\_\_future__
对于新版本中的特性可以使用__future__中的一些功能去测试新版本中的新特性

