balance = 10000;
print("1.check balance")
print("2.withdraw")
print("3.deposit")  

choice = int(input("Enter your choice :"))  
if choice == 1:
    print("Your balance is :",balance)  
elif choice == 2:
    amount = int(input("Enter amount to withdraw :"))
    
    balance = balance - amount
    print("Your new balance is :",balance)
elif choice == 3:
    amount = int(input("Enter amount to deposit :"))
    balance = balance + amount
    print("Your new balance is :",balance)