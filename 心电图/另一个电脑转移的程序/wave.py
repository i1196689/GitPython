#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

import pywt
import pywt.data
import csv,math

with open(r'C:\Users\666\Desktop\mitdb\100_new.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    y = [row[1]for row in reader] #读取第1列

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
  for i in range(8):
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


  return rec_a[1]



#plot_signal_decomp(data1, 'coif5', "DWT: Signal irregularity")
#plot_signal_decomp(data2, 'sym5',
#          "DWT: Frequency and phase change - Symmlets5")

def snr(org,now):
    org_sum = sum([i**2 for i in org])
    org_now = sum([(i-j)**2 for i,j in zip(org,now)])/len(org)
    out_snr = 10*math.log(org_sum/org_now,10)
    out_e = org_now**0.5
    return out_snr,out_e


new = plot_signal_decomp(ecg, 'sym5', "DWT: Ecg sample - Symmlets5")

out_snr,out_e = snr(ecg[0:2000],new[0:2000])
print(out_snr,out_e)

plt.show()

