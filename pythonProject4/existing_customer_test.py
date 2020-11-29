# Authors: Brenda & Josephine

import unittest
from existing_customer import *


## This are tests for the main customer class

class Customer_file(unittest.TestCase):
    def test_customer_phone_number(self):
        customer_phone_number = Customer('Jane', 2547983456, 'Kenya')
        self.assertEqual(customer_phone_number.customer_phone_number, 2547983456)


    def test_customer_phone_number_notequal(self):
        customer_phone_number = Customer('Jane', 234772001432, 'Nigeria')
        self.assertNotEqual(customer_phone_number.customer_phone_number, 234798555526)

    def test_customer_phone_number_equal(self):
        customer_phone_number = Customer('Jane', 2547983456, 'Kenya')
        self.assertEqual(customer_phone_number.customer_phone_number, 2547983456)


    def test_customer_phone_number_not_same(self):
        customer_phone_number = Customer('Jane', 255798345601, 'Uganda')
        self.assertNotEqual(customer_phone_number.customer_phone_number, 255798555526)

    def test_customer_phone_number_same(self):
        customer_phone_number = Customer('Jane', 2557983456, 'Tanzania')
        self.assertEqual(customer_phone_number.customer_phone_number, 2557983456)



if __name__ == '__main__':
    unittest.main()

