#===================Class Inheritance==============#
class Human:
    def __init__(self,name):
        self.name = name
    
    def speak_simple(self):
        print("\nSimply I am ", self.name,":)")

class Employee(Human):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary = salary
    
    def speak_professional(self):
        print(f"My Name is Mr.{self.name}")
        print("I am an employee with salary : ", self.salary )

employee1 = Employee("Mark",20000)
employee1.speak_professional()
employee1.speak_simple()