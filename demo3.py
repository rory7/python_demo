# coding=utf-8
# IO操作
'''
str = raw_input("input:")
print str
'''

# def getInput():
#     return raw_input("please input")
#
#
# def str_out():
#     return "1234"
#
#
# def outInput():
#     str = input(str_out())
#     return str
#
#
# print outInput()

# 打开／关闭文件
f = open('demo1.py', 'r', -1)
name = f.name
mode = f.mode
softspace = f.softspace
iscolse = f.closed

# print name
# print mode
# print softspace
# print iscolse

# f.close()
# print name
# print f.name
# f.write()
# f.read()

f.read(10)
print f.tell()

import os

# os.rename("test.txt", "newTest.txt")
# os.remove("test.txt")
# os.mkdir('test')
# os.chdir("t")
# os.getcwd()
# print os.getcwd()
# os.rmdir()
