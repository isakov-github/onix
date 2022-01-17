# Isakov V.E.

import csv
import json


# generator
def mygen():
    for i in range(5, 91):
        yield i


my_dict = dict()


def f1(x):
    return x / (x + 100)


def f2(x):
    return 1 / x


def f3(x):
    return 20 * (f1(x) + f2(x)) / x


print("Create a dictionary with functions results")
print("f1(x) = x / (x + 100)")
print("f2(x) = 1 / x")
print("f3(x) = 20 * (f1(x) + f2(x)) / x")
print("\nx  -  [f1(x), f2(x), f3(x)]")

for x in mygen():
    my_dict[x] = [f1(x), f2(x), f3(x)]
    print(x, " - ", my_dict[x])

print("\nCreate a csv file and write into it ...")
with open('result.csv', 'w') as my_file:
    my_csv_writer = csv.writer(
        my_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    my_csv_writer.writerow(["x", "f1(x)", "f2(x)", "f3(x)"])
    for x in my_dict:
        my_csv_writer.writerow([x] + my_dict[x])
    print("Done")

print("\nRead data from csv file ...")
my_list = list()
with open('result.csv', 'r') as my_file:
    my_csv_reader = csv.reader(
        my_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in my_csv_reader:
        if(row):
            my_list.append(row)
for row in my_list:
    print(row)

print("\nWrite data into json file ...")
with open('result.json', 'w') as my_file:
    json.dump(my_list, my_file, indent=4)
print("Done")
