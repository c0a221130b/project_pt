import crypt

salt = "$1$AGCDEFGH"
#target = "$1$ABCDEFGH$gj9oqOTTYQtUtHtvpcQab0"
target = "$1$ABCDEFGH$v8ioE16z9/YKebnOefllg/"

fname = "dictpasswd.txt"
with open(fname, "r") as f:
    dictpasswds = f.readlines()
    for dictpasswd in dictpasswds:
        passwd = dictpasswd.rstrip("\n")
        cpass = crypt.crypt(passwd, salt)
        if cpass == target:
            print('Yes', cpass)
            break