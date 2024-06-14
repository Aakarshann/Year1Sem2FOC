def fac(a):
    value=1
    for i in range(value, a+1):
        value*= i
    return value

a=int(input("Enter your number"))
facValue= fac(a)
print("Factorial is ", + facValue)