import random,copy,math

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
L=zip(L_2,L_1)
L=dict(L)
num_ant=int(3*(len(L)/2))#蚂蚁数量(一般为叶片数量的1.5倍)
def create_ant(num_ant,meta_list): #初始化蚂蚁数量
    gather_list=[]
    for i in range(num_ant):
        random.shuffle(meta_list)
        tem=copy.deepcopy(meta_list)
        gather_list.extend([tem])
    return gather_list

def calculate(list_list,num_vane):#计算每个蚂蚁的路径
    sita=[i*(math.pi*2/num_vane) for i in range(num_vane)]
    def map_list(every_list):
        M_x,M_y=0,0
        for i in range(num_vane):
            M_x+=math.sin(sita[i])*every_list[i]
            M_y+=math.cos(sita[i])*every_list[i]
        return (M_x**2+M_y**2)**(1/2)
    goal_list=list(map(map_list,list_list))
    return goal_list

list_list=create_ant(5,L_2)

goal_list=calculate(list_list,70)


def choose(list_list,goal_list,num_ant_half):#选择蚂蚁数量的一半来确定第一个数
    org_dict=dict(zip(goal_list,list_list))
    org_list=sorted(org_dict.keys())
    arr_num_ant=org_list[:num_ant_half]
    dis_list=[]
    for key in arr_num_ant:
        dis_list.extend([org_dict[key]])
        
    return dis_list




arr=choose(list_list,goal_list,3)
for i in arr:
    print(i)
    print('----------')