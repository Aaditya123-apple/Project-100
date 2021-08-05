class ATM ():
    def __init__(self, CardNumber, PIN):
        self.CardNumber=CardNumber
        self.PIN=PIN

    def Withdrawal(self, Amount):
        new_Amount=1000000 - Amount
        print('You have withdrawn:'+str(Amount))

    def BalanceEnquiry(self):
        print('You have 1 million dollars in your account')  

def main():
    CardNumber = input("insert your card number:- ")
    PIN  = input("enter your pin number:- ")

    new_user =  ATM(CardNumber ,PIN)

    print("Choose your activity ")
    print("1.BalanceEnquriy   2.withdrawl")
    activity = int(input("Enter activity number :- "))

    if (activity == 1):
        new_user.BalanceEnquiry()
    elif (activity == 2):
        amount = int(input("Enter the amount:- "))
        new_user.Withdrawal(amount)
    else:
        print("Enter a valid number")

main()