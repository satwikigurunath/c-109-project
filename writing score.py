from unittest import result
import pandas as pa
import csv
import statistics 

df = pa.read_csv("data 2.csv")
writinglist = df["math score"].tolist();

#mean , median and mode for writing score
wMean = statistics.mean(writinglist)
wMode = statistics.mode(writinglist)
wMedian = statistics.median(writinglist)

print("Mean, Median and Mode of writing score is {}, {} and {} respectively".format(wMean,wMedian,wMode));

#Actual stdev for math score colum
wstd = statistics.stdev(writinglist)

w_first_std_start = wMean - wstd
w_first_std_end = wMean + wstd

w_second_std_start = wMean - (2*wstd)
w_second_std_end = wMean + (2*wstd)

w_third_std_start = wMean - (2*wstd)
w_third_std_end = wMean + (2*wstd)

#percentage of data within 1, 2  and 3 standard Deviations for Weight
writing_score_list_of_data_first = [result for result in writinglist if result > w_first_std_start and result< w_first_std_end]
writing_score_list_of_data_second = [result for result in writinglist if result > w_second_std_start and result< w_second_std_end]
writing_score_list_of_data_third = [result for result in writinglist if result > w_third_std_start and result< w_third_std_end]

print("{}% of data for eriting score lies within 1st standard deviation".format(len(writing_score_list_of_data_first)*100.0/len(writinglist)))
print("{}% of data for writing score lies within 2nd standard deviation".format(len(writing_score_list_of_data_second)*100.0/len(writinglist)))
print("{}% of data for writing score lies within 3rd standard deviation".format(len(writing_score_list_of_data_third)*100.0/len(writinglist)))