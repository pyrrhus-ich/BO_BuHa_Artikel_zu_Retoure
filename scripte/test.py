list1 = [1,2,3]
list2 = [3,4,5]

for el in list1:
    for val in list2:
        if el == val:
            print("TRUE " + str(el))

list4=[(1,2,3),(2,5,2),(3,9,4)]

for el in list1:
    for val in list4:
        if el == val[0]:
            print("Gefunden an Stelle")
