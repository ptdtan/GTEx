from __future__ import division
import sys
import numpy as np

#1st argument == file mapping sample:gender
gender_mapping = {}
for line in open(sys.argv[1]):
	person, gender = line.strip().split()
	gender_mapping[person] = gender
#2st argument == samples of tissue

samples = open(sys.argv[2]).read().strip().split("\n")

male_indices, female_indices = [], []
map(lambda x: male_indices.append(x), [samples.index(x) for x in samples if gender_mapping[x] == "1"])
map(lambda x: female_indices.append(x), [samples.index(x) for x in  samples if gender_mapping[x] == "2"])
#4th argument is tissue matrix

matrix = np.loadtxt(sys.argv[3])
Tmatrix = matrix.transpose()
male_df, female_df = [], []

map(lambda y: male_df.append(Tmatrix[y]), male_indices)
map(lambda y: female_df.append(Tmatrix[y]), female_indices)
np.savetxt(sys.argv[3]+".male", np.array(male_df).transpose(), delimiter="\t")
np.savetxt(sys.argv[3]+".female", np.array(female_df).transpose(), delimiter="\t")
