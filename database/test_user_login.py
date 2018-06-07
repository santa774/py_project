# -*- coding: utf-8 -*-
import hashlib
from database import TestMysqlHelper


def login():
    username = input("输入用户名")
    passwd = input("输入密码")

    sha1 = hashlib.sha1()
    sha1.update(passwd.encode("utf-8"))
    sha1_passwd = sha1.hexdigest()

    helper = TestMysqlHelper.MysqlHelper("localhost", 3306, "studydb", "root", "233333")
    sql = "select upwd from userinfos where uname=%s"
    data = (username,)
    result = helper.get_one(sql, data)
    if result[0] == sha1_passwd:
        print("登录成功")
    else:
        print("登录失败")
    pass


if __name__ == "__main__":
    login()

