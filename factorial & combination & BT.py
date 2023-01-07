def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num-1))

def combination(n,m):
    temp=1
    for i in range(m):
        temp*=n
        n-=1
    for j in range(m):
        temp=temp/m
        m-=1
    return temp

def BT(a,b,n):
    temp=0
    for m in range(n+1):
        temp+=combination(n,m)*a**(n-m)*b**(m)
    return temp
