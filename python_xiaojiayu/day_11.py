'''
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def print_score(self):
        print('%s:%s'%(self.name,self.score))
    
    def get_grade(self):
        if self.score>=90:
            return print('A')
        elif self.score>=60:
            return print('B')
        else:
            return print('C')
    
bart=Student('LIU',59)
bart.print_score()
bart.get_grade()

class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score

    def get_name(self):
        return self.__name

    def set_score(self,score):
        self.__score=score
'''
class Student(object):
    def __init__(self,name,gender):
        self.name=name
        self.__gender=gender

    def get_gender(self):
        return self.__gender

    def set_gender(self,gender):
        self.__gender=gender

bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
a=[1,2,4]
print(isinstance(a,list))