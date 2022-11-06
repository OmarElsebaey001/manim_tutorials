#===================Class definition==============#
class Human:
    def __init__(self,aname,an_age):
        self.name = aname
        self.age = an_age*2 

    def speak(self):
        print("My Name is : ", self.name)
###################################################



person1 = Human("John",25)
print("Name attribute is : ", person1.name)

person2 = Human("Maria",24)
print("Name attribute is : ", person2.name)




person1.speak()

person2.speak()

