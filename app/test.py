import unittest

from app import app


class SignupTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_paymentSucess(self):

        paymentData = {
                        'CreditCardNumber': '1234561234561234',
                        'CardHolder': 'John De',
                        'ExpirationDate': '2025-05-17 00:00:00',
                        'SecurityCode': '123',
                        'Amount': 100000
                    }
        
        response =app.post('/args',paymentData)
                    
        assert response == 200


    def test_cardInvalid():
        
        paymentData = {
                        'CreditCardNumber': '1234561234561232',
                        'CardHolder': 'John De',
                        'ExpirationDate': '2025-05-17 00:00:00',
                        'SecurityCode': '123',
                        'Amount': 100000
                    }
        
        response =app.post('/args',paymentData)
                    
        assert response == 400

    def test_dateInvalid():
        
        
        paymentData = {
                        'CreditCardNumber': '1234561234561234',
                        'CardHolder': 'John De',
                        'ExpirationDate': '2020-05-17 00:00:00',
                        'SecurityCode': '123',
                        'Amount': 100000
                    }
        
        response =app.post('/args',paymentData)
                    
        assert response == 400


    def test_amountInvalid():
        
        paymentData = {
                        'CreditCardNumber': '1234561234561234',
                        'CardHolder': 'John De',
                        'ExpirationDate': '2025-05-17 00:00:00',
                        'SecurityCode': '123',
                        'Amount': -1
                    }
        
        response =app.post('/args',paymentData)
                    
        assert response == 400