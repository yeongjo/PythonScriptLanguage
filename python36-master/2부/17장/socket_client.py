# -*- coding:cp949 -*-
import socket

HOST = '127.0.0.1' #localhost
PORT = 50007 #������ ���� ��Ʈ�� ����մϴ�.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #���� ����
s.connect((HOST, PORT))
s.send(b'Hello, python') #���ڸ� �����ϴ�.
data = s.recv(1024) #�����κ��� ������ �޽��ϴ�.
s.close()
print('Received', repr(data))