
class Employee:

    emp_id:int
    
    name:str

    age:int 

    department:str

    salary:int

    def set_employee(self,emp_id,name,age,department,salary):

        self.emp_id=emp_id

        self.name=name

        self.age=age

        self.department=department

        self.salary=salary

    def display(self):

        print(self.emp_id,self.name,self.age,self.department,self.salary)

employee_instance1=Employee()

employee_instance2=Employee()

employee_instance3=Employee()

employee_instance4=Employee()


employee_instance1.set_employee("ashwin",1001,22,"mech",25000)

employee_instance2.set_employee("parvathi",1002,22,"EEE",22000)

employee_instance3.set_employee("alen",1001,22,"BTCS",28000)

employee_instance4.set_employee("ajil",1001,22,"AUTOMB",55000)


employee_instance1.display()

employee_instance2.display()
employee_instance3.display()
employee_instance4.display()


