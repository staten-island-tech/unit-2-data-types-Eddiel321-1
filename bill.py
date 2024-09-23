bad=0
okay=15
good=20
great=25
bill=input("how much is the bill?")
print(bill)
input("how was the service")
values=(0,15,20,25)
print(values)
if bill ==0:
    print("bad")
if bill==15:
    print("okay")
if bill==20:
    print("good")
if bill==25:
    print("great")
input("how much would you like tip?")
print(values)
if bill == bad:
    print ("0% tip")
if bill == okay:
    input("15% tip")
if bill == good:
    input("20% tip")
if bill == great:
    input("25% tip")