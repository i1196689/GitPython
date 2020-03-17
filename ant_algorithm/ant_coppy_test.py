import numpy as np
from scipy import spatial
import pandas as pd
import matplotlib.pyplot as plt
import math


##################################################
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
num_points = len(L_1)
sita=[i*2*math.pi/num_points for i in range(num_points)]

def cal_total_distance(routine):
    routine_x,routine_y,count=0,0,0
    for each in routine:
        routine_x+=math.sin(sita[count])*L[each+1]
        routine_y+=math.cos(sita[count])*L[each+1]
        count+=1
    goal=routine_x**2+routine_y**2
    return goal**0.5

distance_matrix=np.ones((num_points,num_points))*0.5-np.eye(num_points,num_points)*0.5
##############################################

'''
def cal_total_distance(routine):
    num_points, = routine.shape
    return sum([distance_matrix[routine[i % num_points], routine[(i + 1) % num_points]] for i in range(num_points)])

'''
# %% Do ACA
from sko.ACA import ACA_TSP

aca = ACA_TSP(func=cal_total_distance, n_dim=num_points,
              size_pop=50, max_iter=200,
              distance_matrix=distance_matrix)########size_pop 为蚂蚁数量，max_iter为迭代次数

best_x, best_y = aca.run()

# %% Plot
print('best_x:%s'%best_x)
print('**************')
print('best_y:%s'%best_y)