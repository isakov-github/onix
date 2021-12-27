# Isakov V.E.
# comments are superfluous cause of program output

my_list = [[1, 3, 3, 4], [2, 1, 3, 5], [4, 0, 1, 7], [5, 2, 1, 0], [0, 4, 8, 3]]
print("Initial list of lists")
print(my_list)

my_list.sort(key=lambda item: item[1])
print("List sorted by second item of inner lists")
print(my_list)

my_dict = { my_list[i][1] : my_list[i][:1] + my_list[i][2:] for i in range(0, len(my_list)) }
print("Dictionary, created form previous list. key = second item, value = everything else")
print(my_dict)

new_list = []
for key in my_dict.keys():
    my_dict[key].sort(reverse = True)
    new_list += my_dict[key]

print("Values of dictionary sorted in descending order")
print(my_dict)

my_set = set(new_list)
print("Set, created from values of dictionary")
print(my_set)

my_string = ""
for val in my_set:
    my_string += str(val)
print("Resulting string, created from the set")
print(my_string)
