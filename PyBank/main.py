#dependencies
import pandas as pd
import fnmatch
import os

#determine number of csv files to read


numFiles = (len(fnmatch.filter(os.listdir(), '*.csv')))

#create file names for csv

file_1 = "budget_data_1.csv"

file_2 = "budget_data_2.csv"

#import files
file_1_df = pd.read_csv(file_1)

file_2_df = pd.read_csv(file_2)

#print(file_2_df.head())

#count total months
totalMonths = file_1_df['Date'].count() + file_2_df['Date'].count()

#sum revenue
totalRevenue = file_1_df['Revenue'].sum() + file_2_df['Revenue'].sum()

##calc avg revenue change from month to month

#revChng=[]
#
#for index, row in file_1_df.iterrows():
#    if index == 0:
#        lastRev = row['Revenue']
#        #print(rev)
#    else:
#        revChng.append(row['Revenue'] - lastRev)
#        lastRev = row['Revenue']
#
#for index, row in file_2_df.iterrows():
#    if index == 0:
#        lastRev = row['Revenue']
#        #print(rev)
#    else:
#        revChng.append(row['Revenue'] - lastRev)
#        lastRev = row['Revenue']

#print(np.mean(revChng))
allDat_df = file_1_df.append(file_2_df, ignore_index=True)
avgRev = allDat_df['Revenue'].mean()

#get max rev 
if file_1_df['Revenue'].max() > file_2_df['Revenue'].max():
           
    maxRev = file_1_df['Revenue'].max()
else:
    maxRev = file_2_df['Revenue'].max()
    
#get min rev 
if file_1_df['Revenue'].min() > file_2_df['Revenue'].min():
           
    minRev = file_2_df['Revenue'].min()
else:
    minRev = file_1_df['Revenue'].min()   
    
#print message
print('Financial Analysis')
print('---------------------')
print('Total Months: ' + str(totalMonths))   
print('Total Revenue: ' + str(totalRevenue))   
print('Average Revenue Change: ' + str(avgRev))   
print('Greatest Increase in Revenue: ' + str(maxRev))   
print('Greatest Decrease in Revenue: ' + str(minRev))   
    
    










