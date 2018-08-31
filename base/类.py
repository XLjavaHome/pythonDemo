# 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名
# classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。

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
    @classmethod
    def func2(cls):
        print('先加载')

student = Student("Hugh", 99)
# 将student属性打印
print(student.name)
print(student.score)
# print(student.age)  报错
print(student.getAge())
student.print_score()
Student.func2()
student.func2()
