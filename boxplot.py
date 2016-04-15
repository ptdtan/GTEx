# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/ptdtan/.spyder2/.temp.py
"""
import numpy as np
import sys

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

if __name__ == "__main__":
	data = np.loadtxt(sys.argv[1])
	result = list(map(lambda x: boxplot(x), data))
	with open(sys.argv[2], "w") as fout:
		fout.write("\n".join([ ":".join([";".join(list(map(lambda x: str(x),arr[0]))), \
										";".join(list(map(lambda y: str(y), arr[1])))]) for arr in result]))
