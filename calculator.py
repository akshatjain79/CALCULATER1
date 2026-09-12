#calculator 
# my first project
# 3 step to build calculator 
#1 function for operation
# user input
#3 pri

#function to addtwo number
def add(num1,num2):
    return num1 + num2

#unction to multiplytwo number
def multiply(num1,num2):
    return num1 * num2

# function to divide two number
def divide(num1,num2):
    return num1 / num2

# function to substract two number
def substract(num1,num2):
    return num1 - num2

# function to take average of two number
def average(num1,num2):
    return (num1 + num2) / 2
# step2; user input
print("please select an operator to perform the calculation:")
print("1. Add")
print("2. Multiply")
print("3. Divide")
print("4. Substract")
print("5. Average")

select =int(input("select a operation form 1,2,3,4,5:"))
num1 =int(input("enter first number:"))
num2 =int(input("enter second number:"))

# step 3 ; print the result
if (select == 1):
    print(num1, "+" , num2, "=",\
          add(num1,num2))

elif (select == 2):
    print(num1, "*" , num2, "=",\
          multiply(num1,num2))

elif (select == 3):
    print(num1, "/" , num2, "=",\
          divide(num1,num2))

elif (select == 4):
    print(num1, "-" , num2, "=",\
          substract(num1,num2))

elif (select == 5):
    print(num1, "+" , num2,")", "=","2","=",\
          substract(num1,num2))


else:
    print("invalid operation! pls select again")
   
    
    
    
    