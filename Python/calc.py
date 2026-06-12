class calc:
    def __init__(self):
        n1 = int(input("Enter No1 :"))
        n2 = int(input("Enter No2 :"))
        self.n1 = n1
        self.n2 = n2
    def addition(self):
        result = self.n1 + self.n2
        print("Answer is :",result)
    def subtraction(self):
        result = self.n1 - self.n2
        print("Answer is :",result)
    def Multiplication(self):
        result = self.n1 * self.n2
        print("Answer is :",result)
    def Divison(self):
        result = self.n1 / self.n2
        print("Answer is :",result)


o1 = calc()
print("Enter youir choise +,-,*,/")
choise = input("Enetr choise ")

if choise == '+':
    o1.addition()
elif choise =='-':
    o1.subtraction()
elif choise == '*':
    o1.Multiplication()
elif choise =='/':
    o1.Divison()
        