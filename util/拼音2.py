from pinyin import pinyin
# 汉字中的间隔符delimiter
a = pinyin.get('杨强', format='strip', delimiter="")
print(a)
# 中间有空格
b = pinyin.get_initial('杨w强')
print(b.replace(' ', ''))
