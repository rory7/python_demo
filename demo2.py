# coding=UTF-8
# 函数定义
def testfunc(str):
    r = '测试函数传入的字符串是' + str.__str__()
    return r;


def printStr(str):
    print str;
    return


printStr(testfunc("sss"))

# 导入模块
import demo_support

demo_support.ptStr("test")

# 导入模块指定函数

from demo1 import printTest

printTest("test2")

# reload func
reload(demo_support.ptStr("11"))
