# 生成器
def squares(n):
    i = 1
    for x in range(1,n):
        #
        yield x**2
    # while (i <= n):
    #     yield i ** 2
    #     i += 1


for i in squares(7):
    print(i)
