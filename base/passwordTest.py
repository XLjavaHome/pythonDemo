'''生成密码'''

import random
passwords = []
file = open("password.txt", "w")
def initPassWord():
    result = ""
    for x in range(8):
        result += str(random.randint(0, 9));
    return result
for i in range(1000000):
    password = initPassWord()  # 从字母和数字中随机取8位
    if password not in passwords:
        file.write(str(password) + "\n")
        passwords.append(password)
file.close()
