# 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        #     私有的加上"__"
        self.__age = score
    def getAge(self):
        return self.__age
    def print_score(self):
        print("%s: %s" % (self.name, self.score))
student = Student("Hugh", 99)
# 将student属性打印
print(student.name)
print(student.score)
# print(student.age)  报错
print(student.getAge())
student.print_score()
