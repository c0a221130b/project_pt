import crypt

salt = "$1$AGCDEFGH$"
target = "$1$ABCDEFGH$RtWtIqwUqVEkVB5B9dRJv1"
passwdchar_list = "1234567890"

fname = "dictpasswd.txt"
with open(fname, "r") as f:
    dictpasswds = f.readlines()
    for dictpasswd in dictpasswds:
        passwd0 = dictpasswd.rstrip("\n")
        for i1 in passwdchar_list:
            passwd1 = i1
            for i2 in passwdchar_list:
                passwd2 = i2
                for i3 in passwdchar_list:
                    passwd3 = i3
                    passwd_1 = passwd0 + passwd1 + passwd2 + passwd3
                    passwd_2 = passwd1 + passwd2 + passwd3 + passwd0
                    print(passwd_1, passwd_2)
                    cpass_1 = crypt.crypt(passwd_1, salt)
                    cpass_2 = crypt.crypt(passwd_2, salt)
                    if cpass_1 == target or cpass_2 == target:
                        print("Yes ", target)
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
