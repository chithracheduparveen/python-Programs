a=float(input('enter frist side:'))
b=float(input('enter second side:'))
c=float(input('enter third side:'))
#calculating the side of triangle
s=(a+b+c)/2
#calculate the area
area=(s*(s-a)*(s-b)*(s-c)**0.5)
print('the area of the triangle is %0.3f' %area)
