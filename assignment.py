my_list = []

elem = [10, 20, 30, 40]
my_list.extend(elem)
print(my_list)

my_list.insert(1, 15)
print(my_list)

another_lst = [50, 60, 70]
my_list.extend(another_lst)
print(my_list)

my_list.pop()
print(my_list)

my_list.sort()
print(my_list)

ind = my_list.index(30)
print(ind)
