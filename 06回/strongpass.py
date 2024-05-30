import crypt

#salt = "$6$lu0siAR8yeSoFm1n"
salt = "$6$ABCDEFGHIGKLMNOP"
#password = "P1abck2#"
target = "$6$ABCDEFGHIJKLMNO$9CwI7hcVhjzeQHwYZlZbYrOOaqCUZ2MROEOsfZQJfJLI4S.BxWZkQ7/vO6I2hzttDSeBV3rZRUcKsCcEMBhkO1"
passwdchar_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!"
passwdchar_list8 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!"


for i2 in passwdchar_list[52:-1]:
    passchar2 = i2
    for i3 in passwdchar_list[:26]:
        passchar3 = i3
        for i4 in passwdchar_list[:26]:
            passchar4 = i4
            for i5 in passwdchar_list:
                passchar5 = i5
                for i6 in passwdchar_list:
                    passchar6 = i6
                    for i7 in passwdchar_list8:
                        passchar7 = i7
                        passwd1 = "P" + passchar2 + passchar3 + passchar4 + passchar5 +  'k' + passchar6 + passchar7
                        passwd2 = "P" + passchar2 + passchar3 + passchar4 + passchar5 + passchar6 + 'k' + passchar7
                        cpass1 = crypt.crypt(passwd1, salt)
                        cpass2 = crypt.crypt(passwd2, salt)
                        print(passwd1 , passwd2)
                        if cpass1 == target:
                            print("Yes " + cpass1)
                            #print(passwd1)
                            break
                        elif cpass2 == target:
                            print("Yes " + cpass2)
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