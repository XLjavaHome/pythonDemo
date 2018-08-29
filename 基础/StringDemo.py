# 将字符串中第一个字母大写capitalize
print('ayushi'.capitalize())
print('@ayushi'.capitalize())

# 何检查字符串中所有的字符都为字母和数字
# True
print('Ayushi123'.isalnum())

print('Ayushi123!'.isalnum())
'123.3'.isdigit()
'123'.isnumeric()
'ayushi'.islower()
'Ayushi'.isupper()
'Ayushi'.istitle()
'   '.isspace()
'123F'.isdecimal()

import re

# 发现字符串中‘ake  ,函数search()会在第一次匹配时停止运行
rhyme = re.search('.ake', 'I would make a cake, but I hate to bake')
print(rhyme.group())
# 'make'
