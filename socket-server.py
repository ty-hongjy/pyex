'''
Description: 
Autor: name
Date: 2023-03-20 16:47:51
LastEditors: name
LastEditTime: 2024-03-16 09:09:10
'''
#!python3
#!coding='utf-8'

import socket
import threading
import time


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    name="c:\\"+str(addr)+".txt"
    file=open(name,"a")
    ref=0
    while True:
        data = sock.recv(1024)
        if data:
        	file.write( str(ref)+":"+data.decode('utf-8')+"\n" )
        	print("收到"+str(addr)+"的第"+str(ref)+"条数据！")
        	sock.send(data)

        if data.decode('utf-8') == 'exit':
        	sock.close()
        	file.close()
        	break


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.10.21',9999))
s.listen(5)
print("快来连接!")
while True:
	sock,addr=s.accept()
	t=threading.Thread(target=tcplink,args=(sock,addr))
	t.start()

