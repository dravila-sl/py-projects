#Make a program that calculates initial and final concentrations and volumes for reactions

def regla3(w,z,y):
    x = w*z/y
    return x

value1 = input("Enter value to calculate: ")
if value1 == V2:
    c1 = input("Enter C1: ")
    v1 = input("Enter V1: ")
    c2 = input("Enter C2: ")
    v2 = regla3(c1,v1,c2)
    print("V2 is: ",v2)
elif value1 == C2:
    c1 = input("Enter C1: ")
    v1 = input("Enter V1: ")
    v2 = input("Enter V2: ")
    c2 = regla3(c1,v1,v2)
    print("C2 is: ",c2)
