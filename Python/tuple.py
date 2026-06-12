mylist =[]

count = int(input("Enter the number of elements:"))
for i in range(0, count):
    element = input("Enter element:")
    mylist.append(element)
print(mylist)

mytuple = tuple(mylist)
print(mytuple)