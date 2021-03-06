'''
Created 10/12/2021
logan rocks :)     
'''


def main():

    options = """
    1 for factorial
    2 for summation
    3 for powers
    4 for sum of a number's digits
    5 for fibonacci
    6 for GCD euclids  algorithim
    7 for compound interest balance 
    8 for product of 2 whole numbers
    9 for square root newton's algorithm
    """
    function = ""
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
    '''
    This function is to find the factorial of inputted number
    :param: 
    :type name:
    :returns:
    :raises: 
    '''
    
    #Base Case
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
    #Times it with the number 1 less and runs it again until the base case is hit
        return n * factorial(n-1)
    
def summation(n):
    '''
    This function is to find the summation of inputted number
    :param: 
    :type name:
    :returns:
    :raises: 
    '''
    #Base Case
    if n == 0:
        return 0
    if n == 1:
        return 1
    #Adds it with the number 1 less and runs it again until the base case is hit
    return n + summation(n-1)

def power(a,n):
    '''
    This function is to find the result if you raise a to the power of n
    :param: 
    :type name:
    :returns:
    :raises: 
    '''
    #BaseCase
    if n == 0:
        return 1
    if n == 1:
        return a
    #Keeps timing a by itslef until it hits the base case
    return a * power(a,n-1)

def digitSum(n):
    '''
    This function is to find the sum of the digits
    :param: 
    :type name:
    :returns:
    :raises: 
    '''
    #Base case
    if n < 10:
        return n
    #Keeps dividing by 10 to find all digit and adding it by the ones
    return (digitSum(int(n/10)) + n % 10)

def fibonacci(n):
    '''
    This function is to find the fibonacci of a number
    :param: 
    :type name:
    :returns:
    :raises: 
    '''
    #Base Case
    if n == 0:
        return n
    
    elif n == 1:
        return n
    #Adds the fibonacci of the number minus 1 and the number minus 2
    elif n > 1:
        return fibonacci(n -1) + fibonacci(n -2)
 

def gcd(x, y):
    #Base Case
    if y <= x and x % y == 0:
        return y
    else:
        return gcd(y, x % y)

def compound_interest_recursive(principal, rate, time):
    '''
    This function is to calculate compound interest
    :param: 
    :type name:
    :returns:
    :raises: 
    '''
    #Base Case
    if time == 0:
        return principal
    else:
        #Multiplies the principle by the rate time times until time is 0
        return (1 + rate/100) * compound_interest_recursive(principal, rate, time -1)

def ProductNumber(a,b):
    '''
    This function is to find the product of two numbers
    :param: 
    :type name:
    :returns:
    :raises: 
    '''
    #Base Case
    if b == 0:
        return 0
    #Adds a + a b times until b is zero
    return a + ProductNumber(a, b-1)
    
def squareroot(n,p,e):
    '''
    This function is to find the square root of a number
    :param: 
    :type name:
    :returns:
    :raises: 
    '''
    #Base Case
    if abs(e * e - n) < p:
        return e 
    else:
        return squareroot(n,p,(e+n)/e)/2

if __name__ == "__main__":
    main()

