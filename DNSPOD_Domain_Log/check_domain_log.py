#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-22
# @Author  : hanyan_news
# @Link    : https://raw.githubusercontent.com/hanyan007/DNSPOD_Domain_Log
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
    postdata = {'login_token':'10xxxxxxxxxxxxxx','format':'json','domain':'keabc.com','length':'20'}#json格式的请求参数
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

