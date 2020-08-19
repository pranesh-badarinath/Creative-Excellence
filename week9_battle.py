#!/usr/bin/env python
# coding: utf-8

# ###  logic implemented :-
# 
# #### Currency Converter in Python
# 
# ##### Steps to Build the Python Project on Currency Converter
#  1. Real-time Exchange rates
#  2. Import required Libraries
#  3. CurrencyConverter Class
#  4. UI for CurrencyConverter
#  5. Main Function
# 
# ###### 1. Real-time Exchange 
# 
# To get real-time exchange rates, we will use: https://api.exchangerate-api.com/v4/latest/USD
# 
# Here, we can see the data in JSON format, with the following details:
# 
# Base – USD: It means we have our base currency USD. which means to convert any currency we have to first convert it to USD then from USD, we will convert it in whichever currency we want.
# 
# Date and time: It shows the last updated date and time.
# 
# Rates: It is the exchange rate of currencies with base currency USD.
# 
# ###### 2. Import the libraries:
# 
# For this project based on Python, we are using the tkinter and requests library. So we need to import the library.
# 
# ###### 3. Create the CurrencyConverter class
# 
# Now we will create the CurrencyConverter class which will get the real time exchange rate and convert the currency and return the converted amount.
# 
#        a. create the constructor of class.
#           requests.get(url) load the page in our python program and then .json() will convert the page into the json file. We store it in a data variable.
#           
#        b. Convert() method:
#        This method takes following arguments: 
#        
#        From_currency: currency from which you want to convert.
#        
#        to _currency: currency in which you want to convert.
#        
#        Amount: how much amount you want to convert.
#        And returns the converted amount
#        
#        EXAMPLE:
#        
#        url = 'https://api.exchangerate-api.com/v4/latest/USD'
#        converter = CurrencyConverter(url)
#        print(converter.convert('INR','USD',100))
#        
#        OUTPUT: 1.33
#        100 Indian rupees = 1.33 US dollars
#        
# ###### 4. Now let’s create a UI for the currency converter
# 
# To Create UI we will create a class CurrencyConverterUI
# 
# Converter: Currency Converter object which we will use to convert currencies. 
# for class CurrencyConverterUI code will create a Frame.
# 
# Now let’s create the entry box for the amount and options of currency in the frame. So That users can enter the amount and choose among currencies.
# 
# Then, add the CONVERT button which will call the perform function.
# 
# Command = self.perform – It means on click it will call perform().
# 
# ###### perform() method:
# 
# The perform method will take the user input and convert the amount into the desired currency and display it on the converted_amount entry box.
# NOTE: This function is a part of App class.
# 
# ###### RestrictNumberOnly() method:
# 
# Now let’s create a restriction in our entry box. So that user can enter only a number in Amount Field.
# 
# NOTE: This function is a part of App class.
# 
# ###### 5. Let’s create the main function.
# 
# First, we will create the Converter. Second, Create the UI for Converter

# ### Solution :

# In[ ]:


#  Python Project on Currency Converter

# 2. Import the libraries:
import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk

# 3. CurrencyConverter class:

# # a.create the constructor of class.
class RealTimeCurrencyConverter():
    def __init__(self,url):
            self.data = requests.get(url).json()
            self.currencies = self.data['rates']
            
# # b. Convert() method:
    def convert(self, from_currency, to_currency, amount): 
        initial_amount = amount 
        #first convert it into USD if it is not in USD.
        # because our base currency is USD
        if from_currency != 'USD' : 
            amount = amount / self.currencies[from_currency] 
  
        # limiting the precision to 4 decimal places 
        amount = round(amount * self.currencies[to_currency], 4) 
        return amount

class App(tk.Tk):
# 4. UI for CurrencyConverter
    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title = 'Currency Converter'
        self.currency_converter = converter
        
# # Create the Converter
        self.geometry("500x200")
        
        # Label
        self.intro_label = Label(self, text = 'Welcome to Real Time Currency Convertor',  fg = 'blue', relief = tk.RAISED, borderwidth = 3)
        self.intro_label.config(font = ('Courier',15,'bold'))

        self.date_label = Label(self, text = f"1 Indian Rupee equals = {self.currency_converter.convert('INR','USD',1)} USD \n Date : {self.currency_converter.data['date']}", relief = tk.GROOVE, borderwidth = 5)

        self.intro_label.place(x = 10 , y = 5)
        self.date_label.place(x = 160, y= 50)

        # Entry box
        valid = (self.register(self.restrictNumberOnly), '%d', '%P')
        self.amount_field = Entry(self,bd = 3, relief = tk.RIDGE, justify = tk.CENTER,validate='key', validatecommand=valid)
        self.converted_amount_field_label = Label(self, text = '', fg = 'black', bg = 'white', relief = tk.RIDGE, justify = tk.CENTER, width = 17, borderwidth = 3)

        # dropdown
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("INR") # default value
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("USD") # default value

        font = ("Courier", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable,values=list(self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 12, justify = tk.CENTER)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable,values=list(self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 12, justify = tk.CENTER)

        # placing
        self.from_currency_dropdown.place(x = 30, y= 120)
        self.amount_field.place(x = 36, y = 150)
        self.to_currency_dropdown.place(x = 340, y= 120)
        #self.converted_amount_field.place(x = 346, y = 150)
        self.converted_amount_field_label.place(x = 346, y = 150)
        
        # Convert button
        self.convert_button = Button(self, text = "Convert", fg = "black", command = self.perform) 
        self.convert_button.config(font=('Courier', 10, 'bold'))
        self.convert_button.place(x = 225, y = 135)
# # perform() method:
    def perform(self):
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()

        converted_amount = self.currency_converter.convert(from_curr,to_curr,amount)
        converted_amount = round(converted_amount, 2)

        self.converted_amount_field_label.config(text = str(converted_amount))
# # RestrictNumberOnly() method:
    def restrictNumberOnly(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return (string == "" or (string.count('.') <= 1 and result is not None))
    
# 5. Main Function
if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = RealTimeCurrencyConverter(url)

    App(converter)
    mainloop()


    


# In[ ]:




