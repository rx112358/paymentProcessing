import flask
from flask import request

import datetime
    
@app.route('/args', methods=['GET'])
def ProcessPayment():

    # Storing payment details from request
    
    paymentDetails=request.args.get()
    
    # Validating data
    
    validCardNo=validateCard(paymentDetails['CardNumber'])
    validDate=validateDate(paymentDetails['ExpirationDate'])
    
    if paymentDetails['Amount']>0:
        validAmt=True
        
    # Checking if data is valid
    
    if validCardNo and validDate and validAmt:
    
        paymentGateway(paymentDetails['Amount'])
        
        return 200
    
    else:
    
        # Invalid data
    
        return 400
        
    # in case of any errors
        
    return 500
    
def paymentGateway(amount):
    
    if amount<20:
        CheapPaymentGateway.process()
        
    elif amount>=21 and amount<=500:
    
        if ExpensivePaymentGateway.available:
            ExpensivePaymentGateway.process()
        else:
            CheapPaymentGateway.process()
            
    elif amount>500:
    
        if PremiumPaymentGateway.process()=="false" :
            
            for i in range(3):
                
                if PremiumPaymentGateway.process() :
                    return None
                
            
                
    

def validateCard(card_number):

    digits = str(card_number)

    digit_len=len(digits)

    if digit_len != 16:
        return 0

    double = 0
    total = 0

    for i in range(digit_len - 1, -1, -1):
        for c in str((double + 1) * int(digits[i])):
            total += int(c)
        double = (double + 1) % 2

    return (total % 10) == 0
    
    
def validateDate(exp_date):
    
    return exp_date != None and datetime.datetime.now() < exp_date