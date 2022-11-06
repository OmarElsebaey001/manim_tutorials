#===================Class definition==============#
class Human:
    def __init__(self,aname,an_age):
        self.name = aname
        self.age = an_age*2 

    def speak(self):
        print("My Name is : ", self.name)

    def increase_age_by_ten(self):
        self.age = self.age + 10
    
###################################################



person1 = Human("John",25)
print("Name attribute is : ", person1.name)
print("My age is : ", person1.age)
person1.increase_age_by_ten()
print("My age is : ", person1.age)

