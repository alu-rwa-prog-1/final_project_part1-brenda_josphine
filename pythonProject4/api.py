# Authors: Brenda & Josephine

#
from tkinter import *
import tkinter as tk
from tkinter import ttk
import datetime
from realtimeconverter import *
#this is the class for app interface or display screen
class App(Tk):

    def __init__(self , window):
        tk.Tk.__init__(self)

        currency_converter = RealTimeCurrencyConverter()
        self.currency_converter = currency_converter



        # Label
        self.intro_label = Label(window, text='WELCOME!', anchor="center", fg='blue', relief=tk.RAISED,
                                 borderwidth=5)
        self.intro_label.config(font=('Courier', 15, 'bold'))
        window.config(bg='blue')


        self.intro_label.place(x=10, y=5)


        # Entry box
        valid = (window.register(self.restrictNumberOnly), '%d', '%P')
        self.amount_field = Entry(window, bd=3, relief=tk.RIDGE, justify=tk.CENTER, validate='key', validatecommand=valid)
        self.converted_amount_field_label = Label(window, text='', fg='black', bg='white', relief=tk.RIDGE,
                                                  justify=tk.CENTER, width=17, borderwidth=3)

        # dropdown
        self.from_currency_variable = StringVar(window)
        self.from_currency_variable.set("USD")  # default value
        self.to_currency_variable = StringVar(window)
        self.to_currency_variable.set("RWF")  # default value

        font = ("Courier", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)

        print (type(currency_converter.response["rates"]))

        self.from_currency_dropdown = ttk.Combobox(window, textvariable=self.from_currency_variable,
                                                   values=list(currency_converter.response["rates"].values()), font=font,
                                                   state='readonly', width=12, justify=tk.CENTER)

        self.to_currency_dropdown = ttk.Combobox(window, textvariable=self.to_currency_variable,
                                                 values=list(currency_converter.response["rates"].values()), font=font,
                                                 state='readonly', width=12, justify=tk.CENTER)

        # placing
        self.from_currency_dropdown.place(x=30, y=120)
        self.amount_field.place(x=36, y=150)
        self.to_currency_dropdown.place(x=340, y=120)
        # self.converted_amount_field.place(x = 346, y = 150)
        self.converted_amount_field_label.place(x=346, y=150)

        # Convert button
        self.convert_button = Button(window, text="Convert", fg="black", command=self.perform)
        self.convert_button.config(font=('Courier', 10, 'bold'))
        self.convert_button.place(x=225, y=135)

    def perform(self):#this will do the conversion
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()

        converted_amount = self.currency_converter.response(from_curr, to_curr, amount)
        converted_amount = round(converted_amount, 2)#this will round the converted amount into two decimal places

        self.converted_amount_field_label.config(text=str(converted_amount))

    def restrictNumberOnly(self, action, string):#this will allow to input integer or float only
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return (string == "" or (string.count('.') <= 1 and result is not None))


if __name__ == '__main__':
    window = Tk()
    mywin = App(window)
    window.title('Currency ALU')
    window.geometry("400x300+10+10")
    window.mainloop()




