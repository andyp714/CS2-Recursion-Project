'''
Created on Nov 12, 2021

@author: apauley24
'''

def main():
    a = int(input("what number"))
    b = int(input("what number"))
    if b >= 1:
        print(ProductNumber(a, b))
        
        
    

def ProductNumber(a,b):
    if b == 0:
        return 0
    
    return a + ProductNumber(a, b-1)
    
    



if __name__ == "__main__":
    main()