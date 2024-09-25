# 1. INT, FLOAT. The simple code that computes the discriminant using only int numbers.
print("Now we're going to calculate discriminant for a*x2+b*x+c=0")
a = int(input("Input variable a"))
b = int(input("Input variable b"))
c = int(input("Input variable c"))
D = b * b - 4*a*c
if D < 0:
    print ("No roots, D<0")
elif D == 0:
    x = -b/(2*a)
    print (x)
else:
    x1 = float((-b-D**0.5)/(2*a))
    x2 = float((-b+D**0.5)/(2*a))
    print (x1)
    print (x2)