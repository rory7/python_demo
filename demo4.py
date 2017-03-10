# coding=utf-8

# python file相关操作
# python 异常处理

# 1.异常处理
'''
try:
<语句>        #运行别的代码
except <名字>：
<语句>        #如果在try部份引发了'name'异常
except <名字>，<数据>:
<语句>        #如果引发了'name'异常，获得附加的数据
else:
<语句>        #如果没有异常发生
'''


# try:
#     fh = open("demo1.py")
#     fh.write("test file")
# except IOError, Argument:
#     print "find IOerror cant find or read file"
#     print Argument.__str__()
# else:
#     print "write success for test"
# finally:
#     fh.close()

# raise 触发异常
def func(lv):
    if lv > 0:
        raise Exception("invalid lv!", lv)


# try:
#     func(1)
# except "invalid lv!", Argument:
#     print Argument.__str__()

# 自定义异常
class CustomError(RuntimeError):
    def __init__(self, arg):
        self.args = arg


try:
    raise CustomError("bad run")
except CustomError, e:
    print e.args
