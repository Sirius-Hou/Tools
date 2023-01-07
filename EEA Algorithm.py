import math
x1=1
y1=0
x2=0
y2=1
r1=72 ## MANUAL INPUT REQUIRED
r2=49 ## MANUAL INPUT REQUIRED
a=r1
b=r2
q1=0
q2=0

r=1
q=1
x=1
y=1
n=3
print(x1,y1,r1,q1)
print(x2,y2,r2,q2)
while True:
    q=math.floor(r1/r2)
    r=r1-q*r2
    x=x1-q*x2
    y=y1-q*y2
    print(x,y,r,q)
    if (r==0):
        print("n: "+str(n))
        print("X0 = " + str(x2))
        print("Y0 = " + str(y2))
        print("gcd = " +str(r2))
        print("remainder = " +str(q2))
        print(str(a)+" * "+str(x2)+" + "+str(b)+" * "+str(y2)+" = "+str(r2))
        break
    else:
        n+=1
        x1=x2
        x2=x
        y1=y2
        y2=y
        r1=r2
        r2=r
        q1=q2
        q2=q
