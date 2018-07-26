##testa
#
#just learnt how to do a comments doc


countriesText = open("ListOfCurrencies.txt","r")

countrieslist = countriesText.read().splitlines()
n=1
currencyCode=[]
countryName=[]

while n<=69:
    #print(n)

    code,country = countrieslist.pop(1).split(":")
    currencyCode.append(code)
    countryName.append(country)

    if n==68:
        #print("loop broken")
        break

    n+=1

#YEET

#print(currencyCode)
#print(countryName)
#nowork

countryInput = str(input("enter country"))

if countryInput in countryName:
    print("true")
    position = countryName.index(countryInput)
    print(position)
    print("the corresponding currency for ",countryInput, "is: ",currencyCode[position])
    

