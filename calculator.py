# python program to creat calculaor
#ther are 3 basic step to creat puthon file
#function for operat
# use input
#print resule
# function to add two function to add two numbers
def add(num1 ,num2):
    return num1+num2
#function to substract two number
def sub(num1 ,num2):
    return num1-num2
#function two multiply two number
def multiply(num1 ,num2):
    return num1*num2
#function two divide two number
def divide(num1 ,num2):
    return num1/num2
#function two take average of two number
def avg(num1 ,num2):
    return (num1+num2)/2

#step 2 to take user input
print("please select your operation")
print(" 1.additon")
print("2.substraction")
print("3.multiply")
print("4.divide")
print("5.average")


select=int(input("select an operation from 1,2,3,4,5:"))
num1=int(input("enter your first number"))
num2=int(input("enter your second number"))


# here the final move== RESULT
if(select==1):
    print(num1,"+",num2,"=", \
          add(num1,num2))
elif (select==2):
  print (num1,"-",num2,"=" , \
          sub(num1,num2))   
elif (select==3):
  print(num1,"*",num2,"=" , \
          multiply(num1,num2))
elif (select==4):
 print(num1,"/",num2,"=",  \
          divide(num1,num2))
elif (select==5):
         print(num1,"and",num2,"average is =" , \
          avg(num1,num2))
else:
 print("invalid input")



