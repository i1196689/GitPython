import numpy as np
import math,random
from multiprocessing import Pool
import time


L_1=[17, 61, 56, 76, 25, 29, 31, 14, 69, 43, 45, 6, 13, 77, 10, 59, 87, 35, 28, 
    75, 49, 32, 71, 22, 55, 33, 39, 34, 66, 51, 58, 63, 46, 42, 74, 4, 50, 67, 19, 
    52, 47, 7, 48, 62, 88, 18, 20, 12, 70, 36, 57, 65, 60, 16, 78, 1, 8, 40, 11, 5, 
    21, 79, 26, 38, 2, 30, 41, 27, 73, 24, 15, 68, 9, 54, 37, 3, 72, 23, 64, 53, 80, 
    81, 82, 83, 84, 85, 86, 44, 89, 90]
L_2=[7030.876, 7045.008, 7042.67, 7013.952, 7005.039, 7000.265, 6977.76, 7026.464, 
    7019.712, 7008.911, 7014.578, 7008.819, 6985.234, 7032.678, 7033.846, 7025.744, 
    7030.426, 7023.945, 7039.792, 6998.287, 7026.915, 7012.42, 7006.389, 7009.089, 
    6978.931, 7004.408, 6986.583, 6960.113, 7004.407, 7023.044, 7033.307, 7010.888, 
    7055.365, 6997.567, 6994.324, 7014.221, 6991.534, 7013.498, 6991.534, 6960.836, 
    7019.803, 6984.513, 6994.054, 6987.752, 4286.629, 7059.055, 6958.043, 7014.403, 
    7008.82, 6994.235, 7004.318, 6993.331, 6982.262, 7007.92, 7026.374, 6993.963, 
    6966.238, 6995.046, 7014.762, 7000.537, 7022.234, 7001.798, 6989.373, 7006.75, 
    7039.788, 6978.03, 7008.725, 6977.852, 7017.552, 7013.409, 7000.357, 7023.13, 
    6983.163, 7032.137, 7011.251, 7043.929, 6992.794, 7027.546, 6990.904, 7007.92, 
    7041.139, 7054.287, 7042.403, 7076.069, 7054.826, 7067.064, 7080.123, 6992.345, 
    6958.493, 3690.793]



L=zip(L_1,L_2)
L=dict(L)

def ant_run(num_pop,num_iters,info_org,L):
    class ACA_TSP:
        def __init__(self, func, n_dim,
                    size_pop=10, max_iter=20,
                    distance_matrix=None,
                    alpha=1, beta=2, rho=0.1,
                    ):
            self.func = func
            self.n_dim = n_dim  # 城市数量
            self.size_pop = size_pop  # 蚂蚁数量
            self.max_iter = max_iter  # 迭代次数
            self.alpha = alpha  # 信息素重要程度
            self.beta = beta  # 适应度的重要程度
            self.rho = rho  # 信息素挥发速度

            self.prob_matrix_distance = 1 / (distance_matrix + 1e-10 * np.eye(n_dim, n_dim))  # 避免除零错误

            self.Tau = np.ones((n_dim, n_dim))  # 信息素矩阵，每次迭代都会更新
            self.Table = np.zeros((size_pop, n_dim)).astype(np.int)  # 某一代每个蚂蚁的爬行路径
            self.y = None  # 某一代每个蚂蚁的爬行总距离
            self.x_best_history, self.y_best_history = [], []  # 记录各代的最佳情况
            self.best_x, self.best_y = None, None

        def run(self, max_iter=None):
            self.max_iter = max_iter or self.max_iter
            for i in range(self.max_iter):  # 对每次迭代
                prob_matrix = (self.Tau ** self.alpha) * (self.prob_matrix_distance) ** self.beta  # 转移概率，无须归一化。
                for j in range(self.size_pop):  # 对每个蚂蚁
    
                    self.Table[j, 0] = random.randint(0,self.n_dim-1)  # start point，其实可以随机，但没什么区别
                    for k in range(self.n_dim - 1):  # 蚂蚁到达的每个节点
                        taboo_set = set(self.Table[j, :k + 1])  # 已经经过的点和当前点，不能再次经过
                        allow_list = list(set(range(self.n_dim)) - taboo_set)  # 在这些点中做选择
                        prob = prob_matrix[self.Table[j, k], allow_list]
                        prob = prob / prob.sum()  # 概率归一化
                        next_point = np.random.choice(allow_list, size=1, p=prob)[0]
                        self.Table[j, k + 1] = next_point

                # 计算距离
                y = np.array([self.func(i) for i in self.Table])

                # 顺便记录历史最好情况
                index_best = y.argmin()
                x_best, y_best = self.Table[index_best, :].copy(), y[index_best].copy()
                self.x_best_history.append(x_best)
                self.y_best_history.append(y_best)

                # 计算需要新涂抹的信息素
                delta_tau = np.zeros((self.n_dim, self.n_dim))
                for j in range(self.size_pop):  # 每个蚂蚁
                    for k in range(self.n_dim - 1):  # 每个节点
                        n1, n2 = self.Table[j, k], self.Table[j, k + 1]  # 蚂蚁从n1节点爬到n2节点
                        delta_tau[n1, n2] += 1 / y[j]  # 涂抹的信息素
                    n1, n2 = self.Table[j, self.n_dim - 1], self.Table[j, 0]  # 蚂蚁从最后一个节点爬回到第一个节点
                    delta_tau[n1, n2] += 1 / y[j]  # 涂抹信息素

                # 信息素飘散+信息素涂抹
                self.Tau = (1 - self.rho) * self.Tau + delta_tau

            best_generation = np.array(self.y_best_history).argmin()
            self.best_x = self.x_best_history[best_generation]
            self.best_y = self.y_best_history[best_generation]
            return self.best_x, self.best_y

        fit = run
    
    L=L
    num_points = len(L)
    sita=[i*2*math.pi/num_points for i in range(num_points)]


    num_pop,num_iters,info_org=num_pop,num_iters,info_org #参数设置


    def cal_total_distance(routine):
        routine_x,routine_y,count=0,0,0
        for each in routine:
            routine_x+=math.sin(sita[count])*L[each+1]
            routine_y+=math.cos(sita[count])*L[each+1]
            count+=1
        goal=routine_x**2+routine_y**2
        return goal**0.5

    distance_matrix=np.ones((num_points,num_points))*info_org-np.eye(num_points,num_points)*info_org

    aca = ACA_TSP(func=cal_total_distance, n_dim=num_points,
                size_pop=num_pop, max_iter=num_iters,
                distance_matrix=distance_matrix)########size_pop 为蚂蚁数量，max_iter为迭代次数



    best_x, best_y = aca.run()
    best_x=list(best_x)
    best_x.append(best_y)
    return best_x
def add_one(list_org):
    out=[i+1 for i in list_org]
    return out
def num_to_blade(list_org):
    out=[L[i] for i in list_org]
    return out
############################################     参数设置    ##################################################
num_pop,num_iters,info_org,interation=4000,1500 ,0.01,9
#######################   如上参数:   第一个为蚂蚁数量，第二个为迭代次数，第三个为信息素浓度，第四个为for循环次数     ######################################################################
time_start=time.time()
p_name=['p_%s'%i for i in range(interation)]
out_list,out_value=[],[]
if __name__=='__main__':
    p=Pool(9)
    for i in range(interation):
        p_name[i]=p.apply_async(ant_run,(num_pop,num_iters,info_org,L))
    print('>>>  程序开始运行.....')
    p.close()
    p.join()
    
    for j in range(interation):
        out_list.extend([p_name[j].get()])
        out_value.append(out_list[j][-1])
        out_list[j].pop(-1)
    out_list=list(map(add_one,out_list))
    time_cost=time.time()-time_start
    list_blade=list(map(num_to_blade,out_list))
    print('out_list:%s'%out_list)
    print('list_blade:%s'%list_blade)
    print('####################################################################################################################')
    print('>>>  运行时间: %s 分钟,蚂蚁数量: %s , 迭代次数: %s , 信息素浓度: %s ,for循环次数: %s .'%(time_cost/60,num_pop,num_iters,info_org,interation))
    print('out_value:%s'%out_value)
