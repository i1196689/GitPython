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

    def train(self, cases, labels, limit=10000, learn=0.05, correct=0.1,err=30):
        for j in range(limit):
            error = 0.0
            for i in range(len(cases)):
                label = labels[i]
                case = cases[i]
                error += self.back_propagate(case, label, learn, correct)
            if j%100 == 0:
                print('误差:',error)
            if error<err:
                break


    def strat_train(self,train_data,train_lab,test_data,test_lab,num_in,num_h,num_out,iter,lr,m,err):
        self.setup(num_in,num_h, num_out)
        self.train(train_data,train_lab, iter, lr, m,err)
        tem = []
        for case in test_data:
            out = self.predict(case)
            max_out = max(out)
            for i in range(len(out)):
                if out[i]<max_out:
                    out[i] = 0
                else:
                    out[i] = 1
            tem.append(out)
        num =0
        for i in range(len(test_lab)):
            if tem[i] == test_lab[i]:
                num = num+1
        print('正确率：',num/len(test_lab))


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



def pro(selcet):
    data_0= []
    data_1 = []
    if selcet == 0:
        path_0 = r'C:\Users\666\Desktop\mitdb\整理数据\训练数据集_mul.xlsx'
        data_0 = import_excel_matrix(path_0)
    if selcet == 1:    
        path_1 = r'C:\Users\666\Desktop\mitdb\整理数据\测试数据集_mul.xlsx'
        data_1 = import_excel_matrix(path_1)
    if selcet ==2:
        path_0 = r'C:\Users\666\Desktop\mitdb\整理数据\训练数据集_mul.xlsx'
        data_0 = import_excel_matrix(path_0)
        path_1 = r'C:\Users\666\Desktop\mitdb\整理数据\测试数据集_mul.xlsx'
        data_1 = import_excel_matrix(path_1)
    if len(data_0)>0:
        train_0 = []
        train_lab = []
        for num_0 in data_0:
            train_0.append(num_0[0:10])
            train_lab.append(num_0[11:16])
    if len(data_1)>0:
        test_0 = []
        test_lab = []
        for num_1 in data_1:
            test_0.append(num_1[0:10])
            test_lab.append(num_1[11:16])

    if selcet ==0:
        return train_0,train_lab
    if selcet ==1:
        return test_0,test_lab
    if selcet == 2:
        return train_0,train_lab,test_0,test_lab





train_data,train_lab,test_data,test_lab = pro(2)

print('数据处理结束，输入神经网络...')


nn = BPNeuralNetwork()
nn.strat_train(train_data[0:500],train_lab[0:500],train_data[500:1000],train_lab[500:1000],10,5,5,2500,0.1,0.1,0)