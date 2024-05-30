import crypt
import time
from argon2 import PasswordHasher

salt = "$2y$10$/oi7iOXQUZfteF9imxBrmu"
target = "$2y$10$/oi7iOXQUZfteF9imxBrmuJgh3c7RdWxkjedZY95ga6DLWyJOuq.q"
passchar_list = "aps01"
for i0 in passchar_list:
    passchar0 = i0
    for i1 in passchar_list:
        passchar1 = i1
        for i2 in passchar_list:
            passchar2 = i2
            for i3 in passchar_list:
                passchar3 = i3
                for i4 in passchar_list:
                    passchar4 = i4
                    for i5 in passchar_list:
                        passchar5 = i4
                        passwd = passchar0 + passchar1 + passchar2 + passchar3 + passchar4 + passchar5
                        ph = PasswordHasher()
                        flag = False
                        try:
                            flag = ph.verify(target, passwd)
                        except:
                            pass
                        #cpass = crypt.crypt(passwd, salt)
                        #print(passwd)
                        #if cpass == target:
                        print("Yes" + target)
                        print(passwd)
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

