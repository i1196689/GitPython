'''
class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('dog is running...')

def twice(animal):
    animal.run()
    animal.run()
dog=Dog()
twice(dog)


class Student(object):
    count=0
    def __init__(self,name):
        self.name=name
        Student.count+=1
# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
'''
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value <0 or value >100:
            raise ValueError('score must between 0~100 !')
        self._score=value
s=Student()
s.score=60
print(s.score)
