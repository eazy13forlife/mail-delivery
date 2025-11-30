import csv

with open("CSV/Distances.csv") as csvfile:
    CSV_Distance = csv.reader(csvfile)
    CSV_Distance = list(CSV_Distance)




print(CSV_Distance);