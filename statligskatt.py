age = int(input("Ange �lder: "))
inkomst = int(input("Ange inkomst: "))

#funktion till skatt utr�kning 
def skatt(age, inkomst):
    if inkomst <= 540700: 
        return 0
    #om det �r mindre �n 540700 betalar man inte skatt
    
    elif inkomst > 554900 and age <= 64: 
        return ((inkomst -14200 -540700) *0.20)
     #om man inte fyllt 65 och har in inkomst p� 554900kr eller mer
     
    elif inkomst > 618700 and age >=65:
        return ((inkomst -78000 -540700) *0.20)
    #om man �r 65 eller �ldre och har en inkomst p� 618700 kr eller mer

#loop till fler skatt r�kning    
def repeat():
    while True:
     igen = input("Vill du g�ra en ny skatt ber�kning? ")
     if igen == "nej":
            break
     else:
         age = int(input("Ange �lder: "))
         inkomst = int(input("Ange inkomst: "))
         skatt(age, inkomst)
         print("Du betalar", skatt(age, inkomst), " kr i statlig skatt.")


print("Du betalar", skatt(age, inkomst), " kr i statlig skatt.")

#anropa repeat loop f�r att fr�ga om ny ber�kning
repeat()



 





