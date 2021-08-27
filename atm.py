class Atm(object):
    def __init__(self,card,pin):
       self.card=card 
       self.pin=pin
    def cashWithdrawal(self):
        print("cash withdrawed")
    def  balanceEnquiry(self):
        print("balance enquired")
        
abc=Atm("abcxyz","efgh")
print(abc.cashWithdrawal())
print(abc.pin)