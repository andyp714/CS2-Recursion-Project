'''
Created on Nov 10, 2021

@author: apauley24
'''
def main():
    pass
    n = int(input("WHat number"))
    print(factorial(n))




def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    
    return n * factorial(n-1)



if __name__ == "__main__":
    main()