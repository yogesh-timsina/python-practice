class MyException(Exception):
    pass
def CheckBalance():
    money=5000
    withdraw=4500
    balance=money-withdraw
    if(balance<=1000):
        raise MyException("Insufficient balance you can't withdraw")
    print(balance)
try:
    CheckBalance()
except MyException as e:
    print("Exception occur:",e)
else:
    print("Withdrawal successfully")
finally:
    print("this is finally block which is always executed no matter what the condition occur.")