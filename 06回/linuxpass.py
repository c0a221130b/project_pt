import crypt
import time
salt = '$6$3Ffxg.BoNMqKoJju$'
target = '$6$3Ffxg.BoNMqKoJju$qnUED0MSKUa3NFMTobsYIEX2KbdzKUX3m5IQFt18UNQT5QWqE98eO/NSVBEm9gtzv0Y9BmJTOxFejm/w1x.1Q1'

#salt = '$y$j9T$N.wFWcOy78xPlkAr3SEbb1$'
#target = '$y$j9T$N.wFWcOy78xPlkAr3SEbb1$iMaBbwHBzVtb43r45BzMn/jTktZ08yA316xqzeTRyDC'
passchar_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!#'

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
                                #print(passwd)
                                if i6 == len(passchar_list)-1:
                                    print(time.time() - start_t)
                                    start_t = time.time()
                                    
                                if cpass == target:
                                    print("Yes" + cpass)
                                    print(passwd)
                                    end_t = time.time()
                                    elapsed_t = end_t - start_t
                                    print(f"{elapsed_t} s")
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
        else:
            continue
        break
    else:
        continue
    break