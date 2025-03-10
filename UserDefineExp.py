class CreateException(Exception):
    pass
def BillPayMent():
    billAmt=1000
    payMent=500
    if(payMent<1000):
        raise CreateException("You pay less amount of Bill .\n please pay as per Bill amt")
try:
    BillPayMent()
    print("Payment successful")
except CreateException as e:
    print("Bill payment Unsuccessful as:",e)
else:
    print("ding ding ding")