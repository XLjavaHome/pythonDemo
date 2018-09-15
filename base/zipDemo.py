# 两个列表中的数据项进行了配对，并用它们创建了元组。
print(list(zip(['a','b','c'],[1,2,3])))
# [('a', 1), ('b', 2), ('c', 3)]
nums = ['flower','flow','flight']
# num加*和不加结果不一样
for i in zip(*nums):
    print(i)
