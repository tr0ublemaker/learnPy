#day 1 
## 迭代
任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，只要符合迭代条件，就可以使用for循环。
###如何判断一个对象可否迭代

*方法是通过collections模块的Iterable类型判断
'

>>> from collections import Iterable
>>> isinstance('abc', Iterable) # str是否可迭代
True
>>> isinstance([1,2,3], Iterable) # list是否可迭代
True
>>> isinstance(123, Iterable) # 整数是否可迭代
Falss
'


Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
'
>>> for i, value in enumerate(['A', 'B', 'C']):
...     print(i, value)
...
0 A
1 B
2 C
'

##列表生成器
要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：

‘
>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
’

还可以使用两层循环，可以生成全排列：

‘
>>> [m + n for m in 'ABC' for n in 'XYZ']
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
’

for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：

>>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
>>> for k, v in d.items():
...     print(k, '=', v)
...
y = B
x = A
z = C

因此，列表生成式也可以使用两个变量来生成list：

>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
>> [k + '=' + v for k, v in d.items()]
['y=B', 'x=A', 'z=C']


##生成器
这是list

>l = [x for x in range(10)]

这是generator
>p = (x for x in range(10))

generator 有p.next()方法



斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：

>def fib(max):
    >>n, a, b = 0, 0, 1
    while n < max:
        >>>print b
        a, b = b, a + b
        n = n + 1
        
###迭代 yield


