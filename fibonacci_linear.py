def fibonacci_linear():
    n = int(input("Enter a positive number "))
    a = 0
    b = 1
    if n<0 :
        fibonacci_linear()
    print("\nThe fibonacci series is: ")
    if n==0:
        print(a)
    elif n==1:
        print(b)
    else:
        print("0\n1")
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
            print(b)
fibonacci_linear()