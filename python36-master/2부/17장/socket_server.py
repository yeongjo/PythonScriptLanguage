# -*- coding:cp949 -*-
import socket

HOST = '' #ȣ��Ʈ�� �������� ������ ������ ��� �������̽��� �ǹ��մϴ�.
PORT = 50007 #��Ʈ�� �����մϴ�.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1) #������ ���� ������ ��ٸ��ϴ�.
conn, addr = s.accept() #������ �����մϴ�.
print('Connected by', addr)
while True:
    data = conn.recv(1024)
    if not data: break
    conn.send(data) #���� �����͸� �״�� Ŭ���̾�Ʈ�� �����մϴ�.
conn.close()