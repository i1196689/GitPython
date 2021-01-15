#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import codecs
import pywt
import pywt.data
import csv,math,xlwt
import xlsxwriter

num_ter = 217

with open(r'C:\Users\666\Documents\MATLAB\MIT_HIT\10%s\10%s.csv'%(num_ter,num_ter),'r') as csvfile:
    reader = csv.reader(csvfile)
    y = [row[0]for row in reader] #读取第1列

ecg = [float(i) for i in y] #将字符串转化为数字



mode = pywt.Modes.smooth


def plot_signal_decomp(data, w, title):
  """Decompose and plot a signal S.
  S = An + Dn + Dn-1 + ... + D1
  """
  w = pywt.Wavelet(w)#选取小波函数
  a = data
  ca = []#近似分量
  cd = []#细节分量
  for i in range(5):
    (a, d) = pywt.dwt(a, w, mode)#进行5阶离散小波变换
    ca.append(a)
    cd.append(d)

  rec_a = []
  rec_d = []

  for i, coeff in enumerate(ca):
    coeff_list = [coeff, None] + [None] * i
    rec_a.append(pywt.waverec(coeff_list, w))#重构

  for i, coeff in enumerate(cd):
    coeff_list = [None, coeff] + [None] * i
    if i ==3:
      print(len(coeff))
      print(len(coeff_list))
    rec_d.append(pywt.waverec(coeff_list, w))

  # fig = plt.figure()
  # ax_main = fig.add_subplot(len(rec_a) + 1, 1, 1)
  # ax_main.set_title(title)
  # ax_main.plot(data)
  # ax_main.set_xlim(0, len(data) - 1)
  

  # for i, y in enumerate(rec_a):
  #   ax = fig.add_subplot(len(rec_a) + 1, 2, 3 + i * 2)
  #   ax.plot(y, 'r')
  #   ax.set_xlim(0, len(y) - 1)
  #   ax.set_ylabel("A%d" % (i + 1))

  # for i, y in enumerate(rec_d):
  #   ax = fig.add_subplot(len(rec_d) + 1, 2, 4 + i * 2)
  #   ax.plot(y, 'g')
  #   ax.set_xlim(0, len(y) - 1)
  #   ax.set_ylabel("D%d" % (i + 1))
  return rec_a[1]



def snr(org,now):
    org_sum = sum([i**2 for i in org])
    org_now = sum([(i-j)**2 for i,j in zip(org,now)])/len(org)
    out_snr = 10*math.log(org_sum/org_now,10)
    out_e = org_now**0.5
    return out_snr,out_e


new = plot_signal_decomp(ecg, 'sym5', "DWT: Ecg sample - Symmlets5")
s_num = [100,10000,100000]
for i in s_num:
  out_snr,out_e = snr(ecg[i:i+2000],new[i:i+2000])

  print(out_snr,out_e)



