# 1到5的范围
index = 5
# 没有1就是从0开始
for i in range(1, index):
    print(i)
    if i == len(range(index)) - 1:
        print("循环结束")
else:
    print('for循环结束')


def release(lst):
    fmp = []
    for item in lst:
        if isinstance(item, list):
            tmp = release(item)
            for item2 in tmp:
                yield item2
        else:
            yield item


# l = [1, 2, 3, 4, 5, [6], [7, 8, [9, [10]]]]
# print(l)
# lst = release(l)
# print(lst)
# print(list(lst))
