# coding=utf-8˝
# ! code 1
print "hello,python";

count = 1
test = 'test'
myCode = test + count.__str__()
print myCode

ts = ['1', '2', '3']
tiny = [13, "123", "1123"]
print ts
print tiny
print ts[0] + "\n" + tiny[1].__str__() * 2

# 元组不能二次赋值，相当于只读list
py = (ts, tiny)
print py

# 字典
dt = {}
dt['1'] = 123
dt['2'] = '123'
print dt.keys()
print dt.values()
print dt["1"]

# number(数字)
var1 = 1
var2 = 2
var3 = 3
del var1
var1 = 10
print var1
print var2
print var3

# 字符串格式化
print 'test %s and count %d' % ('123', 21)

# 三引号

hi = '''hi
there '''
hi  # repr()
'hi\nthere'
print hi


def printTest(str):
    print str
