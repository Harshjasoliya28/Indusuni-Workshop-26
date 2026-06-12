#single inheritance
class MyCar:

    def MyCarMethod(self):
        print("This is My Car Class Method ")

class HJCar(MyCar):
    def HJCarMethod(self):
        print("This is HJ Car class method")
    def MyCarMethod(self):
        print("This is My Car Class child Method ")
    def mydata(self):
        super().MyCarMethod()

o1 = HJCar()
o1.MyCarMethod()
o1.mydata()