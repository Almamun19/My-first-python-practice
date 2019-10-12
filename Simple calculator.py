#make a simple calculator.
#This function adds two number.
def add(x,y):
    return x+y
#This function subtracts two number.
def sub(x,y):
    return x-y
#This function multiplies two number.
def multiply(x,y):
    return x*y
#This function divides two number.
def divide(x,y):
    return x/y
print('select operation:')
print('1.Add')
print('2.Subtruct')
print('3.Multiply')
print('4.Divide')
#Take input from user.
chose=input('Enter choice(1/2/3/4):')
num1=int(input('Enter first number: '))
num2=int(input('Enter second number: '))
if chose=='1':
    print(num1,'+',num2,'=', add(num1,num2))
elif chose=='2':
    print(num1,'-',num2,'=',sub(num1,num2))
elif chose=='3':
    print(num1,'*',num2,'=',multiply(num1,num2))
elif chose=='4':
    print(num1,'/',num2,'=',divide(num1,num2))
else:
    print('Invalid input.')