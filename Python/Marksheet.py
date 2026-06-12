sub1 = int(input("Enter Subject 1 Mark :"))
sub2 = int(input("Enter Subject 2 Mark :"))
sub3 = int(input("Enter Subject 3 Mark :"))
sub4 = int(input("Enter Subject 4 Mark :"))
sub5 = int(input("Enter Subject 5 Mark :"))

print("Subject 1 Mark is :",sub1)
print("Subject 2 Mark is :",sub2)
print("Subject 3 Mark is :",sub3)
print("Subject 4 Mark is :",sub4)
print("Subject 5 Mark is :",sub5)

total = sub1 + sub2 + sub3 + sub4 + sub5
per = (total/500)*100
print("Total Marks is :",total) 

print("Percentage is :",per)

if per >= 90:
    print("Grade is A+")
elif per >= 80:
    print("Grade is A")
elif per >= 70:
    print("Grade is B")
elif per >= 60:
    print("Grade is C")