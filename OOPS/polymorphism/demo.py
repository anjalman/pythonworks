# polymorphism
# perform a single task (more than one way)
# THERE ARE TWO METHODS
# > method_overloading
# > method_overriding

# => method_overloading(same method name and different number of parameters)

# python is not support method_overloading because python use (*args) method

class Operation:

    def add(self,num1,num2):

        print(num1+num2)

    def add(self,num1,num2,num3):

        print(num1+num2+num3)

obj=Operation()

obj.add(10,20,30)

# obj.add(10,20) #error

# here only operate three parameter number of programs the 1st operation is not work



# METHOD_OVERRIDING(There are two classes and the inherite each others and method sighnature will be same eg:child inherit the parent class)

class Parent:


    def mobile(self):

        print("nokia")

class Child:

    def mobile(Self):

        print("iphone")

child_instance=Child()
child_instance.mobile()



