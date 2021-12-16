# Isakov V.E.

import csv
import json

# generator
def mygen():
    for i in range(5, 91):
        yield i

my_dict = dict()

for x in mygen():
    f1 = lambda x: x / (x + 100)
    f2 = lambda x: 1 / x
    f3 = lambda x: 20 * (f1(x) + f2(x))/x
    my_dict[x] = [f1(x), f2(x), f3(x)]
    #print(my_dict[x])

with open('result.csv', 'w') as my_file:
    my_csv_writer = csv.writer(my_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    my_csv_writer.writerow(["x", "f1(x)", "f2(x)", "f3(x)"])
    for x in my_dict:
        my_csv_writer.writerow([x] + my_dict[x])

my_list = list()
with open('result.csv', 'r') as my_file:
    my_csv_reader = csv.reader(my_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in my_csv_reader:
        if(row):
            my_list.append(row)

with open('result.json', 'w') as my_file:
    json.dump(my_list, my_file, indent=4)
