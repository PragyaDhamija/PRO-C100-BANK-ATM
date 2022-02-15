class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def checkBalance(self):
        print("Your balance is 50000")

    def withdrawl(self,amount):
        newAmount = 50000 - amount
        print("You have withdrawn the amount "+str(amount) +" successfully. Your remaining balance is "+ str(newAmount))
    def deposit(self,amount):
        newAmount = 50000 + amount
        print("You have deposited the amount "+str(amount) +" successfully. Your account balance now is "+ str(newAmount))


def main():
    print("Welcome to ABC back. We are so happy to have you :)")
    cardNumber = input("Insert your ATM card number:- ")
    pinNumber  = input("Enter your pin number:- ")

    newUser =  Atm(cardNumber ,pinNumber)

    print("Choose your activity ")
    print("1. Balance Enquriy     2. Withdrawl     3. Deposit Cash")
    activity = int(input("Enter activity number :- "))

    if (activity == 1):
        newUser.checkBalance()
    elif (activity == 2):
        amount = int(input("Enter the amount to withdrawn:- "))
        newUser.withdrawl(amount)
    elif (activity == 3):
        amount = int(input("Enter the amount to be deposited:- "))
        newUser.deposit(amount)
    else:
        print("Please enter a valid number!!!")


if __name__ == "__main__":
    main()