import random
class ant(object):
    distance=0
    ants_name=[]
    ant_count=0
    def rnd_distance(self):
        return random.randint(1,10)
    def set_name(self,name):
        self.name=name
        ant.ant_count+=1
        ant.ants_name.append(self.name)
        return print('共有%s只蚂蚁.我的名字是%s,大家的名字是%s.'%(ant.ant_count,self.name,ant.ants_name))
    def run(self):
        ant_self_distance=self.rnd_distance()
        ant.distance=ant.distance+ant_self_distance
        return print('我跑了%s米,所有蚂蚁一共跑了%s米.'%(ant_self_distance,ant.distance))
   





