#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 17:15:25 2018
@author: rd
"""
from __future__ import division
import numpy as np
"""
This dataset is part of MNIST dataset,but there is only 3 classes,
classes = {0:'0',1:'1',2:'2'},and images are compressed to 14*14 
pixels and stored in a matrix with the corresponding label, at the 
end the shape of the data matrix is 
num_of_images x 14*14(pixels)+1(lable)
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


def class_lab(label):
    a = len(label[0])
    b = len(label)
    for i in range(b):
        for j in range(a):
            if label[i][j] == 1:
                label[i] = j
                break
    return label

data_train = np.array(data_train)
data_test = np.array(data_test)
data_train = data_train[0:3000,:]
data_test = data_test[0:1500,:]


data_trainlab = class_lab(data_trainlab)
data_testlab = class_lab(data_testlab)

data_trainlab = data_trainlab[0:3000]
data_testlab = data_testlab[0:1500]
print(data_train[0].shape)


'''
def load_data(split_ratio):
    tmp=np.load("data216x197.npy")
    data=tmp[:,:-1]
    label=tmp[:,-1]
    mean_data=np.mean(data,axis=0)
    train_data=data[int(split_ratio*data.shape[0]):]-mean_data
    train_label=label[int(split_ratio*data.shape[0]):]
    test_data=data[:int(split_ratio*data.shape[0])]-mean_data
    test_label=label[:int(split_ratio*data.shape[0])]
    return train_data,train_label,test_data,test_label
'''
"""compute the hingle loss without using vector operation,
While dealing with a huge dataset,this will have low efficiency
X's shape [n,14*14+1],Y's shape [n,],W's shape [num_class,14*14+1]"""
def lossAndGradNaive(X,Y,W,reg):
    dW=np.zeros(W.shape)
    loss = 0.0
    num_class=W.shape[0]
    num_X=X.shape[0]
    for i in range(num_X):
        scores=np.dot(W,X[i])        
        cur_scores=scores[int(Y[i])]
        for j in range(num_class):
            if j==Y[i]:
                continue
            margin=scores[j]-cur_scores+1
            if margin>0:
                loss+=margin
                dW[j,:]+=X[i]
                dW[int(Y[i]),:]-=X[i]
    loss/=num_X
    dW/=num_X
    loss+=reg*np.sum(W*W)
    dW+=2*reg*W
    return loss,dW

def lossAndGradVector(X,Y,W,reg):
    dW=np.zeros(W.shape)
    N=X.shape[0]
    Y_=X.dot(W.T)
    margin=Y_-Y_[range(N),Y.astype(int)].reshape([-1,1])+1.0
    margin[range(N),Y.astype(int)]=0.0
    margin=(margin>0)*margin
    loss=0.0
    loss+=np.sum(margin)/N
    loss+=reg*np.sum(W*W)
    """For one data,the X[Y[i]] has to be substracted several times"""
    countsX=(margin>0).astype(int)
    countsX[range(N),Y.astype(int)]=-np.sum(countsX,axis=1)
    dW+=np.dot(countsX.T,X)/N+2*reg*W
    return loss,dW

def predict(X,W):
    X=np.hstack([X, np.ones((X.shape[0], 1))])
    Y_=np.dot(X,W.T)
    Y_pre=np.argmax(Y_,axis=1)
    return Y_pre

def accuracy(X,Y,W):
    Y_pre=predict(X,W)
    acc=(Y_pre==Y).mean()
    return acc

def model(X,Y,alpha,steps,reg):
    X=np.hstack([X, np.ones((X.shape[0], 1))])
    W = np.random.randn(4,X.shape[1]) * 0.0001
    for step in range(steps):
        loss,grad=lossAndGradNaive(X,Y,W,reg)
        W-=alpha*grad
        print("The {} step, loss={}, accuracy={}".format(step,loss,accuracy(X[:,:-1],Y,W)))
    return W

#train_data,train_label,test_data,test_label=load_data(0.2)

W=model(data_train,data_trainlab,0.001,500,0.3)
print("Test accuracy of the model is {}".format(accuracy(data_test,data_testlab,W)))

