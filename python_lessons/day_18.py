import json 

class Product:
    def __init__(self,d):
        self.__dict__=d

f=open("product.json","r")
jsonStr=f.read()
print(jsonStr)
product=json.loads(jsonStr,object_hook=Product)
print(type(product))
print(product.name)
print(product.price)