#list
有时候，为了需求，需要统计两个 list 之间的交集，并集，差集。查询了一些资料，现在总结在下面:
1. 获取两个list 的交集

#方法一:
    a=[2,3,4,5]
    b=[2,5,8]
    tmp = [val for val in a if val in b]
    print tmp
    #[2, 5]

#方法二
	print list(set(a).intersection(set(b)))

2.获取两个list 的并集

	print list(set(a).union(set(b)))

3.获取两个 list 的差集

	print list(set(b).difference(set(a))) # b中有而a中没有的
