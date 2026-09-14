class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def __repr__(self):
        return f"Student(name={self.name}, age={self.age})"
    def add_student(self, name, age):
        self.name = name
        self.age = age
        
    def get_Student(self):
       print(f"Name: {self.name}\nAge: {self.age}") 
      
    
Gheo = Student(None, None)


Gheo.add_student("John", 20)
Gheo.get_Student()   
 
 
      
        