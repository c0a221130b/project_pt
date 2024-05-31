import crypt
import time

salt = "$2y$10$ecRmAWY4n/jLa0tTzIaG7."
target = "$2y$10$ecRmAWY4n/jLa0tTzIaG7.SMhb1TfdROy3nXeG5aVZorUX1n6/WHO"

passchar_list = "abcdefghijklmnopqrstuvwxyz1234567890"
start_t = time.time()
for i0 in range(len(passchar_list)):
    passchar0 = passchar_list[i0]
    for i1 in range(len(passchar_list)):
        passchar1 = passchar_list[i1]
        for i2 in range(len(passchar_list)):
            passchar2 = passchar_list[i2]
            for i3 in range(len(passchar_list)):
                passchar3 = passchar_list[i3]
                for i4 in range(len(passchar_list)):
                    passchar4 = passchar_list[i4]
                    for i5 in range(len(passchar_list)):
                        passchar5 = passchar_list[i5]
                        for i6 in range(len(passchar_list)):
                            passchar6 = passchar_list[i6]
                            for i7 in range(len(passchar_list)):
                                passchar7 = passchar_list[i7]
                                passwd = passchar0 + passchar1 + passchar2 + passchar3 + passchar4 + passchar5 + passchar6 + passchar7
                                cpass = crypt.crypt(passwd, salt)
                                print(passwd)
                                if cpass == target:
                                    print("Yes" + cpass)
                                    print(passwd)
                                    break
                            else:
                                continue
                            break
                        else:
                            print(time.time() - start_t)
                            start_t = time.time()
                            continue
                        break
                    else:
                        continue
                    break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        break
    else:
        continue
    break