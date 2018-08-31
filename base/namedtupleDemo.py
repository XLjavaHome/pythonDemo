from collections import namedtuple

# Namedtuple能让我们用名称/标签获取一个元组的元素，这里我们使用函数namedtuple()，将其从collections模块中导入。
result = namedtuple('result', 'Physics Chemistry Maths')  # format
Ayushi = result(Physics=86, Chemistry=95, Maths=86)  # declaring the tuple
print(Ayushi.Chemistry)
# 95
