import re
def isLetters(str):
    '''
    判断是否为字母数字
    :param str:
    :return:
    '''
    r = re.compile(r'^[a-zA-Z0-9]')
    result = r.match(str)
    if result == None:
        return False
    else:
        return True
if __name__ == '__main__':
    print(isLetters('asda'))
    print(isLetters('测试'))
