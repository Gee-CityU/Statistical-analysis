# Purpose: run a statistical test (one-way chisquare)
# This script is to conduct a mannwhitney u test based on a dataset
# To run this script in Anaconda: python antcount.py --input_file=master.csv

import argparse
import numpy
import os
import pandas
import scipy
from pandas import DataFrame
from scipy.stats import chisquare

# Define the arguments send to the script
parser = argparse.ArgumentParser(description='Run Chi-square Test')
parser.add_argument('--input_file', action='store',dest='input_file',default='')
#parser.add_argument('--output_file', action='store',dest='output_file',default='')
args = parser.parse_args()

# Create a function to build data frame
def build_data_frame (CSVfile):
	data = pandas.read_csv(CSVfile)
	data_frame = pandas.DataFrame(data)
	return (data_frame)

# Create a function to run mannwhitney u
def run_onewaychisq (Array):
    stat, p = chisquare(Array)
    return(stat, p)

# Start the main program here
dataframe = build_data_frame(args.input_file)
print ('Running a one-way Chi-square test...')

# Build a dataframe based on the categorical variable (for dividing the data into two groups) and the interval variable (the data to load in the stat test)
selected_dataframe = dataframe[['N_2000_2005', 'N_2006_2010', 'N_2011_2015', 'N_2016_2020']]

# Build an array of each element in a row, and redo this step for all the rows.
row_array = []
for rows in selected_dataframe.itertuples():
	array = [rows.N_2000_2005, rows.N_2006_2010, rows.N_2011_2015, rows.N_2016_2020]
	row_array.append(array)

# Print(data_array)

# Run the statisitcal tests to individual rows 
for item in row_array:
	chisq_result = run_onewaychisq(item)
	print ('chisq value and p value: ', round(chisq_result[0],3), round(chisq_result[1],3))
    #print('chisq, p value:', round(chisq_result[0],3), round(chisq_result[1],3))
    #print ('chisq value and p value: ', round (chisq_result[0], 3), round(chisq_result[1], 4))

print ("Done...")