from scipy import *  
from scipy.linalg import norm, pinv  
import numpy as np
   
from matplotlib import pyplot as plt  


import numpy as np
import math
import copy
from sklearn.decomposition import PCA





import pywt.data
import csv,math,xlwt
import xlsxwriter
import xlrd
import math

import xlrd,xlsxwriter
from bayes_opt import BayesianOptimization


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

path_train = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\整理数据\\short_train.xlsx'
path_test = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\整理数据\\short_test.xlsx'
# path_trainlab = r'C:\Users\666\Documents\MATLAB\MIT_HIT\整理数据\train_lab-f.xlsx'
# path_testlab = r'C:\Users\666\Documents\MATLAB\MIT_HIT\整理数据\test_lab-f.xlsx'



data_train = import_excel_matrix(path_train)

data_test = import_excel_matrix(path_test)


data_trainlab = [num[264:268] for num in data_train]
data_testlab = [num[264:268] for num in data_test]
data_train = [E_list[0:260] for E_list in data_train]
data_test = [E_list[0:260] for E_list in data_test]
data_train = np.matrix(data_train)
data_test = np.matrix(data_test)
data_train = data_train[0:3000,:]
data_test = data_test[0:1500,:]
# data_train = data_train.T
# data_test = data_test.T




def class_lab(label):
    a = len(label[0])
    b = len(label)
    for i in range(b):
        for j in range(a):
            if label[i][j] == 1:
                label[i] = j
                break
    return label

data_train = np.matrix(data_train)
data_test = np.matrix(data_test)
data_train = data_train[0:3000,:]
data_test = data_test[0:1500,:]


data_trainlab = class_lab(data_trainlab)
data_testlab = class_lab(data_testlab)

data_trainlab = data_trainlab[0:3000]
data_testlab = data_testlab[0:1500]
   
class RBF:  
       
    def __init__(self, indim, numCenters, outdim):  
        self.indim = indim  
        self.outdim = outdim  
        self.numCenters = numCenters  
        self.centers = [random.uniform(-1, 1, indim) for i in range(numCenters)]  
        self.beta = 8  
        self.W = random.random((self.numCenters, self.outdim))  
           
    def _basisfunc(self, c, d):
        [m,n] = d[0].shape
        e = []
        for i in range(n):
            e.append(d[0,i])
        d = e    
        assert len(d) == self.indim  
        return np.exp(-self.beta * norm(c-d)**2)  
       
    def _calcAct(self, X):  
        # calculate activations of RBFs  
        G = np.zeros((X.shape[0], self.numCenters), float)  
        for ci, c in enumerate(self.centers):  
            for xi, x in enumerate(X):  
                G[xi,ci] = self._basisfunc(c, x)  
        return G  
       
    def train(self, X, Y):  
        """ X: matrix of dimensions n x indim  
            y: column vector of dimension n x 1 """  
           
        # choose random center vectors from training set  
        rnd_idx = random.permutation(X.shape[0])[:self.numCenters]  
        self.centers = [X[i,:] for i in rnd_idx]  
           
        
        # calculate activations of RBFs  
        G = self._calcAct(X)  
         
           
        # calculate output weights (pseudoinverse)  
        self.W = np.dot(pinv(G), Y)  
           

    def test(self, X):  
        """ X: matrix of dimensions n x indim """  
           
        G = self._calcAct(X)  
        Y = np.dot(G, self.W)  
        return Y  

if __name__ == '__main__':  


       
    # rbf regression  
    rbf = RBF(260, 10, 1)  
    rbf.train(data_train, data_trainlab)  
    z = rbf.test(data_test)
    print(z[1400:1500])  
         
