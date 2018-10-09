import pinyin
# 汉字中的间隔符delimiter
a = pinyin.get('杨强', format='strip', delimiter="")
print(a)
b = pinyin.get_initial('杨强')
print(b.replace(' ', ''))
