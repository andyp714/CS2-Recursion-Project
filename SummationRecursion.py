'''
Created on Nov 10, 2021

@author: apauley24
'''
def main():
    pass
    n = int(input("WHat number do you want the summation of"))
    print(summation(n))




def summation(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return n + summation(n-1)



if __name__ == "__main__":
    main()