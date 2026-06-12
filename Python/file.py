myfile = open("harsh.txt", 'a')
myfile.write("Hello World !")
myfile.close()

myfile2 = open("harsh.txt", 'r')
content = myfile2.read()
print(content)
myfile2.close()