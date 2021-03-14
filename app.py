import csv
import pandas as pd

file1 = 'bright-stars.csv'
file2 = 'dwarf.csv'

dataSet1 = []
dataSet2 = []

with open(file1, 'r') as f:
    csvReader = csv.reader(f)

    for i in csvReader:
        dataSet1.append(i)

with open(file2, 'r') as d:
    csvReader = csv.reader(d)

    for i in csvReader:
        dataSet2.append(i)

header1 = dataSet1[0]
header2 = dataSet2[0]

data1 = dataSet1[1:]
data2 = dataSet2[1:]

headers = header1 + header2

data = []

for i in data1:
    data.append(i)
for j in data2:
    data.append(j)

with open('allStars.csv', 'w') as e:
    csvWriter = csv.writer(e)
    csvWriter.writerow(headers)
    csvWriter.writerows(data)

