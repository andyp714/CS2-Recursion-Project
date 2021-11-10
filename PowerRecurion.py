'''
Created on Nov 10, 2021

@author: apauley24
'''
def main():
    pass
    a = int(input("WHat base"))
    n = int(input("what power"))
    print(power(a,n))




def power(a,n):
    if n == 0:
        return 1
    if n == 1:
        return a
    
    return a * power(a,n-1)



if __name__ == "__main__":
    main()