# Purpose: run a statistical test (mannwhitney u test)
# This script is to conduct a mannwhitney u test based on a dataset
# To run this script in Anaconda: python antcount.py --input_file=master.csv

import argparse
import numpy
import os
import pandas
import scipy
from pandas import DataFrame
from scipy.stats import mannwhitneyu

# Define the arguments send to the script
parser = argparse.ArgumentParser(description='Run MannWhitney U')
parser.add_argument('--input_file', action='store',dest='input_file',default='')
#parser.add_argument('--output_file', action='store',dest='output_file',default='')
args = parser.parse_args()

# Create a function to build data frame
def build_data_frame (CSVfile):
	data = pandas.read_csv(CSVfile)
	data_frame = pandas.DataFrame(data)
	return (data_frame)

# Create a function to run mannwhitney u
def run_mannwhitneyu (Data1, Data2):
    stat, p = mannwhitneyu(Data1, Data2, alternative='two-sided')
    return('Statistics=%.3f, p=%.3f' % (stat, p))

# Start the main program here
dataframe = build_data_frame(args.input_file)
print ('Running a Man Whitney U test...')

# Build a dataframe based on the categorical variable (for dividing the data into two groups) and the interval variable (the data to load in the stat test)
selected_dataframe_1 = dataframe[['Academic', 'ADJ', 'APP', 'NN', 'NOM', 'PPOF', 'PPOTHER']]

# Split the dataframe （the rows into two groups) to UG and GR
dataframe1_feature = selected_dataframe_1.loc[selected_dataframe_1['Academic'] == str('UG')]
dataframe2_feature = selected_dataframe_1.loc[selected_dataframe_1['Academic'] == str('GR')]
#print(dataframe1_feature, "\n", dataframe2_feature)

# Specify target features for comparision between UG and GR
# Pandas.series Vs. List 
# # add .values.tolist() which is a function from numpy to convert pandas.series (a column in dataframe with index) 
# # to a list of column data, this is different from pandas.series
# # see more: https://discuss.analyticsvidhya.com/t/what-is-the-difference-between-pandas-series-and-python-lists/27373)

dataframe1_adj = dataframe1_feature['ADJ'].values.tolist() 
dataframe2_adj = dataframe2_feature['ADJ'].values.tolist()

#print(type(dataframe1_adj))
#print(dataframe1_adj)

dataframe1_app = dataframe1_feature['APP'].values.tolist()
dataframe2_app = dataframe2_feature['APP'].values.tolist()
dataframe1_nn = dataframe1_feature['NN'].values.tolist()
dataframe2_nn = dataframe2_feature['NN'].values.tolist()
dataframe1_nom = dataframe1_feature['NOM'].values.tolist()
dataframe2_nom = dataframe2_feature['NOM'].values.tolist()
dataframe1_ppof = dataframe1_feature['PPOF'].values.tolist()
dataframe2_ppof = dataframe2_feature['PPOF'].values.tolist()
dataframe1_ppother = dataframe1_feature['PPOTHER'].values.tolist()
dataframe2_ppother = dataframe2_feature['PPOTHER'].values.tolist()


# Run the statisitcal tests to all the groups 
mannwhitneyu_results_adj = run_mannwhitneyu(dataframe1_adj, dataframe2_adj)
mannwhitneyu_results_app = run_mannwhitneyu(dataframe1_app, dataframe2_app)
mannwhitneyu_results_nn = run_mannwhitneyu(dataframe1_nn, dataframe2_nn)
mannwhitneyu_results_nom = run_mannwhitneyu(dataframe1_nom, dataframe2_nom)
mannwhitneyu_results_ppof = run_mannwhitneyu(dataframe1_ppof, dataframe2_ppof)
mannwhitneyu_results_ppother = run_mannwhitneyu(dataframe1_ppother, dataframe2_ppother)

# Present results 
print('ADJ: ', mannwhitneyu_results_adj)
print('APP: ', mannwhitneyu_results_app)
print('NN: ', mannwhitneyu_results_nn)
print('NOM: ', mannwhitneyu_results_nom)
print('PPOF: ', mannwhitneyu_results_ppof)
print('PPOTHER: ', mannwhitneyu_results_ppother)

# Specify target rhetorical functions for comparision between UG and GR

selected_dataframe_2 = dataframe[['Academic', 'M1', 'M1S1', 'M1S2', 'M2', 'M2S1', 'M2S2', 'M3', 'M3S1', 'M4']]
dataframe1_function = selected_dataframe_2.loc[selected_dataframe_2['Academic'] == str('UG')]
dataframe2_function = selected_dataframe_2.loc[selected_dataframe_2['Academic'] == str('GR')]

dataframe1_m1 = dataframe1_function['M1'].values.tolist()
dataframe2_m1 = dataframe2_function['M1'].values.tolist()
dataframe1_m1s1 = dataframe1_function['M1S1'].values.tolist()
dataframe2_m1s1 = dataframe2_function['M1S1'].values.tolist()
dataframe1_m1s2 = dataframe1_function['M1S2'].values.tolist()
dataframe2_m1s2 = dataframe2_function['M1S2'].values.tolist()
dataframe1_m2 = dataframe1_function['M2'].values.tolist()
dataframe2_m2 = dataframe2_function['M2'].values.tolist()
dataframe1_m2s1 = dataframe1_function['M2S1'].values.tolist()
dataframe2_m2s1 = dataframe2_function['M2S1'].values.tolist()
dataframe1_m2s2 = dataframe1_function['M2S2'].values.tolist()
dataframe2_m2s2 = dataframe2_function['M2S2'].values.tolist()
dataframe1_m3 = dataframe1_function['M3'].values.tolist()
dataframe2_m3 = dataframe2_function['M3'].values.tolist()
dataframe1_m3s1 = dataframe1_function['M3S1'].values.tolist()
dataframe2_m3s1 = dataframe2_function['M3S1'].values.tolist()
dataframe1_m4 = dataframe1_function['M4'].values.tolist()
dataframe2_m4= dataframe2_function['M4'].values.tolist()

# Run the statisitcal tests to all the groups 
mannwhitneyu_results_m1 = run_mannwhitneyu(dataframe1_m1, dataframe2_m1)
mannwhitneyu_results_m1s1 = run_mannwhitneyu(dataframe1_m1s1, dataframe2_m1s1)
mannwhitneyu_results_m1s2 = run_mannwhitneyu(dataframe1_m1s2, dataframe2_m1s2)
mannwhitneyu_results_m2 = run_mannwhitneyu(dataframe1_m2, dataframe2_m2)
mannwhitneyu_results_m2s1 = run_mannwhitneyu(dataframe1_m2s1, dataframe2_m2s1)
mannwhitneyu_results_m2s2 = run_mannwhitneyu(dataframe1_m2s2, dataframe2_m2s2)
mannwhitneyu_results_m3 = run_mannwhitneyu(dataframe1_m3, dataframe2_m3)
mannwhitneyu_results_m3s1 = run_mannwhitneyu(dataframe1_m3s1, dataframe2_m3s1)
mannwhitneyu_results_m4 = run_mannwhitneyu(dataframe1_m4, dataframe2_m4)

# Present results 
print('M1: ', mannwhitneyu_results_m1)
print('M1S1: ', mannwhitneyu_results_m1s1)
print('M1S2: ', mannwhitneyu_results_m1s2)
print('M2: ', mannwhitneyu_results_m2)
print('M2S1: ', mannwhitneyu_results_m2s1)
print('M2S2: ', mannwhitneyu_results_m2s2)
print('M3: ', mannwhitneyu_results_m3)
print('M3S1: ', mannwhitneyu_results_m3s1)
print('M4: ', mannwhitneyu_results_m4)

print ("Done...")
