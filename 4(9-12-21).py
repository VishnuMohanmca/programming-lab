print("area of rectangle")
l=int(input(" Enter the length:"))
b=int(input(" Enter the breadth:"))
c=lambda x,y: x*y
print("Area of rectangle:"+str(c(l,b)))
print("area of square")
s=int(input("side of square:"))
c=lambda x: x*x
print("Area of Square:"+str(c(s)))
print("area of triangle")
l=int(input("base:"))
b=int(input("height:"))
c=lambda x,y: .5*x*y
print("Area of triangle:"+str(c(l,b)))