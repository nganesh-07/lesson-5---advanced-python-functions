# zip with sets
list1 = {8, 9, 7}
list2 = {"z", "x", "y"}
list3 = list(zip(list1, list2))

print(list3)

# zip with lists
no1 = [0, 5, 10, 15, 20]
no2 = [3, 6, 9, 12, 15]

for x, y in zip(no1, no2[::-1]):
    print(x,y)

# zip in dictionary
events = ["mani-pedi", "flight booking", "grocery run"]
times = ["9:15", "12", "10:30"]

my_dict = {events: times for events,
           times in zip(events, times)}
print(my_dict)