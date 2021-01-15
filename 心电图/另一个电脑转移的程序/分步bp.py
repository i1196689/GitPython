import math
import random
import xlrd,xlsxwriter

random.seed(0)


def rand(a, b):
    return (b - a) * random.random() + a


def make_matrix(m, n, fill=0.0):
    mat = []
    for i in range(m):
        mat.append([fill] * n)
    return mat


def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


class BPNeuralNetwork:
    def __init__(self):
        self.input_n = 0
        self.hidden_n = 0
        self.output_n = 0
        self.input_cells = []
        self.hidden_cells = []
        self.output_cells = []
        self.input_weights = []
        self.output_weights = []
        self.input_correction = []
        self.output_correction = []

    def setup(self, ni, nh, no):
        self.input_n = ni + 1
        self.hidden_n = nh
        self.output_n = no
        # init cells
        self.input_cells = [1.0] * self.input_n
        self.hidden_cells = [1.0] * self.hidden_n
        self.output_cells = [1.0] * self.output_n
        # init weights
        self.input_weights = make_matrix(self.input_n, self.hidden_n)
        self.output_weights = make_matrix(self.hidden_n, self.output_n)
        # random activate
        for i in range(self.input_n):
            for h in range(self.hidden_n):
                self.input_weights[i][h] = rand(-0.2, 0.2)
        for h in range(self.hidden_n):
            for o in range(self.output_n):
                self.output_weights[h][o] = rand(-2.0, 2.0)
        # init correction matrix
        self.input_correction = make_matrix(self.input_n, self.hidden_n)
        self.output_correction = make_matrix(self.hidden_n, self.output_n)

    def predict(self, inputs):
        # activate input layer
        for i in range(self.input_n - 1):
            self.input_cells[i] = inputs[i]
        # activate hidden layer
        for j in range(self.hidden_n):
            total = 0.0
            for i in range(self.input_n):
                total += self.input_cells[i] * self.input_weights[i][j]
            self.hidden_cells[j] = sigmoid(total)
        # activate output layer
        for k in range(self.output_n):
            total = 0.0
            for j in range(self.hidden_n):
                total += self.hidden_cells[j] * self.output_weights[j][k]
            self.output_cells[k] = sigmoid(total)
        return self.output_cells[:]

    def back_propagate(self, case, label, learn, correct):
        # feed forward
        self.predict(case)
        # get output layer error
        output_deltas = [0.0] * self.output_n
        for o in range(self.output_n):
            error = label[o] - self.output_cells[o]
            output_deltas[o] = sigmoid_derivative(self.output_cells[o]) * error
        # get hidden layer error
        hidden_deltas = [0.0] * self.hidden_n
        for h in range(self.hidden_n):
            error = 0.0
            for o in range(self.output_n):
                error += output_deltas[o] * self.output_weights[h][o]
            hidden_deltas[h] = sigmoid_derivative(self.hidden_cells[h]) * error
        # update output weights
        for h in range(self.hidden_n):
            for o in range(self.output_n):
                change = output_deltas[o] * self.hidden_cells[h]
                self.output_weights[h][o] += learn * change + correct * self.output_correction[h][o]
                self.output_correction[h][o] = change
        # update input weights
        for i in range(self.input_n):
            for h in range(self.hidden_n):
                change = hidden_deltas[h] * self.input_cells[i]
                self.input_weights[i][h] += learn * change + correct * self.input_correction[i][h]
                self.input_correction[i][h] = change
        # get global error
        error = 0.0
        for o in range(len(label)):
            error += 0.5 * (label[o] - self.output_cells[o]) ** 2
        return error

    def train(self, cases, labels, limit=10000, learn=0.05, correct=0.1):
        for j in range(limit):
            error = 0.0
            for i in range(len(cases)):
                label = labels[i]
                case = cases[i]
                error += self.back_propagate(case, label, learn, correct)
            if j%100 == 0:
                print('误差:',error)

    def strat_train(self,train_data,train_lab,test_data,test_lab,num_in,num_h,num_out,iter,lr,m,butn):
        self.setup(num_in,num_h, num_out)
        self.train(train_data,train_lab, iter, lr, m)
        tem = []
        for case in test_data:
            out = self.predict(case)
            if butn ==1:
                max_out = max(out)
                for i in range(len(out)):
                    if out[i]<max_out:
                        out[i] = 0
                    else:
                        out[i] = 1
            tem.append(out)
        if butn == 1:
            num =0
            for i in range(len(test_lab)):
                if tem[i] == test_lab[i]:
                    num = num+1
            print('正确率：',num/len(test_lab))
        else:
            return tem


    # def test(self):
    #     cases = [
    #         [0, 0],
    #         [0, 1],
    #         [1, 0],
    #         [1, 1],
    #     ]
    #     labels = [[0], [1], [1], [0]]
    #     self.setup(2, 5, 1)
    #     self.train(cases, labels, 10000, 0.05, 0.1)
    #     for case in cases:
    #         print(self.predict(case))




def import_excel_matrix(path):
    table = xlrd.open_workbook(path).sheets()[0]  # 获取第一个sheet表
    row = table.nrows  # 行数
    data_matrix = []
    for i in range(row):  # 对列进行遍历
        data_matrix.append(table.row_values(i))
    return data_matrix


def save(data,path):
    f = xlsxwriter.Workbook(path)  # 创建工作簿
    sheet1 = f.add_worksheet('sheet1')  # 创建sheet
    l = len(data[0])
    h = len(data)  # h为行数，l为列数
    for i in range(h):
        for j in range(l):
            sheet1.write(i, j, data[i][j])
    f.close()







# nn = BPNeuralNetwork()
# nn.strat_train(train_data[0:500],train_lab[0:500],train_data[500:-1],train_lab[500:-1],10,10,4,800,0.1,0.1)



path_tn = r'C:\Users\666\Desktop\mitdb\整理数据\训练数据集_tn.xlsx'
path_tf = r'C:\Users\666\Desktop\mitdb\整理数据\训练数据集_tf.xlsx'
path_tv = r'C:\Users\666\Desktop\mitdb\整理数据\训练数据集_tv.xlsx'
path_tu = r'C:\Users\666\Desktop\mitdb\整理数据\训练数据集_tu.xlsx'

path_cn = r'C:\Users\666\Desktop\mitdb\整理数据\测试数据集_cn.xlsx'
path_cf = r'C:\Users\666\Desktop\mitdb\整理数据\测试数据集_cf.xlsx'
path_cv = r'C:\Users\666\Desktop\mitdb\整理数据\测试数据集_cv.xlsx'
path_cu = r'C:\Users\666\Desktop\mitdb\整理数据\测试数据集_cu.xlsx'

path_1 = r'C:\Users\666\Desktop\mitdb\整理数据\测试数据集_cls.xlsx'
data_cc = import_excel_matrix(path_1)
path_0 = r'C:\Users\666\Desktop\mitdb\整理数据\测试数据集_out.xlsx'

data_tn = import_excel_matrix(path_tn)
data_tf = import_excel_matrix(path_tf)
data_tv = import_excel_matrix(path_tv)
data_tu = import_excel_matrix(path_tu)


data_cn = import_excel_matrix(path_cn)
data_cf = import_excel_matrix(path_cf)
data_cv = import_excel_matrix(path_cv)
data_cu = import_excel_matrix(path_cu)



def intrain(train_n,train_f,train_v,train_u,num):
    train_tn = []
    lab_tn = []

    for i in range(num):
        if i < len(train_n):
            train_tn.append(train_n[i][0:10])
            lab_tn.append([1])
        if i < len(train_f):
            train_tn.append(train_f[i][0:10])
            lab_tn.append([0])
        if i < len(train_v):
            train_tn.append(train_v[i][0:10])
            lab_tn.append([0])
        if i < len(train_u):
            train_tn.append(train_u[i][0:10])
            lab_tn.append([0])
    return train_tn,lab_tn

num_t = len(data_tn)
num_c = len(data_cn)
# intrain_tn ,inlab_tn = intrain(data_tn,data_tf,data_tv,data_tu,num_t)
# intest_cn, inlab_cn = intrain(data_cn,data_cf,data_cv,data_cu,num_c)

intrain_tf ,inlab_tf = intrain(data_tf,data_tn,data_tv,data_tu,num_t)
intest_cf, inlab_cf = intrain(data_cf,data_cn,data_cv,data_cu,num_c)

# intrain_tf ,inlab_tf = intrain(data_tf,data_tn,data_tv,data_tu,num)
# intrain_tv ,inlab_tv = intrain(data_tv,data_tn,data_tf,data_tu,num)
# intrain_tu ,inlab_tu = intrain(data_tu,data_tn,data_tf,data_tv,num)

print('数据处理结束，输入神经网络...')


nn = BPNeuralNetwork()
tem_cn = nn.strat_train(intrain_tf[0:400],inlab_tf[0:400],intest_cf[0:400],inlab_cf[0:400],10,30,1,1000,0.1,0.1,1)


        
