# 切片是Python中的一种方法，能让我们只检索列表、元素或字符串的一部分。在切片时，我们使用切片操作符[]
demo = (1, 2, 3, 4, 5)[2:4]
# (3, 4)
print(demo)

demo2 = [7, 6, 8, 5, 9][2:]
# [8, 5, 9]
print(demo2)
demo3 = 'Hello'[:-1]
# ‘Hell’
print(demo3)
