def fibonacci(n):
    if n==0 or n==1: 
        return n
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
num = int(input("Enter a number between 0 and 30 "))
print("\n Fibonacci series upto", num, "are\n")
for i in range(0,num+1):
    print(fibonacci(i))