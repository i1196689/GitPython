import hashlib
def calc_md5(password):
    psw=hashlib.md5()
    psw.update(("%s" % (password)).encode("utf-8"))
    print(psw.hexdigest())
calc_md5(123456789)