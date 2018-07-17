#pyxchange.py
#this is the start of the pyxchange application file, currently for experimental purposes and getting the functionality done without the proper interface (16.7.18)

#import the forex API
from forex_python.converter import CurrencyRates

#name the CurrencyRates object for easy use
c = CurrencyRates()

#creating a useful function for giving codes the 'CODE' look for the thingo
def VarReady(CurrencyCode):
    cur=CurrencyCode.upper()
    newVar = ''+cur+''
    return newVar

#make a function that turns country names into currency codes here


#obtain the currencies from the user, the first being the currency the user wishes to exchange from and the second what is being exchanged to
currencyFrom = VarReady(str(input("enter your desired currency to exchange from here : ")))
currencyTo = VarReady(str(input("enter the currency you wish to exchange to here : ")))
amountToConvert = input("How much do you wish to convert? : ")

finalAmount = c.convert(currencyFrom,currencyTo,int(amountToConvert))

print(finalAmount)

