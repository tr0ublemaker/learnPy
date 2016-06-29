#-*- coding:utf-8 -*-
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


if __name__ == '__main__':
    # for x in fib(10):
    #     print x
    # def f(a,b):
    #     return a*10 + b
    # a = reduce(f,[x for x in range(10)])

    # def up(s):
    #
    #     s = s[:1].upper()+s[1:].lower()
    #     return s
    # a = ['adam', 'LISA', 'barT']
    # import time
    # st = time.time()
    # for x in xrange(100000):
    #     map(up,a)
    # print time.time()-st
    # pass
    # def pro(list):
    #     def aa(a,b):
    #         return a*b
    #     return reduce(aa,list)
    # l1 = [x for x in range(1,5)]
    # print pro(l1)
    def is_prime(num):
        for i in range(2,num-1):
            if num%i == 0:
                return True
        return False
    re = filter(is_prime,[i for i in range(1,101)])
    print re
