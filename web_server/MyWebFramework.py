# -*-coding:utf-8-*-
import time

STATIC_PAGE_ROOT_LOCATION = "./html"
DYNAMIC_PAGE_ROOT_LOCATION = "./wsgipython"

class WebFramework():
    def __init__(self, urls):
        self.urls = urls


    def __call__(self, environ, start_response):
        requestPageName = environ.get("PATH_INFO", "/")
        if requestPageName.startswith("/static"):
            try:
                print(requestPageName)
                file = open(STATIC_PAGE_ROOT_LOCATION + requestPageName[7:], "rb")
            except:
                status = "404 NOT_FOUND"
                headers = []
                start_response(status, headers)
                return "not found"
            else:
                pageData = file.read()
                status = "200 OK"
                headers = []
                start_response(status, headers)
                file.close()
                return pageData.decode("utf-8")

        for request_action, handler in self.urls:
            if request_action == requestPageName:
                return handler(environ, start_response)

        # 没有找到的情况
        status = "404 NOT_FOUND"
        headers = []
        start_response(status, headers)
        return "not found"


def show_time(environ, start_response):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    start_response(status, headers)
    return time.ctime()


def say_hello(environ, start_response):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    start_response(status, headers)
    return "say_hello!!!!!!!!!!"

urls = {
    ("/", show_time),
    ("/ctime", show_time),
    ("/sayhello", say_hello)
}
app = WebFramework(urls)
