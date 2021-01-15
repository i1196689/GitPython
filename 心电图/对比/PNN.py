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

path_train = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\train.xlsx'
path_test = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\test.xlsx'

path_trainlabel = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\train_lable_bp.xlsx'
path_testlabel = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\test_label_bp.xlsx'


data_train = import_excel_matrix(path_train)
data_trainlab = import_excel_matrix(path_trainlabel)
data_test = import_excel_matrix(path_test)
data_testlab = import_excel_matrix(path_testlabel)
#####################################################




data_train = np.matrix(data_train)
data_test = np.matrix(data_test)
data_train = data_train[0:3000,:]




data_trainlab = data_trainlab[0:3000]

#######离散化对数据预测有影响，数据长度对数据也有影响。

##############################################################################################################
#************************************************************************************************************
#####PCA###########################


# def t_pac(data):
#     data = [met[0:260] for met in data]
#     data = np.array(data)
#     pca = PCA(n_components=3)
#     data = pca.fit(data).transform(data)
#     data = list(data)
#     for j in range(len(data)):
#         data[j] = data[j].tolist()
#     return data

# data_train_0 = t_pac(data_train)
# data_test_0 = t_pac(data_test)


# for i in range(len(data_train_0)):
#     data_train_0[i].extend(data_train[i][0:260])

# for h in range(len(data_test_0)):
#     data_test_0[h].extend(data_test[h][0:260])

# data_train = data_train_0
# data_test = data_test_0


####离散化##############
# def data_prs(data):
#     T = np.linspace(-4,4,85)
#     for E_list in data:
#         for num in range(len(E_list)):
#             for i in range(len(T)):
#                 if E_list[num] >= T[i] and E_list[num] <T[i+1]:
#                     E_list[num] = T[i+1]
#                     break
#     return data

# data_train = data_prs(data_train)
# data_test = data_prs(data_test)

##################均值化####################

# def t_mean(data):
#     data = np.mat(data)
#     [m,n] = data.shape
#     for i in range(m):
#         s = np.mean(data[i,:])
#         if s > 0 :
#             data[i,:] = data[i,:] - s
#         else:
#             data[i,:] = data[i,:] + s

#     return data

# data_train = t_mean(data_train)

# data_test = t_mean(data_test)



#*********************************************************************************************************************
################################################################################################################









# def load_data(file_name):
#     '''导入数据
#     input:  file_name(string):文件的存储位置
#     output: feature_data(mat):特征
#             label_data(mat):标签
#             n_class(int):类别的个数
#     '''
#     # 1、获取特征
#     f = open(file_name)  # 打开文件
#     feature_data = []
#     label = []
#     for line in f.readlines():
#         feature_tmp = []
#         lines = line.strip().split("\t")
#         for i in range(len(lines) - 1):
#             feature_tmp.append(float(lines[i]))
#         label.append(int(lines[-1]))      
#         feature_data.append(feature_tmp)
#     f.close()  # 关闭文件
    
#     return np.mat(feature_data), label

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
                    
num_s = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

data_testlab = data_testlab[0:3000]
data_test = data_test[0:3000,:]
# 1、导入数据
print ("--------- 1.load data ------------")
trainX, labelX = data_train,data_trainlab


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
        if predict_results[c] == data_testlab[c]:
            num =num +1

    return num/len(Nor_testX)


out = start_train(0.1)
print(out)
    
# rf_bo = BayesianOptimization(start_train,{'sigm':(0,1)})
# rf_bo.maximize()
    
    
    
    
    
    
    
    
    
    
