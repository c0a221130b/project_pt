import crypt

salt = "CG"
target = 'CG24gtUBCD1bA'

passwdchar_list = "abcdefghijklmnopqrstuvwxyz1234567890"
for i0 in passwdchar_list:
    passwd0 = i0
    for i1 in passwdchar_list:
        passwd1 = i1
        for i2 in passwdchar_list:
            passwd2 = i2
            for i3 in passwdchar_list:
                passwd3 = i3
                for i4 in passwdchar_list:
                    passwd4 = i4
                    for i5 in passwdchar_list:
                        passwd5 = i5
                        passwd = passwd0 + passwd1 + passwd2 + passwd3 + passwd4 + passwd5
                        print(passwd)
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