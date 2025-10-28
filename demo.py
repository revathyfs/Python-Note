def display(argument):
    return argument

class Bank():
    def __init__(self,abc):
        self.name="SBI TVM"
        self.balance=1000
        self.account_holer_name=abc
    def display_balance(self):
        print(self.balance)
 
class branch(Bank):
    def __init__(self,):
        super().__init__(self)
        print(self.balance)


 
class sub_branch(Bank):
    def __init__(self,):
        super().__init__(self)
        print(self.balance)
'''


-----------------------------------------------------------------------


'''

class Bank():
    def __init__(self,abc):
        self.name="SBI TVM"
        self.balance=1000
        self.account_holer_name=abc
    def display_balance(self):
        print(self.balance)

 
class State():
    def __init__(self,):
       print("gff")
 
class Multiple(Bank,State):
    def __init__(self,):
       print("gff")


'''


-----------------------------------------------------------------------


'''
class Bank():
    def __init__(self,abc):
        self.name="SBI TVM"
        self.balance=1000
        self.account_holer_name=abc
    def display_balance(self):
        print(self.balance)


class branch(Bank):
    def __init__(self,):
        super().__init__(self)
        print(self.balance)



#super() is used for calling parent
class Multilevel(branch):
    def __init__(self,):
        super().__init__(self)
        print(self.balance)



abc=branch()
abc.display_balance()




