#Exploring Logical Operations and Precedence 6.1
a = 2
b = 5
c = 10
d= a+b*c
print ("a + b * c =")
print (d)
new = (a+b) * c
print ("(a+b)*c =")
print (new)
if d==new:
    print("match")
else: 
    print("does not match")