list = ['Apple' , 'guava' , 'Mango' , 'banana' , 'kiwi' ]

print("length of list:", len(list))
print("First element" , list[0])
print("Last element" , list[-1])

list.append('coconut')
print("updated list:" , list)

list.remove('guava')
print("updated List ;" , list)

list.sort()
print("sorted list" , list)

list.pop(1)
print("updated list is:" , list)

list.reverse()
print("reversed list is:" , list)

print("multiplication list is:" , list)

lst = list[:4]
print("sliced list:" , lst)

lst.clear()
print("updated list" , lst)