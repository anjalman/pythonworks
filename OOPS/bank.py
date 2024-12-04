# CONSTUCTOR


class Bank:

    acc_no:int

    name:str

    balance:int

    acc__type:str

    mobile_no:int

    def __init__(self,acc_no,name,balance,acc_type,mobile_no):

        self.acc_no=acc_no
        self.name=name
        self.balance=balance
        self.acc__type=acc_type
        self.mobile_no=mobile_no

    def deposite(self,amount):

        self.balance+=amount

        print(f"your balance is{self.acc_no}has been creadited with amouont{amount}aval balance{self.balance}")

    def withdwar(self,amount):

        if self.balance<amount:

            self.balance-=amount

            print("insuffiecient balance")

        else:

            print(f"your balance is{self.acc_no} has been debited with amouont {amount} aval balance {self.balance}")

    def get_balance(self):


        print("your balance is",self.balance)

Bank_instance1=Bank(2025241200,"sharath",5000,"savings",9652457890)

Bank_instance1.withdwar(500)

