#登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。
import hashlib
s=input("input password:")
s=s.replace("input password:","")
md5=hashlib.md5()
md5.update(s.encode("utf-8"))
aims=md5.hexdigest()
print(aims)