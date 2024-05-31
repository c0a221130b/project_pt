import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('192.168.65.3', 80))
msg = 'GET /test/test.html HTTP/1.1\r\n'
msg = msg + 'Host: 192.168.65.3\r\n'
msg = msg + 'Connection: keep-alive\r\n'
msg = msg + '\r\n'
cmd = msg.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()