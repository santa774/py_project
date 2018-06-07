# -*- coding:utf-8 -*-
import socket
import re
from multiprocessing import Process

PAGE_ROOT_LOCATION = "./html"


class HttpServer():
    def __init__(self):
        self.serSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 复用socket
        self.serSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def bind_addr(self, addr):
        self.serSocket.bind(addr)

    def start(self):
        self.serSocket.listen(10)
        while True:
            clientSocket, newAddr = self.serSocket.accept()
            print("%s , %s连接上了" % (newAddr))
            clientProcess = Process(target=self.handleClient, args=(clientSocket,))
            clientProcess.start()
            clientSocket.close()

    # 处理客户端请求
    def handleClient(self, clientSocket):
        # 接受客户发送的请求
        requestData = clientSocket.recv(1024)
        print("收到的数据:%s" % (requestData))
        # 拆分获取请求中的具体请求页面，使用正则表达式提取出需要的数据
        requestDataList = requestData.splitlines()
        requestHeader = requestDataList[0]  # excample: GET / HTTP/1.1
        print(requestHeader.decode("utf-8"))
        requestPageName = re.match(r"\w+ +(/[^ ]*) ", requestHeader.decode("utf-8")).group(1)
        if "/" == requestPageName:
            requestPageName = "/index.html"

        try:
            print(requestPageName)
            file = open(PAGE_ROOT_LOCATION + requestPageName, "rb")
        except:
            responseHeaderLines = "HTTP/1.1 404 Not Found\r\n"
            responseHeaderLines += "Server: my server\r\n"
            responseHeaderLines += "\r\n"
            responseBody = "The page is not find"
        else:
            pageData = file.read()
            file.close()
            responseHeaderLines = "HTTP/1.1 200 OK\r\n"
            responseHeaderLines += "Server: my server\r\n"
            responseHeaderLines += "\r\n"
            responseBody = pageData.decode("utf-8")

        response = responseHeaderLines + responseBody
        clientSocket.send(bytes(response, "utf-8"))
        clientSocket.close()


def main():
    serSocket = HttpServer()
    serSocket.bind_addr(("", 8000))
    serSocket.start()


if __name__ == "__main__":
    main()
