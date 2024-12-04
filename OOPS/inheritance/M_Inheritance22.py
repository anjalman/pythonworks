# class Person:
#     name:str

#     age:int

#     def __init__(self,name,age):

#         name=name

#         age=age

#     def display_person_info(self):

#         print(self.name,self.age)

# class Employee:

#     e_id:int
#     salary:int


#     def __init__(self,e_id,salary):

#         e_id=e_id
#         salary=salary

#     def employee_info(self):

#         print(self.e_id,self.salary)

# class Manager(Person,Employee):


#     department:str


#     def __init__(self,age,name,e_id,salary,department):

#         Person.__init__(self,name,age)
        
#         Employee.__init__(self,e_id,salary)

#         self.department=department

#     def display_manager_info(self):

#         self.display_person_info()

#         self.employee_info()

#         print(self.department)

# manager_instance=Manager("aniruth",28,709,55000,"Frontend developer")

# manager_instance.display_manager_info()

class Person:

    def _init_(self,name,age):

        self.name=name
        self.age=age

    def dispaly_person_info(self):

        print(self.name,self.age)

class Employee:

    def _init_(self,eid,salary):

        self.eid=eid
        self.sarary=salary

    def dispaly_employee_info(self):

        print(self.eid,self.sarary)

class Manager(Person,Employee):

    def __init__(self,name,age,eid,salary,department):

        Person._init_(self,name,age)
        Employee._init_(self,eid,salary)
        self.department=department

    def dispaly_manager_info(self):

        self.dispaly_person_info()

        self.dispaly_employee_info()

        print(self.department)

manager_instance1=Manager("vaishnav",29,"e2019",100000,"Developer")
manager_instance1.dispaly_manager_info()