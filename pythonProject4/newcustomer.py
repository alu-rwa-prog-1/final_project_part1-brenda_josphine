# Authors Brenda & Josephine

from main_customer import *

class New_customer(Customer):

    def __init__(self, customer_name, customer_phone_number, country):
        super().__init__(customer_name, customer_phone_number,country)
        self.customer_name = customer_name
        self.customer_phone_number = customer_phone_number
        self.country = country

#this is the class for new customer to input their personal identification