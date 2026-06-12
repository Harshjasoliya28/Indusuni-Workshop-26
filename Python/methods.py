mylist1 = ["Harsh","Pythom"]
mylist2 = [88,99]

mylist1.sort()
print(mylist1)
mylist2.sort()  
print(mylist2)

mylist3 = [88,"Harsh",33.3,"Pythom",22]
mylist3.reverse()
print(mylist3)

print(sum(mylist2))

mycount = mylist3.count("Harsh")
print(mycount)

mylist3.append("Java")
print(mylist3)

mylist3.insert(2,"Django")
print(mylist3)  

position =mylist3.index("Pythom")
print(position)

mylist3.pop(3)
print(mylist3)

mylist3.remove(88)        
print(mylist3)

mylist3.clear()
print(mylist3)

mynewlist = mylist3.copy()
print(mynewlist)
mylist1.extend(mylist2)
print(mylist1)
