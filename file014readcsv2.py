import csv

dates = []
scores = []

with open('data02.csv','r') as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    for row in reader:
        dates.append(row[0])
        scores.append(row[1])

print("dates: ", dates)
print("scores: ", scores)

