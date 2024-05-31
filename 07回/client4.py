import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('192.168.65.3', 80))

'''
msg = 'GET /login/login.php HTTP/1.1\r\n'
msg = msg + 'Host: 192.168.65.3\r\n'
msg = msg + 'Connection: keep-alive\r\n'
msg = msg + '\r\n'
msg = msg + 'user_name=root&password=abcd1234\r\n'
'''

msg = "POST /login/login.php HTTP/1.1\r\n"
msg = msg + 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7\r\n'
msg = msg + 'Accept-Encoding: deflate\r\n'
msg = msg + 'Accept-Language: ja,en-US;q=0.9,en;q=0.8\r\n'
msg = msg + 'Cache-Control: max-age=0\r\n'
msg = msg + 'Connection: keep-alive\r\n'
msg = msg + 'Content-Length: 32\r\n'
msg = msg + 'Content-Type: application/x-www-form-urlencoded\r\n'
msg = msg + 'Cookie: PHPSESSID=l55o78q1bac496lp7e5i6b5tm4\r\n'
msg = msg + 'Host: 192.168.65.3\r\n'
msg = msg + 'Origin: http://192.168.65.3\r\n'
msg = msg + 'Referer: http://192.168.65.3/login/login.php\r\n'
msg = msg + 'Upgrade-Insecure-Requests: 1\r\n'
msg = msg + 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36\r\n'
msg = msg + '\r\n'
msg = msg + 'user_name=root&password=abcd1235\r\n'
cmd = msg.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()