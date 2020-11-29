# Authors: Brenda & Josephine

import unittest
from newcustomer import *


## This are tests for the new customer class.


class Customer_file(unittest.TestCase):
    def test_customer_name(self):#this will test the name entered by new customer
        customer_name = Customer('Mike', 2767983456, 'South Africa')
        self.assertEqual(customer_name.customer_name, 'Mike')

    def test_customer_phone_number(self):#this is the test for phone number entered by new customer
        customer_phone_number = Customer('Jane', 254702360119, 'Kenya')
        self.assertEqual(customer_phone_number.customer_phone_number, 254702360119)

    def test_customer_country(self):##this is the test the country entered by new customer
        customer_country = Customer('Awin', 233798555526, 'Ghana')
        self.assertEqual(customer_country.country, 'Ghana')

    def test_customer_name_notequal(self):#this will test if the name inputed by the user doesn't already used by other customer
        customer_name = Customer('Jane', 2547983456, 'Kenya')
        self.assertNotEqual(customer_name.customer_name, 'Mary')

    def test_customer_phone_number_notequal(self):##this will test if the phone_number inputed by the user doesn't already used by other customer
        customer_phone_number = Customer('Ivone', 2547983456, 'Kenya')
        self.assertNotEqual(customer_phone_number.customer_phone_number, 254798555526)


if __name__ == '__main__':
    unittest.main()

