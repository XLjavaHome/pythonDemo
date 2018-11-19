s = set()
s.add(1)
s.add("hello")
print(len(s))
print(s)
# set集合直接跟string字符串相加是不行的得遍历相加
myString = "字符串"
for i in s:
    # 要将数字转换为字符串
    myString += str(i)
print(myString)
