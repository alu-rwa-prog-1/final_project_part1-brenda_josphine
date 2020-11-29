# Authors: Brenda & Josephine

import unittest
from main_customer import *

## This are tests for the main customer class

class Customer_file(unittest.TestCase):
    def test_customer_name(self):#this will test the name entered by customer
        customer_name = Customer('Jane', 2547983456, 'Kenya')
        self.assertEqual(customer_name.customer_name, 'Jane')

    def test_customer_phone_number(self):#this is the test for phone number entered y customer
        customer_phone_number = Customer('Jane', 2547983456, 'Kenya')
        self.assertEqual(customer_phone_number.customer_phone_number, 2547983456)

    def test_customer_country(self):#this will test customer country
        customer_country = Customer('Queen', 254798555526, 'Kenya')
        self.assertEqual(customer_country.country, 'Kenya')

    def test_customer_name_notequal(self):#testing if the name entered doesn't already used by other customer
        customer_name = Customer('Jane', 2547983456, 'Kenya')
        self.assertNotEqual(customer_name.customer_name, 'Mary')

    def test_customer_phone_number_notequal(self):#testing if phone umer entered doesn't already used by other customer
        customer_phone_number = Customer('Jane', 2547983456, 'Kenya')
        self.assertNotEqual(customer_phone_number.customer_phone_number, 254798555526)

if __name__ == '__main__':
    unittest.main()

