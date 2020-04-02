#!user/bin/env python
# _*_ coding: utf-8 _*_
 
# @Version :   1.0
# @Author  :   liujunkong
# @Email   :   1196689756@qq.com
# @Time    :   2020/03/28 18:13:30
#Description:
 
#from add_time import timers
import math,random,copy,time
import numpy as np
import pandas as pd
from pandas.core.series import Series
from matplotlib import pyplot as plt


L_1=[47, 15, 29, 57, 52, 40, 20, 44, 45, 65, 12, 32, 50, 67, 33, 9, 30, 42, 11, 13, 60, 
18, 8, 59, 23, 31, 28, 6, 41, 55, 66, 19, 49, 24, 1, 56, 5, 43, 38, 39, 46, 70, 22, 26, 
4, 36, 25, 3, 69, 17, 61, 37, 7, 63, 21, 51, 54, 35, 2, 10, 34, 53, 62, 16, 27, 58, 48, 64, 68, 14]
L_2=[58021.555, 58188.973, 58438.129, 58198.211, 58139.844, 58130.465, 58224.496, 58210.168, 
58008.453, 58201.094, 58151.91, 58088.086, 58245.402, 58153.391, 58309.773, 57871.414, 58140.707, 
57811.164, 58446.582, 58526.051, 58034.395, 58022.969, 58467.906, 57427.84, 58113.273, 58020.02, 
58064.785, 58328.859, 58158.246, 58165.406, 57683.879, 58033.598, 58147.195, 58269.109, 58137.215, 
58146.219, 58490.207, 58285.211, 58373.438, 57637.551, 58130.953, 58334.555, 58334.188, 58211.605, 
58104.137, 57979.859, 58101.453, 57959.086, 58108.949, 58065.789, 58145.563, 58012.012, 58358.555, 
58045.586, 58227.848, 57842.711, 58148.449, 58487.664, 58519.691, 57871.137, 58167.398, 58023.844, 
57908.699, 57956.043, 58291.84, 58421.148, 57879.496, 57877.262, 57843.551, 58268.633]

L=zip(L_1,L_2)
L=dict(L)





class SA_Tabu(object): 

    def __init__(self,L=L,t=0.001,T=100,each_T_internations=100,
                            T_descent_rate=0.9,threshold_value=0.1,
                            threshold_t=1,re_T=40,len_list=10): 
        self.L                   = L                   #字典
        self.t                   = t                   #终止温度
        self.T                   = T                   #起始温度        
        self.each_T_internations = each_T_internations #当前温度下的迭代次数
        self.T_descent_rate      = T_descent_rate      #温度下降率
        self.threshold_value     = threshold_value     #加入禁忌表阈值
        self.threshold_t         = threshold_t         #启动候选列表的温度阈值
        self.re_T                = re_T                #候选解的运行的温度
        self.len_list            = len_list           #程序终止条件(禁忌列表长度)
        self.rmb_value_list,self.rmb_blade_order_list,self.out_all_list  = [],[],[] #记忆优值(禁忌表) #记忆优值对应的列表
        
         

    @property
    def sita(self): 
        create_sita = [i*2*math.pi/len(self.L) for i in range(len(self.L))]#
        return create_sita

    def cal_total_distance(self,blade_order): #目标函数
        self.blade_order = blade_order
        blade_order_x,blade_order_y,count = 0, 0, 0
        for each in self.blade_order: 
            blade_order_x += math.sin(self.sita[count])*self.L[each]
            blade_order_y += math.cos(self.sita[count])*self.L[each]
            count         += 1
        goal           = blade_order_x**2+blade_order_y**2
        return goal**0.5
    
    @property
    def Rnd_blade_order(self): #随机顺序
        blade_order = list(np.random.permutation(len(self.L)))
        blade_order = [i+1 for i in blade_order]
        return blade_order
    
    def change_blade_position(self,blade_order):#交换两个叶片位置的函数
        self.blade_order=blade_order
        Rnd_1 = random.randint(0,len(self.L) - 1)
        Rnd_2 = random.randint(0,len(self.L) - 1)
        while Rnd_1 == Rnd_2:
            Rnd_1 = random.randint(0,len(self.L) - 1)
        temp = self.blade_order[Rnd_1]
        self.blade_order[Rnd_1] = self.blade_order[Rnd_2]
        self.blade_order[Rnd_2] = temp
        return self.blade_order

    def blade_weight(self,blade_list):
        self.blade_list=blade_list
        out=[L[i] for i in self.blade_list]
        return out





    @property
    def Rnd(self): #生成随机数
        return random.random()

    @property
    def run(self):
        blade_order = self.Rnd_blade_order
        out         = self.cal_total_distance(blade_order)
        while self.T>self.t:
            self.T=self.T*self.T_descent_rate
            for i in range(self.each_T_internations):
                temp_list=blade_order.copy()
                blade_order_new = self.change_blade_position(blade_order)
                out_new         = self.cal_total_distance(blade_order_new)
                delta           = out_new-out
                if delta < 0: 
                    blade_order = blade_order_new
                    out         = out_new
                    '''
                    if out < self.threshold_value and out not in self.rmb_value_list:
                        self.rmb_value_list.append(out)
                        self.rmb_blade_order_list.extend([blade_order])
                    '''
                else:
                    if self.T < self.threshold_t and out < self.threshold_value:
                        self.T = self.re_T
                        if out not in self.rmb_value_list:
                            self.rmb_value_list.append(out)
                            self.rmb_blade_order_list.extend([blade_order])
                        blade_order = blade_order_new
                        out         = out_new
                        break;
                    else:
                        if self.Rnd < math.e**(-delta/self.T):
                            blade_order = blade_order_new
                            out         = out_new
                        else:
                            blade_order=temp_list.copy()
            self.out_all_list.append(out)
            if len(self.rmb_value_list) >= self.len_list:
                break;
        #################################################

        
        if len(self.rmb_value_list)>0:
            d_store,count = {},0
            d_store['min_value'] = min(self.rmb_value_list)
            d_store['value']=self.rmb_value_list 
            for value in self.rmb_value_list:
                d_store['叶片_%s'%count] = self.rmb_blade_order_list[count]
                d_store['重量_%s'%count] = list(map(self.blade_weight,self.rmb_blade_order_list))[count]
                count += 1
            d_frame = pd.DataFrame(dict([ (k,Series(v)) for k,v in d_store.items() ]))
            #d_frame.to_excel('SA_tabu.xlsx',sheet_name='out',index=False)
            d_frame.to_excel('out.xlsx',sheet_name='out',index=False)
            plt.plot(self.out_all_list)
            plt.show()
            return print('程序结束.')
        else:
            return print('未得到符合要求的值，please try again...')

        

'''
        return self.rmb_value_list,self.rmb_blade_order_list,list(map(self.blade_weight,self.rmb_blade_order_list)),self.out_all_list
'''



print('程序开始运行.....')
time_start = time.time()
SA = SA_Tabu(L=L,t=0.0001,T=7000,each_T_internations=200,
                    T_descent_rate=0.99,threshold_value=0.1,
                    threshold_t=10,re_T=80,len_list=2)
#print('t起始温度 %s ,T终止温度 %s ,each_T_internations当前温度下的迭代次数 %s ,T_descent_rate温度下降率 %s ,threshold_value加入禁忌表阈值 %s ,threshold_t启动候选列表的温度阈值 %s ,re_T候选解的运行的温度 %s ,len_list程序终止条件(禁忌列表长度) %s .'%())
SA.run
'''
out_value_list,out_blade_list,out_blade_weight,out_all_list=SA.run
'''
time_cost = time.time()-time_start
print('程序运行时间: %s .'%time_cost)




            
