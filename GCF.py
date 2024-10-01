""" a= int(input("Input a number"))
b=int(input("input another number"))
sigma=[]
def factors(a,b):
    for i in range(1, a+1):
        if a % i == 0 and b % i == 0:
            sigma(i)
            factors(a,b)
            print(sigma[1]) """
a= int(input("Input a number"))
b=int(input("input another number"))
for i in range(2,a+1):
    if a % i == 0 and b % i == 0:
        gcf= i
        print(gcf)