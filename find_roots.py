import math
def find_roots(a,b,c):
    discriminant=math.sqrt((b*b)-(4*a*c))
    x1=((-b)+discriminant)/(2*a)
    x2=((-b)-discriminant)/(2*a)
    return x1,x2


if __name__=="__main__":
    a=int(input("Enter a's value:"))
    b=int(input("Enter b's value:"))
    c=int(input("Enter c's value:"))
    print(find_roots(a,b,c))