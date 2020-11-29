# Authors: Brenda & Josephine

from newcustomer import *
import mysql.connector
from mysql.connector.constants import ClientFlag
 #=======================================================#
user_data = mysql.connector.connect(host='localhost', user='root', passwd="", db='clientsdb',  client_flags=[ClientFlag.LOCAL_FILES])
user_choice = input("Are you: \n1.New_customer\n2.Existing_customer \n...")
        #print()

if user_choice == '1':# this will send the users to new customer registartion
                # new customer details
        name = input('What is your full name: ')
        phone_number = int(input('Input your phone number with country code: '))
        country = input("Input your country: ")
        new_user = New_customer(name, phone_number, country)

                # connect with database

        my_cursor = user_data.cursor()#this will help to insert client information to database



        my_cursor.execute("""
                INSERT INTO clients(name, phone_number, country)
                VALUES (%s, %s, %s)
                """, (new_user.customer_name, new_user.customer_phone_number, new_user.country))#new customer input in database

        user_data.commit()
        print('Data entered successfully.')
        user_data.close()

        if (user_data):
                user_data.close()
                print("\nThe connection is closed.")

        print('Registered successfully!')



elif user_choice == '2':#this will put the user on existing customer login

 # existing customer login
        my_cursor = user_data.cursor()

        phone_number = int(input('Input your phone number with country code: '))

        my_cursor.execute(
                "SELECT phone_number, COUNT(*) FROM clients WHERE phone_number = '%s' GROUP BY phone_number",
                    (phone_number)
                )
                # gets the number of rows affected by the command executed
        row_count = my_cursor.rowcount
        print("number of affected rows: {}".format(row_count))
        if row_count == 0:
                print("It Does Not Exist")

        print('Welcome once again!')






