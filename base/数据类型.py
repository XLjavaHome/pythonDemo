'''
Python支持5种数据类型
'''
# 1. Numbers（数字）——用于保存数值
a=7.0
# 2 Strings（字符串）——字符串是一个字符序列。我们用单引号或双引号来声明字符串
title="Ayushi's Book"
# 3. Lists（列表）——列表就是一些值的有序集合，我们用方括号声明列表。
array = [3, 4, "212", ["sas", 121], 3]
# 可以有重复元素
print(array)
# 去掉重复元素
set = set(['1', 'A', 1, '1', 2])
print(set)
# 区分大小写
print('1' in set)
print('a' in set)
print('A' in set)
# 4. Tuples（元组）——元组和列表一样，也是一些值的有序集合，区别是元组是不可变的，意味着我们无法改变元组内的值。
name=('Ayushi','Sharma')
name[0]='Avery'
# 5. Dictionary（字典）——字典是一种数据结构，含有键值对。我们用大括号声明字典。
squares={1:1,2:4,3:9,4:16,5:25}
type(squares)
squares={x:x**2 for x in range(1,6)}
squares