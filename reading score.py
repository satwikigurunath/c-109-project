from unittest import result
import pandas as pa
import csv
import statistics 

df = pa.read_csv("data 2.csv")
readinglist = df["reading score"].tolist();

#mean , median and mode for writing score
rMean = statistics.mean(readinglist)
rMode = statistics.mode(readinglist)
rMedian = statistics.median(readinglist)

print("Mean, Median and Mode of writing score is {}, {} and {} respectively".format(rMean,rMedian,rMode));

#Actual stdev for writing score colum
rstd = statistics.stdev(readinglist)

r_first_std_start = rMean - rstd
r_first_std_end = rMean + rstd

r_second_std_start = rMean - (2*rstd)
r_second_std_end = rMean + (2*rstd)

r_third_std_start = rMean - (2*rstd)
r_third_std_end = rMean + (2*rstd)

#percentage of data within 1, 2  and 3 standard Deviations for Weight
reading_score_list_of_data_first = [result for result in readinglist if result > r_first_std_start and result< r_first_std_end]
reading_score_list_of_data_second = [result for result in readinglist if result > r_second_std_start and result< r_second_std_end]
reading_score_list_of_data_third = [result for result in readinglist if result > r_third_std_start and result< r_third_std_end]

print("{}% of data for reading score lies within 1st standard deviation".format(len(reading_score_list_of_data_first)*100.0/len(readinglist)))
print("{}% of data for reading score lies within 2nd standard deviation".format(len(reading_score_list_of_data_second)*100.0/len(readinglist)))
print("{}% of data for reading score lies within 3rd standard deviation".format(len(reading_score_list_of_data_third)*100.0/len(readinglist)))