#Primitive data types:String,Integers,Boolean and float
#subscripting
print("Hello"[0])
print("Hello"[-1])
print(222_222_900)#integer#we can use _ instead of comma for our simplification
print(34.29)#float
print(False,True)#boolean

#Type error---->len(any integer)
print(type(23))
print(len(str(8900)))
#Type conversion/Typecasting
print(int("123")+int("234"))
#valueerror---->int("abc")
#Typeerror::print("Number of characters in your name is:"+len(input("Enter tour name::")))You have to typecast the 2nd part to string.

#+++++Mathematical operator++++
print(7+3)
print(7-3)
print(7*3)
print(7/3)#Implicit typecasting.Python is automatically converting the result to float
print(7//3)
print(7**3)

#PE(MD)(AS)    (Parenthisis,Exponent,Multiplication,Division,Addition,Subtraction)
print(3*3+3/3-3)#left to right

#Number manipulation and f-strings
print(int(23.93))#Floors the number
print(round(23.93,1))#Rounds the number
score=0
score+=1#Shorthand operator
#f-string
bool1=True
print(f"Your score is:{score} and it is {bool1}")