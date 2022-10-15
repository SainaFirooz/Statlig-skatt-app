age = int(input("Ange ålder: "))
inkomst = int(input("Ange inkomst: "))

#funktion till skatt uträkning 
def skatt(age, inkomst):
    if inkomst <= 540700: 
        return 0
    #om det är mindre än 540700 betalar man inte skatt
    
    elif inkomst > 554900 and age <= 64: 
        return ((inkomst -14200 -540700) *0.20)
     #om man inte fyllt 65 och har in inkomst på 554900kr eller mer
     
    elif inkomst > 618700 and age >=65:
        return ((inkomst -78000 -540700) *0.20)
    #om man är 65 eller äldre och har en inkomst på 618700 kr eller mer

#loop till fler skatt räkning    
def repeat():
    while True:
     igen = input("Vill du göra en ny skatt beräkning? ")
     if igen == "nej":
            break
     else:
         age = int(input("Ange ålder: "))
         inkomst = int(input("Ange inkomst: "))
         skatt(age, inkomst)
         print("Du betalar", skatt(age, inkomst), " kr i statlig skatt.")


print("Du betalar", skatt(age, inkomst), " kr i statlig skatt.")

#anropa repeat loop för att fråga om ny beräkning
repeat()



 





