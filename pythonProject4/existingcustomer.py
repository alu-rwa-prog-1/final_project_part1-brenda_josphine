# Authors Brenda & Josephine


from main_customer import *
# this is the class for existing customer

class Existing_customer(Customer):

    def __init__(self,customer_phone_number):
        super().__init__(customer_phone_number)

        self.customer_phone_number = self.customer_phone_number


