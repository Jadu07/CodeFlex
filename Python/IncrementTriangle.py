def IncrementTriangle(n):
    if n < 1:
        print("The number must be greater than 0!")
    elif n > 1000:
        print("The number must be lesser than 1001!")
    else:
        for i in range(n,0,-1):
            for j in range(i,n+1):
                print(j, end = "")
            print()
try:
    n = int(input())
    IncrementTriangle(n)
except ValueError:
    print("The input must be an integer!")