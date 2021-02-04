def abc():
    a = 33
    b = 200
    UserName="USAMA"
# Tests for equality and inequality with strings
    if b == 200:
        print("b equal to 200")
    if a ==33:
        print("b equal to 200")    
    
    if b != 30:
        print("b is not equal to a")
    
    
    
    
    
    
    
       # Tests using the lower() function    
  
    if UserName.lower() == "usama":
        print("UserName is equal to usama")

    
    
    
    
    
    
    #Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to
    
    if a>=33:
        print('yes')
    if a==33:
        print('yes')
    if a>3: 
        print('yes')    
    if a<55:
        print('yes')     
        
        
        
    
#     Tests using the and keyword and the or keyword
    if a==33 and b==200:
        print('bes')
    if a==3 or b>100:
        print('yes')    
    
    
#  Test whether an item is in a list

    two_one=[1,2,3,4,5,6]
    list_two=two_one
    list_three=[22,44,5,67,7]
    if list_two is two_one:
        print('list_one is list_two')
    if list_two is not list_three:
        print('list_one is not list_two')
        
