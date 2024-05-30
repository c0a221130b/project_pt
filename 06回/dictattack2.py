import crypt
salt = "$1$ABCDEFGH$"
target = "$1$ABCDEFGH$/3XvwCiaQ.3NBkhnySA3V0"
#password = 'TokyoNagoyaOakaNagoya'

fname = "./passphrase.txt"
with open(fname, "r") as f:
    passphrases1 = f.readlines()
    passphrases2 = f.readlines()
    passphrases3 = f.readlines()
    passphrases4 = f.readlines()
    
    for passphrase1 in passphrases1:
        passwd1 = passphrase1.rstrip("\n")
        for passphrase2 in passphrases2:
            passwd2 = passphrase2.rstrip("\n")
            for passphrase3 in passphrases3:
                passwd3 = passphrase3.rstrip('\n')
                for passphrase4 in passphrases4:
                    passwd4 = passphrase4.rstrip('\n')
                    passwd0 = passwd1 + passwd2 + passwd3 + passwd4
                    cpass = crypt.crypt(passwd0, salt)
                    if cpass == target:
                        print('Yes', cpass)
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