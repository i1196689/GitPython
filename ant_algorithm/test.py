import copy,math,random
vane_weight=[58021.555, 58188.973, 58438.129, 58198.211, 58139.844, 58130.465, 58224.496, 58210.168, 
58008.453, 58201.094, 58151.91, 58088.086, 58245.402, 58153.391, 58309.773, 57871.414, 58140.707, 
57811.164, 58446.582, 58526.051, 58034.395, 58022.969, 58467.906, 57427.84, 58113.273, 58020.02, 
58064.785, 58328.859, 58158.246, 58165.406, 57683.879, 58033.598, 58147.195, 58269.109, 58137.215, 
58146.219, 58490.207, 58285.211, 58373.438, 57637.551, 58130.953, 58334.555, 58334.188, 58211.605, 
58104.137, 57979.859, 58101.453, 57959.086, 58108.949, 58065.789, 58145.563, 58012.012, 58358.555, 
58045.586, 58227.848, 57842.711, 58148.449, 58487.664, 58519.691, 57871.137, 58167.398, 58023.844, 
57908.699, 57956.043, 58291.84, 58421.148, 57879.496, 57877.262, 57843.551, 58268.633]


###常数设置：
info_arf=0.5
info_bta=0.5
info_ori=0.1
info_waste=0.5


def create_map(value):#生成所有路径
    vane_each=[value for i in range(70)]
    vane_tuple_list=list(zip(vane_each,vane_weight))
    return vane_tuple_list

vane_tuple_list=list(map(create_map,vane_weight))
for each_list in vane_tuple_list:
    for each_tuple in each_list:
        if each_tuple[0]==each_tuple[1]:
            each_list.remove(each_tuple)#去除重复路径
vane_len=len(vane_weight)
sita=[i*(2*math.pi/vane_len) for i in range(vane_len)]
vane_order=[i for i in range(vane_len)]
vane_order_sita=list(zip(sita,vane_order))
vane_road=[]
for each_list_addsita in vane_tuple_list:
    for each_tuple_addsita in each_list_addsita:
        for each_vane_order_sita in vane_order_sita:
            temp=copy.deepcopy(each_tuple_addsita)
            temp=temp+each_vane_order_sita
            vane_road.extend([temp])


def change_list(value):
    b=list(value)
    return b
vane_road=list(map(change_list,vane_road))
vane_info=info_ori#储存每只蚂蚁留下的信息素
for each_addlen in vane_road:
    value=copy.deepcopy(each_addlen)
    vane_dis=(value[0]*math.sin(value[2])+(value[1]*math.sin(value[2])))**2+(value[0]*math.cos(value[2])+(value[1]*math.cos(value[2])))**2
    vane_dis_reverse=1/(vane_dis**(1/2))
    each_addlen.append(vane_dis_reverse)
    each_addlen.append(vane_info)

def calculate(crl_list):#计算序列的值
    num_vane=len(crl_list)
    M_x,M_y=0,0
    sita=[i*((math.pi*2)/num_vane) for i in range(num_vane)]
    for i in range(num_vane):
        M_x+=math.sin(sita[i])*crl_list[i]
        M_y+=math.cos(sita[i])*crl_list[i]
    return (M_x**2+M_y**2)**(1/2)

def Rnd():
    rnd=random.random()
    return rnd

def start_run(m,n):#  m只蚂蚁迭代n轮
    for iters in range(n):
        for ant in range(m):
            road_wait=[]
            for road_count in range(vane_len):
                road_wait_plus=[]
                if road_count==0:
                    for each_road in vane_road:
                        if each_road[3]==0:
                            road_wait_plus.extend([each_road])
                    road_possible_all=0
                    for each_road_wait_plus in road_wait_plus:
                        road_possible_each=((each_road_wait_plus[5])**(info_bta))*(each_road_wait_plus[4]**(info_arf))
                        road_possible_all+=road_possible_each
                        each_road_wait_plus.append(road_possible_each)#6
                    poss_all=0
                    for each_poss in road_wait_plus:
                        each_poss[6]/=road_possible_all
                        poss_all+=each_poss[6]
                        each_poss[6]=poss_all
                    poss_num=-1
                    god_num=Rnd()
                    for each_poss_num in road_wait_plus:
                        if god_num<each_poss_num[6]:
                            poss_num+=1
                    road_wait.extend([road_wait_plus[poss_num]])
                    road_count+=1
                else:
                    road_distory=[]
                    for each_distroy in road_wait:
                        road_distory.extend(each_distroy)
                    for each_road_other in vane_road:
                        if each_road_other[3]==road_count:
                            if road_wait[road_count-1][1]==each_road_other[0] and (each_road_other[2] not in road_distory):
                                road_wait_plus.extend([each_road_other])
                    road_possible_all=0
                    for each_road_wait_plus_other in road_wait_plus:
                        road_possible_each=(((each_road_wait_plus_other[5]))**(info_bta))*(each_road_wait_plus_other[4]**(info_arf))
                        road_possible_all+=road_possible_each
                        each_road_wait_plus_other.append(road_possible_each)#6
                    poss_all=0
                    for each_poss_other in road_wait_plus:
                        each_poss_other[6]/=road_possible_all
                        poss_all+=each_poss_other[6]
                        each_poss_other[6]=poss_all
                    poss_num=-1
                    god_num=Rnd()
                    for each_poss_num_other in road_wait_plus:
                        if god_num<each_poss_num_other[6]:
                            poss_num+=1
                    road_wait.extend([road_wait_plus[poss_num]])
                    road_count+=1
            cover_road=[]
            for index in range(vane_len):
                if index==0:
                    cover_road.append(road_wait[index][0])
                else:
                    cover_road.append(road_wait[index][1])
            fin_value=calculate(cover_road)
            fin_value_reverse=1/fin_value
            for add_fin_value_reverse in road_wait:
                temp_list=add_fin_value_reverse[:6]
                if temp_list in vane_road:
                    list_index=vane_road.index(temp_list)
                    vane_road[list_index][5]+=fin_value_reverse
        for each_add_info in vane_road:
            each_add_info[5]=0.1*(info_waste**(iters+1))+each_add_info[5]-0.1*(info_waste**(iters))
    re_list=[]
    re_list.extend(cover_road)
    re_list.append(fin_value)
    return re_list

out_list=start_run(30,20)
print(out_list)
            

