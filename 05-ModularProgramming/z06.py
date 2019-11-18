import csv
import re

with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    n = 0
    for row in reader:
        if n == 0:
            print('#', row[0], row[1], row[2], row[3])
            print('===========================================')
            n+=1
        else:
            print(n, row[0], row[1], row[2], row[3])
            n+=1
            
    