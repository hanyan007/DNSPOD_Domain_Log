# DNSPOD_Domain_Log

HTTP请求方式：
POST
请求参数：
参数名	是否必须	参数描述
公共参数	是	详见：公共参数
domain_id 或 domain	是	分别对应域名ID和域名, 提交其中一个即可
offset	否	记录开始的偏移，第一条记录为 0，依次类推，默认为0
length	否	共要获取的日志条数，比如获取20条，则为20，默认为500条，单次最多获取500条

响应代码：
共通返回
-7 企业账号的域名需要升级才能设置
-8 代理名下用户的域名需要升级才能设置
6 域名ID错误
8 非域名所有者



CODE

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask import request
import sys
import urllib
import urllib2

reload(sys)
sys.setdefaultencoding('utf-8')
app = Flask(__name__)

@app.route('/')
def welcome():
    lt= [] #将结果导入list
    posturl = 'https://dnsapi.cn/Domain.Log'  #dnspod接口
    postdata = {'login_token':'10xxxxxxxxxxxfc0','format':'json','domain':'keaaa.com','length':'20'}#json格式的请求参数
    req = urllib2.Request(posturl)
    data = urllib.urlencode(postdata) #post数据需要urlencode()下，将字典转换成“data1=value1&data2=value2”的格式
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(req,data)
    result = response.read()
    list = eval(result)  #将str返回为list
    for i in list['log']:   #读取每条记录再逐条做Unicode编码
            log= i.decode("unicode_escape")
            lt.append(log)  #将结果导入list
    return render_template('index.html', var1 = lt)  #返回数据到html

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port = 80)  #启动端口
