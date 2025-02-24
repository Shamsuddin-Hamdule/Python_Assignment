#1. Write a function greet(name) that takes a name ehich is store in variable as input and prints "Hello, [name]!".

n=input("Enter Your Name : ")
print("Hello",n,"!")

#2. Create a function square(num) that returns the square of a given number.

n=int(input("enter a number to get Square of it : "))
print("The Square of your Number :",n," is ",n*n)

#3. Write a function is_even(n) that returns True if a number is even, otherwise False.

def is_even(n):
    if n%2 == 0:
        print("The number :",n," is even")
    else:
        print("The number :",n," is Odd")
        
is_even(10)

#4. Define a function sum_numbers(a, b=10) that takes two numbers and returns their sum. If the second number is not provided, it should default to 10.

def sum_numbers(a,b=10):
    print("the sum of numbers is",a+b)
    
sum_numbers(10)

#5. Write a recursive function factorial(n) to calculate the factorial of a number.

def fact(n):
    if n < 0:
        print("Number should be a Positive integer")
    elif n <= 1:
        print("Factorial of 0 & 1 is always 1")
    else:
        f=1
        i=n
        while n > 1:
            f = f*n
            n=n-1
        print("Factorial of ",i," is",f)
    
fact(10)

#6. Use a lambda function with filter( ) to get all even numbers from a list: [1, 2, 3, 4, 5, 6, 7, 8].

listy =  [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = list(filter(lambda x: x % 2 == 0, listy))
print(even_numbers)

#7. Write a while loop to print the first 5 multiples of 3.
print("first 5 multiples of 3")
i=1
while i <= 5 :
    print(i*3) 
    i = i+1
    

#8. Create a loop that prints all numbers from 1 to 20 but skips multiples of 5.

print("all numbers from 1 to 20 but skips multiples of 5")
for i in range (1 ,20):
    if i%5 == 0:
        print(i,"is Multiple of 5")
    else:
        print(i)
        

#9. Write a loop that stops when it encounters the number 7 in this list: [1, 2, 3, 4, 5, 6, 7, 8, 9].

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in liste:
    if i==7:
        break
    else:
        print(i)
        
#10. Write a program that checks if a year is a leap year. (Hint: A year is a leap year if it is divisible by 4 but not by 100, except when it is also divisible by 400.)

y = int(input("Enter Any Year : "))

if y%4==0:
    if y%100!=0:
        print("Leap Year")
    else:
        if y%400==0:
            print("Leap Year")
        else:
            print("Not A leap year")
else:
    print("Not A leap year")