def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

print("Select Operation: -/n"
    "1:Addition"
    "2:Substarction"
    "3:Multiplication"
    "4:Division")


sel= int(input("select operation (1-4)"))

n1=int(input("Enter first Number:"))

n2=int(input("Enter Second Number: "))

if sel == 1:
    print(n1,"+",n2 "=",add(n1,n2))

elif sel == 2:
    print(n1,"-",n2 "=",sub(n1,n2))

elif sel == 3:
    print(n1,"*",n2 "=",mul(n1,n2))

elif sel== 4:
    print(n1,"/",n2 "=",div(n1,n2))

else:
    print("invalid Input")