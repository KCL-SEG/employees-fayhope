"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self,name,wage,hours,monthly,contracts,commission):
        self.name = name
        self.wage = wage
        self.hours = hours
        self.monthly = monthly
        self.contracts = contracts
        self.commission = commission 

    def get_pay(self):
        if self.monthly:
            base = self.wage
        else:
            base = self.hours*self.wage
        total = base + (self.contracts*self.commission)
        return total
        

    def __str__(self):
        if self.monthly:
            base = self.wage
            phrase = "{} works on a monthly salary of {}".format(self.name, self.wage)
        else:
            base = self.hours * self.wage
            phrase = "{} works on a contract of {} hours at {}/hour".format(self.name, self.hours, self.wage)
        if self.contracts == 1:
            phrase += " and receives a bonus commission of {}".format(self.commission)
        elif self.contracts > 1:
            phrase += " and receives a commission for {} contract(s) at {}/contract".format(self.contracts, self.commission)
        self.total = base + (self.contracts * self.commission)
        phrase += ". Their total pay is {}.".format(self.total)
        return phrase

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000,0,True,0,0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',25,100,False,0,0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',3000,0,True,4,200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',25,150,False,3,220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',2000,0,True,1,1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',30,120,False,1,600)
