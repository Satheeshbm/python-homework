from pathlib import Path
import csv
#csvpath = Path('../budget_data.csv')

records =[]
#row_count = 0


with open('Desktop/BC_Homeworks/python-homework/budget_data.csv','r') as csvfile :
    #csvreader = csv.reader(csvfile, delimiter=',')
    csvreader = csv.reader('Desktop/BC_Homeworks/python-homework/budget_data.csv', delimiter=',')
    csv_header = next(csvreader)
    csv_header.append("Diff")
    records.append(csv_header)
    cum_pl_t0 = 0
    cum_pl_t1 = 0
    ls_avg = []
    for index,row in csvreader:
        date = row[0]
        p_l = int(row[1])
        if row.index == 1:
            cum_pl_t0 = 0
            cum_pl_t1 = p_l
        else :
            cum_pl_t0 = cum_pl_t1
            cum_pl_t1 = cum_pl_t1 + p_l
        ls_avg.append(cum_pl_t1 - cum_pl_t0)
        
        print (index)