from unittest import result
import pandas as pa
import csv
import statistics 

df = pa.read_csv("data 2.csv")
mathlist = df["math score"].tolist();

#mean , median and mode for math score
mMean = statistics.mean(mathlist)
mMode = statistics.mode(mathlist)
mMedian = statistics.median(mathlist)

print("Mean, Median and Mode of math score is {}, {} and {} respectively".format(mMean,mMedian,mMode));

#Actual stdev for math score colum
mstd = statistics.stdev(mathlist)

m_first_std_start = mMean - mstd
m_first_std_end = mMean + mstd

m_second_std_start = mMean - (2*mstd)
m_second_std_end = mMean + (2*mstd)

m_third_std_start = mMean - (2*mstd)
m_third_std_end = mMean + (2*mstd)

#percentage of data within 1, 2  and 3 standard Deviations for Weight
math_score_list_of_data_first = [result for result in mathlist if result > m_first_std_start and result< m_first_std_end]
math_score_list_of_data_second = [result for result in mathlist if result > m_second_std_start and result< m_second_std_end]
math_score_list_of_data_third = [result for result in mathlist if result > m_third_std_start and result< m_third_std_end]

print("{}% of data for math score lies within 1st standard deviation".format(len(math_score_list_of_data_first)*100.0/len(mathlist)))
print("{}% of data for math score lies within 2nd standard deviation".format(len(math_score_list_of_data_second)*100.0/len(mathlist)))
print("{}% of data for math score lies within 3rd standard deviation".format(len(math_score_list_of_data_third)*100.0/len(mathlist)))