def gcd(num1, num2):
    a=1
    for i in range(1, max(num1, num2)+1):
        if num1%i==0 and num2%i==0:
            a=i
    return 
