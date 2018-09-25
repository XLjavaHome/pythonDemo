'''
%格式化
'''
s1 = 72
s2 = 85
r = (s2 - s1) / s2 * 100
# %f表示浮点数（小数）
# 而通过%.1f则表示保留1位
'''
%f浮点数
%d整数
%s字符串
二个百分号输出1个百分号
'''
print('小明提高了%.1f %%,%s' % (r, '测试多个占位符'))
print('小明提高了%s%%' % r)

'''
format格式化
'''
#   格式化字典，0代表参数顺序
'My name is {0[username]}, age is {0[age]}!'.format({'username': 'yiifaa', 'age': 32})
# 注意!r的用法，会直接输出字符串格式，携带单引号
'My name is {0[username]!r}, age is {0[age]}!'.format({'username': 'yiifaa', 'age': 32})
# 通过下标
print('My name is {0}, age is {1}!'.format('yiifaa', 32))
#  格式化元组
print('My name is {0}, age is {1}!'.format(*['yiifaa', 32]))
# 通过关键字
print('My name is {username}, age is {age}!'.format(age=32, username='yiifaa'))
