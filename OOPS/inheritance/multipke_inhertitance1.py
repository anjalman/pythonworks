
class GrandParent:
    def m1(self):

        print("grandparent class m1 method")
    # def m(self):
    #             print("grandparent class m1 method")


class Parent:

    def m2(self):

        print("parent classs m2 method")
     # def m(self):

        # print("parent classs m2 method")

# error name ambiguty error[java] => inteface method use to solve this


class Child(Parent,GrandParent): #multiple inheritance 

    def m3(self):

        print("chlid class m3 method")

child_inheritance=Child()

child_inheritance.m3()

child_inheritance.m2()

child_inheritance.m1()