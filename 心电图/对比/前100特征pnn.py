# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 13:21:13 2018

@author: lj
"""
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



def pro(s):
    path_train = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\五种类别\train\均值标准差\主要特征提取\90特征点\%s.xlsx'%(s)
    path_test = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\五种类别\test\主要特征\90特征点\%s.xlsx'%(s)
    data_train = import_excel_matrix(path_train)
    data_test = import_excel_matrix(path_test)
    return data_train,data_test


s = ['S','V','U','F','N']
label = [0,1,2,3,4]
data_test = []
data_train = []
label_train = []
label_test = []
for i in range(5):
    data_1,data_2 = pro(s[i])
    if len(data_1)>1000:
        data_train.extend(data_1[0:1000])
        tem = [label[i] for j in range(1000)]
        label_train.extend(tem)
    else:
        data_train.extend(data_1)
        tem = [label[i] for j in range(len(data_1))]
        label_train.extend(tem)

    # if len(data_2)>1000:
    #     data_test.extend(data_2[0:1000])
    #     tem = [label[i] for j in range(1000)]
    #     label_test.extend(tem)
    # else:
    #     data_test.extend(data_2)
    #     tem = [label[i] for j in range(len(data_2))]
    #     label_test.extend(tem)
    data_test.extend(data_2)
    tem = [label[i] for j in range(len(data_2))]
    label_test.extend(tem)

    
print(len(data_train),len(data_test),len(label_train),len(label_test))

data_train = np.matrix(data_train)
data_test = np.matrix(data_test)




def Normalization(data):
    '''样本数据归一化
    input:data(mat):样本特征矩阵
    output:Nor_feature(mat):归一化的样本特征矩阵
    '''
    m,n = np.shape(data)
    Nor_feature = copy.deepcopy(data) 
    sample_sum = np.sqrt(np.sum(np.square(data),axis = 1))   
    for i in range(n):
        Nor_feature[:,i] = Nor_feature[:,i] / sample_sum
        
    return Nor_feature

def distance(X,Y):
    '''计算两个样本之间的距离
    '''
    return np.sum(np.square(X-Y),axis = 1)

def distance_mat(Nor_trainX,Nor_testX):
    '''计算待测试样本与所有训练样本的欧式距离
    input:Nor_trainX(mat):归一化的训练样本
          Nor_testX(mat):归一化的测试样本
    output:Euclidean_D(mat):测试样本与训练样本的距离矩阵
    '''
    m,n = np.shape(Nor_trainX)
    p = np.shape(Nor_testX)[0]
    Euclidean_D = np.mat(np.zeros((p,m)))
    for i in range(p):
        for j in range(m):
            Euclidean_D[i,j] = distance(Nor_testX[i,:],Nor_trainX[j,:])[0,0]
    return Euclidean_D

def Gauss(Euclidean_D,sigma):
    '''测试样本与训练样本的距离矩阵对应的Gauss矩阵
    input:Euclidean_D(mat):测试样本与训练样本的距离矩阵
          sigma(float):Gauss函数的标准差
    output:Gauss(mat):Gauss矩阵
    '''
    m,n = np.shape(Euclidean_D)
    Gauss = np.mat(np.zeros((m,n)))
    for i in range(m):
        for j in range(n):
            Gauss[i,j] = math.exp(- Euclidean_D[i,j] / (2 * (sigma ** 2)))
    return Gauss

def Prob_mat(Gauss_mat,labelX):
    '''测试样本属于各类的概率和矩阵
    input:Gauss_mat(mat):Gauss矩阵
          labelX(list):训练样本的标签矩阵
    output:Prob_mat(mat):测试样本属于各类的概率矩阵
           label_class(list):类别种类列表
    '''
    ## 找出所有的标签类别
    #labelX[i].all() not in label_class
    label_class = []
    for i in range(len(labelX)):
        if labelX[i] not in label_class:            
            label_class.append(labelX[i])
    
    n_class = len(label_class)
    ## 求概率和矩阵
    p,m = np.shape(Gauss_mat)
    Prob = np.mat(np.zeros((p,n_class)))
    for i in range(p):
        for j in range(m):
            for s in range(n_class):
                if labelX[j] == label_class[s]:
                    Prob[i,s] += Gauss_mat[i,j]
    Prob_mat = copy.deepcopy(Prob)
    Prob_mat = Prob_mat / np.sum(Prob,axis = 1)
    return Prob_mat,label_class

def calss_results(Prob,label_class):
    '''分类结果
    input:Prob(mat):测试样本属于各类的概率矩阵
          label_class(list):类别种类列表
    output:results(list):测试样本分类结果
    '''
    arg_prob = np.argmax(Prob,axis = 1) ##类别指针
    results = []
    for i in range(len(arg_prob)):
        results.append(label_class[arg_prob[i,0]])
    return results
                    



# 1、导入数据
print ("--------- 1.load data ------------")
trainX, labelX = data_train,label_train


# 2、样本数据归一化
Nor_trainX = Normalization(trainX)
Nor_testX = Normalization(data_test) 
# 3、计算Gauss矩阵
Euclidean_D = distance_mat(Nor_trainX,Nor_testX)

def start_train(sigm=0.1):
    Gauss_mat = Gauss(Euclidean_D,sigm)
    Prob,label_class = Prob_mat(Gauss_mat,labelX)
    # 4、求测试样本的分类
    predict_results = calss_results(Prob,label_class)

    num = 0
    for c in range(len(Nor_testX)):
        if predict_results[c] == label_test[c]:
            num =num +1

    return num/len(Nor_testX)


# out = start_train(0.1)
# print(out)
    
rf_bo = BayesianOptimization(start_train,{'sigm':(0.01,1.5)})
rf_bo.maximize()
    
    
    
    
    
    
    
    
    
    
