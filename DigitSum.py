'''
Created 10/12/2021
main
Factorial
Summation

Powers

Sum of a number's digits

Fibonacci

Product of a number's digits

GCD EUCLIDS  ALGORITHIM

Compound Interest Balance 

Product of 2 whole numbers

Square Root Newton's algorithm

     
    
'''


function = ()
def main():
    pass
    options = """
    1 for factorial
    2 for summation
    3 for powers
    4 for sum of a number's digits
    5 for fibonacci
    6 for GCD EUCLIDS  ALGORITHIM
    7 for compound interest balance 
    8 for product of 2 whole numbers
    9 for square root newton's algorithm
    """
    print(options)
    userinput =  input("please a chose a number from the menu above")
    if userinput == "1":
        n = int(input("enter number"))
        function = factorial(n)
    elif userinput == "2":
        n = int(input("Wwat number do you want the summation of"))
        function = summation(n)
    elif userinput == "3":
        a = int(input("what base"))
        n = int(input("what power"))
        function = power(a,n)
    elif userinput == "4":
        n = int(input("what number"))
        function = digitSum(n)
    elif userinput == "5":
        n = int(input("what number"))
        function = fibonacci(n)
    elif userinput == "6":
        y= int(input("what number"))
        x= int(input("what number"))
        function = gcd(x, y)
    elif userinput == "7":
        time = int(input("what number"))
        rate = int(input("what number"))
        principal = int(input("what number"))
        function = compound_interest_recursive(principal, rate, time)
    elif userinput == "8":
        a = int(input("what number"))
        b = int(input("what number"))
        functions = ProductNumber(a, b)
    elif userinput == "9":
        n= int(input("what number"))
        p= int(input("what number"))
        e= int(input("what number"))
        function = squareroot(n,p,e)
    else:
        print("try again")
        
    print(function)
    
def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
def summation(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return n + summation(n-1)

def power(a,n):
    if n == 0:
        return 1
    if n == 1:
        return a
    
    return a * power(a,n-1)

def digitSum(n):
    if n < 10:
        return n
    return (digitSum(int(n/10)) + n % 10)

def fibonacci(n):
    if n == 0:
        return n
    
    elif n == 1:
        return n
 
    elif n > 1:
        return fibonacci(n -1) + fibonacci(n -2)
 

def gcd(x, y):
    if y <= x and x % y == 0:
        return y
    else:
        return gcd(y, x % y)

def compound_interest_recursive(principal, rate, time):
    if time == 0:
        return principal
    else:
        return (1 + rate/100) * compound_interest_recursive(principal, rate, time -1)

def ProductNumber(a,b):
    if b == 0:
        return 0
    
    else:
        return a + ProductNumber(a, b-1)
    
def squareroot(n,p,e):
    if abs(e * e - n) < p:
        return e 
    else:
        return squareroot(n,p,(e+n)/e)/2

if __name__ == "__main__":
    main()

