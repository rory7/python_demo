# coding=utf-8

'''
python面向对象

create class
--
class ClassName:
   '类的帮助信息'   #类文档字符串
   class_suite  #类体
--
'''

# class Obj:
#     def __init__(self):
#         pass
#
#     def prt(self):
#         print (self)
#         print (self.__class__)
#
#
# t = Obj()
# t.prt()

'''
创建实例对象
"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
'''


class Employee:
    empCount = 0

    def __init__(self, str, arg):
        self.str = str
        self.arg = arg
        self.empCount += 1

    def display(self):
        print self.empCount

    def prtStr_Arg(self):
        print self.str + "--" + self.arg


emp1 = Employee("111", "12")
emp2 = Employee("222", "22")
emp1.display()
emp1.prtStr_Arg()
emp2.display()
emp2.prtStr_Arg()

'''
python 内置类属性
__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
'''

'''
python垃圾回收
Python 使用了引用计数这一简单技术来跟踪和回收垃圾。
在 Python 内部记录着所有使用中的对象各有多少引用。
一个内部跟踪变量，称为一个引用计数器。
当对象被创建时， 就创建了一个引用计数， 当这个对象不再需要时， 也就是说， 这个对象的引用计数变为0 时， 它被垃圾回收。
但是回收不是"立即"的， 由解释器在适当的时机，将垃圾对象占用的内存空间回收。

垃圾回收机制不仅针对引用计数为0的对象，同样也可以处理循环引用的情况。循环引用指的是，两个对象相互引用，但是没有其他变量引用他们。
这种情况下，仅使用引用计数是不够的。Python 的垃圾收集器实际上是一个引用计数器和一个循环垃圾收集器。
作为引用计数的补充， 垃圾收集器也会留心被分配的总量很大（及未通过引用计数销毁的那些）的对象。
在这种情况下， 解释器会暂停下来， 试图清理所有未引用的循环。

'''
