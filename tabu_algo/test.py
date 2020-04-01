class Test(object):
    def __init__(self):
        self.test_0=0
        self.test_1=1
        self.test_2=2

a=Test()
s=a.__dict__
s.pop('test_0')
print(s)
