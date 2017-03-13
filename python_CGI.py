# conding=utf-8

# python CGI

'''
CGI架构
    |- - - - - - - - - - - - - - - - - - - - - - - -|
    |                  Browser                      |
    |                                               |
    |  Html          JavaScript             Css     |
    |- - - - - - - - - - - - - - - - - - - - - - - -|

                      Internet
    |- - - - - - - - - - - - - - - - - - - - - - - -|
    |                  WebServer                    |
    |                                               |
    |  DataBase         执行 CGI       FileSystem    |
    |- - - - - - - - - - - - - - - - - - - - - - - -|
'''

'''
进行CGI编程前，确保您的Web服务器支持CGI及已经配置了CGI的处理程序。
Apache 支持CGI 配置：
设置好CGI目录：
ScriptAlias /cgi-bin/ /var/www/cgi-bin/
所有的HTTP服务器执行CGI程序都保存在一个预先配置的目录。这个目录被称为CGI目录，并按照惯例，它被命名为/var/www/cgi-bin目录。
CGI文件的扩展名为.cgi，python也可以使用.py扩展名。

指定其他运行CGI脚本的目录，可以修改httpd.conf配置文件，如下所示：
<Directory "/var/www/cgi-bin">
   AllowOverride None
   Options +ExecCGI
   Order allow,deny
   Allow from all
</Directory>

在 AddHandler 中添加 .py 后缀，这样我们就可以访问 .py 结尾的 python 脚本文件：
AddHandler cgi-script .cgi .pl .py
'''

'''
HTTP头部的格式如下：
HTTP 字段名: 字段内容
    头	                    描述
Content-type:	请求的与实体对应的MIME信息。例如: Content-type:text/html
Expires: Date	响应过期的日期和时间
Location: URL	用来重定向接收方到非请求URL的位置来完成请求或标识新的资源
Last-modified: Date	请求资源的最后修改时间
Content-length: N	请求的内容长度
Set-Cookie: String	设置Http Cookie
'''

'''
CGI环境变量
所有的CGI程序都接收以下的环境变量，这些变量在CGI程序中发挥了重要的作用：
CONTENT_TYPE	这个环境变量的值指示所传递来的信息的MIME类型。目前，环境变量CONTENT_TYPE一般都是：application/x-www-form-urlencoded,他表示数据来自于HTML表单。
CONTENT_LENGTH	如果服务器与CGI程序信息的传递方式是POST，这个环境变量即使从标准输入STDIN中可以读到的有效数据的字节数。这个环境变量在读取所输入的数据时必须使用。
HTTP_COOKIE	客户机内的 COOKIE 内容。
HTTP_USER_AGENT	提供包含了版本数或其他专有数据的客户浏览器信息。
PATH_INFO	这个环境变量的值表示紧接在CGI程序名之后的其他路径信息。它常常作为CGI程序的参数出现。
QUERY_STRING	如果服务器与CGI程序信息的传递方式是GET，这个环境变量的值即使所传递的信息。这个信息经跟在CGI程序名的后面，两者中间用一个问号'?'分隔。
REMOTE_ADDR	这个环境变量的值是发送请求的客户机的IP地址，例如上面的192.168.1.67。这个值总是存在的。而且它是Web客户机需要提供给Web服务器的唯一标识，可以在CGI程序中用它来区分不同的Web客户机。
REMOTE_HOST	这个环境变量的值包含发送CGI请求的客户机的主机名。如果不支持你想查询，则无需定义此环境变量。
REQUEST_METHOD	提供脚本被调用的方法。对于使用 HTTP/1.0 协议的脚本，仅 GET 和 POST 有意义。
SCRIPT_FILENAME	CGI脚本的完整路径
SCRIPT_NAME	CGI脚本的的名称
SERVER_NAME	这是你的 WEB 服务器的主机名、别名或IP地址。
SERVER_SOFTWARE	这个环境变量的值包含了调用CGI程序的HTTP服务器的名称和版本号。例如，上面的值为Apache/2.2.14(Unix)
'''

# CGI环境变量输出
import os

print "Content-type: text/html"
print
print "<meta charset=\"utf-8\""
print "<b>path</b><br>"
print "<ul>"
for key in os.environ.keys():
    print "<li><span style='color:green'>%30s</span>:%s</li>" % (key, os.environ[key])
print "</ul>"
