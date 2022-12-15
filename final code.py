  # -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 14:22:00 2022

,xla@author: shobi
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#function for reading the data from 2013 to 2018 for 5 countries.
def read(file):
    a=pd.read_excel(file)
    a=a.iloc[[16,26,48,79,178],[0,57,58,59,60,61,62]]
    a=a.set_axis(['Country','2013','2014','2015','2016','2017','2018'],axis=1,inplace=False)
    a.reset_index(drop=True, inplace=True)
    print(a)
    b=a.set_index('Country').T
    print(b)
    return a, b
#read the data using function.
data1,t_data1=read("C:\\Users\\shobi\\ADS Asgnmt\\Shobin\\infantdata.xls")
data3,t_data3=read("C:\\Users\\shobi\\ADS Asgnmt\\Shobin\\populationgrowth.xls")



#printing the statistical properties of the data.
print("\n Statistics values of data: \n")
c=t_data1.describe()
d=t_data3.describe()
print(c)
print(d)

#defining a function for plotting various graphs.

def plot_1(data_name,types,xlabel,ylabel,title):
    data_name.plot(kind=types)
    plt.xlabel=xlabel
    plt.ylabel=ylabel
    plt.title=title
    plt.show()
    
#plotting the Line graphs and Kernel density estimate function for the transposed datas.
         
plot_1(t_data1,"line","xlabel","ylabel","title")
plot_1(t_data3,"line","xlabel","ylabel","title")
plot_1(t_data1,"bar","xlabel","ylabel","title")
plot_1(t_data3,"bar","xlabel","ylabel","title")

#printing the correlation between various years of the above data.  
print(t_data1.corr())
print(t_data3.corr())

#defining a function for finding correlation between countries of given data.

def Correla(data18):
    s=data18.corr()
    return s

#printing the values of correlation of transposed data.
Correla(t_data1)
Correla(t_data3)