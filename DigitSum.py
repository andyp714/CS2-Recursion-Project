'''
 Created on Nov 10, 2021

 @author: apauley24
'''
 def main():
     pass
     n = int(input("what number"))
     print(digitSum(n))

 def digitSum(n):
     if n < 10:
         return n
     return (digitSum(int(n/10)) + n % 10)



 if __name__ == "__main__":
     main() 
