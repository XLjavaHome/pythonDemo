from enum import Enum, unique
# 首先，定义枚举要导入enum模块。
# 枚举定义用class关键字，继承Enum类。
# 注意:
#
# 　　定义枚举时，成员名称不允许重复　
#
# 　　默认情况下，不同的成员值允许相同。但是两个相同值的成员，第二个成员的名称被视作第一个成员的别名　
#
# 　　　如果枚举中存在相同值的成员，在通过值获取枚举成员时，只能获取到第一个成员
#
# 　如果要限制定义枚举时，不能定义相同值的成员。可以使用装饰器@unique【要导入unique模块】
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
if __name__ == '__main__':
    for name, member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)
