x= int(input("Input a number"))
for i in range(2, x + 1):
       if x % i == 0:
           factor=i
           print(factor)