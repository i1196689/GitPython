'''
class Student():
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def get_name(self):
        if isinstance(self.name,str):
            return self.name
    def get_age(self):
        if isinstance(self.age,int):
            return self.age
    def get_score(self):
        if isinstance(self.score,int):
            return self.score
zm=Student('xiaoping',20,80)
print(zm.name)
print(zm.age)
print(zm.score)

class Student():
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def get_name(self):
        if isinstance(self.name,str):
            return self.name
    def get_age(self):
        if isinstance(self.age,int):
            return self.age
    def get_score(self):
        if isinstance(self.score,int):
            return self.score
'''
class Dictclass():
    def __init__(self,class1):
        self.class1=class1
    def del_dict(self,key):
        if key in self.class1.keys():
            def self.class1[key]
            return self.class1
        return 'No!'
    def get_dict(self,key):
        if key in self.class1.keys():
            return self.class1[key]
        return 'not found!'


