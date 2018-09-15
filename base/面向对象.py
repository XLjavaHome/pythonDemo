std1 = {'name': 'Michael', 'score': 98}
std2 = {'name': 'Bob', 'score': 81}


# 而处理学生成绩可以通过函数实现，比如打印学生的成绩：
def print_score(std):
    print('%s: %s' % (std['name'], std['score']))


print_score(std1)
print_score(std2)


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


michael = Student('Michael', 98)
bob = Student('Bob', 81)
michael.print_score()
bob.print_score()
'''__call__() 函数
__call__()函数可以使一个类实例像函数一样被调用。 
下面以斐波那契数列为例来说明__call__() 函数的用途。斐波那契数列（Fibonacci sequence）在数学上以如下递归的方法定义：F(0)=0，F(1)=1, F(n)=F(n-1)+F(n-2)（n>=2，n∈N*）。也就是后一个数为前两个数相加，具体数值为：0、1、1、2、3、5、8、13、21、34、…… 
使用面向对象编程的代码如下：
在定义Fib类中使用了__call__() 函数，使得实例 f 可以像函数一样被调用，f(10)中的10 对应就是__call__() 函数中的参数 num 。
'''
class Fib(object):
    def __init__(self):
        pass
    def __call__(self,num):
        a,b = 0,1;
        self.l=[]

        for i in range (num):
            self.l.append(a)
            a,b= b,a+b
        return self.l
 # 输出前10个斐波那契数列
f = Fib()
print(f(10))
