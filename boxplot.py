# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/ptdtan/.spyder2/.temp.py
"""
import numpy as np
from time import time
def boxplot(data):
    median = np.median(data)
    upper_quartile = np.percentile(data, 75)
    lower_quartile = np.percentile(data, 25)
    
    iqr = upper_quartile - lower_quartile
    upper_whisker = data[data<=upper_quartile+1.5*iqr].max()
    lower_whisker = data[data>=lower_quartile-1.5*iqr].min()
    outliers = np.concatenate((np.array(data[data>upper_whisker]),\
                    np.array(data[data<lower_whisker])), axis=0) 
    return [lower_whisker, lower_quartile, median, 
            upper_quartile,upper_whisker ], outliers

start = time()
data = np.loadtxt("Adipose.txt")
Tdata = data.transpose()
result = list(map(lambda x: boxplot(x), data))
print time()-start
print result[0]
print len(result)