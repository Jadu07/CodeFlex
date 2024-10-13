def is_prime(n):
    if n<2:
        return False
    if n==2:
        return True
    for i in range (2,int(n**0.5)+1):
        if(n%i==0):
            return False
    return True

num1 = int(input())
num2 = int(input())
if is_prime(num1) and is_prime(num2):
    print(num1+num2)
else:
    print("error")    
