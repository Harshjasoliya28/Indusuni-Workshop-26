mydic = {}
count = int(input("Enter the number of key:"))
for i in range(0, count):
    key = input("Enter key:")
    mydic[key]= input("Enter value:")
   
for i in mydic:
    print(f"Key is {i} Value is {mydic[i]}")
