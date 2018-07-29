# 更改集合！
def addlist(alist):
    for i in alist:
        yield i * 2
alist = [1, 2, 3, 4]
for x in addlist(alist):
    print (x)


def h():
    print 'Wen Chuan'
    yield 5
    print 'Fighting!'

c = h()
c.next()