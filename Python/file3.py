filename = input("Enter file name: ")
data = input("Enter data to add: ")

with open(filename, "a") as file:
    file.write(data + "\n")

print("Data added successfully!")

with open(filename, "r") as file:
    print("\nFile Content:")
    print(file.read())