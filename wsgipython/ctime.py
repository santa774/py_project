import time

#wsgi规范，需要传2个参数，第一个是请求头的字典，第二个是处理函数
def application(environ, start_response):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    start_response(status, headers)
    return time.ctime()