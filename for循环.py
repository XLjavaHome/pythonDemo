# 1到5的范围
index = 5
for i in range(1, index):
    print(i)
    if i == len(range(index)) - 1:
        print("循环结束")
else:
    print('for循环结束')
