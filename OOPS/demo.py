
# class : blueprint,template

# object: realworld entity


# string representation of object

# __str__(self)=> object string representation

# __init_=>constructor attributes initilization

# (self=> current instance)
# super=> ( to access parent class method)

# inheritance
    # single
    # multilevel
    # multiple
# polymorphism

    # method_overloading
    # method_overriding

# Abstraction

    # essential aaaya karyngal mathram show cheyth avashyallathath hide cheyya



class Student:

    name:str
    roll:int
    age:int
    course:str

    def set_student(self,name,roll,age,course):

        self.name=name
        self.roll=roll
        self.age=age
        self.course=course

    def disply(self):

        print(self.name,self.age,self.roll,self.course)

    # reference_name=ClassName

student_instance1=Student()

student_instance1.set_student("gopika",25,101,"django")
student_instance1.disply()



# employee

# Student




