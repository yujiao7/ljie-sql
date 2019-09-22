#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/9'
# 搭一个注册环境
from flask import Flask, request, jsonify

from mysql_tools import mysql_db

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'
# 装饰器
@app.route('/signup/',methods=['POST'])
def signup():
    data = request.form
    # data = request.json
    # print(sql)
    # print()
    #连接数据库插入数据 先连接数据库
    sql = "insert into `user` (password,phone,username) values('{}','{}','{}');" .format(data.get ('password'),data.get ('phone'),data.get ('username'))

    mydb = mysql_db(host="qa.yansl.com", user="root", password="root", database="practise")
    res = mydb.update_execute(sql)
    print(res)
    resp = "{'code':{},'message':{}"
    code = 2000 #成功
    message = '注册成功'
    if(not res):
        code = 4000 #失败
        message = '注册失败'
        data ={
            "code":code,
            "message":message
        }
        resp = jsonify(data)
        return resp
    # print(data.get("username"))
    # print(data)
    return '我是注册界面'

if __name__ == '__main__':
    app.run()

# 验证数据重复
