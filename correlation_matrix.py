import argparse
import numpy
import os
import pandas
import scipy
from pandas import DataFrame
from scipy.stats import shapiro

# Define the arguments send to the script
parser = argparse.ArgumentParser(description='Run a correlation matrix')
parser.add_argument('--input_file', action='store',dest='input_file',default='')
#parser.add_argument('--output_file', action='store',dest='output_file',default='')
args = parser.parse_args()

# Create a function to build data frame
def build_data_frame (CSVfile):
	data = pandas.read_csv(CSVfile)
	data_frame = pandas.DataFrame(data)
	return (data_frame)

# Create a function to run a correlation matrix 
def run_corr_matrix (Dataframe):
    corr_matrix = Dataframe.corr(method='spearman') #specify specific type of correlation
    return(corr_matrix)

# Start the main program here
dataframe = build_data_frame(args.input_file)
selected_dataframe = dataframe[['ADJ', 'APP', 'NN', 'NOM', 'PPOF', 'PPOTHER', 'M1', 'M1S1', 'M1S2', 'M2', 'M2S1', 'M2S2', 'M3', 'M3S1', 'M4']]
#print(selected_dataframe)

print ('Running a correlation matrix...')
correlation_matrix = run_corr_matrix(selected_dataframe)
print(correlation_matrix)

print('Done.')
								