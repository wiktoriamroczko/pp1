import csv
import statistics

with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    n = 0
    tab = []
    for row in reader:
        if n == 0:
            print("%-3s %-9s %-13s %-3s %-9s" % ('#', row[0], row[1], row[2], row[3]))
            print('='*60)
            n+=1
        else:
            print("%-3s %-9s %-13s %-3s %-9s" % (n, row[0], row[1], row[2], row[3]))
            tab.append(int(row[2]))
            n+=1
    aryt = statistics.mean(tab)
    print(f'\n średnia arytmetyczna wieku pracowników: {aryt}')