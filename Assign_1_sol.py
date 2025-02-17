#1.	Write a program to find the largest of two numbers using if-else statements.

a=10
b=20
if a > b :
    print("",a," is larger than ",b)
else:
    print("",b," is laregr than ",a)

#2.	Write a program that uses if-else statements to print whether a number is positive, negative, or zero.

n=10

if n > 0:
    print("Number is Positive")
elif n<0:
    print("Number is Negative")
else:
    print("Number is Zero")
    
#3.	Write a program that checks whether a given number is even or odd using the ternary operator.

n=11

result = "even" if n%2==0 else "odd"
print(result)

#4.	What is the output of the following expression? result = 25 // 4 * 3 + 18 % 7 - 5 * 2 / 2

result = 25 // 4 * 3 + 18 % 7 - 5 * 2 / 2
print(result)

#5.	Write a program to calculate the area of a triangle given its base and height using the formula Area = (base * height) / 2.

base = 10
height = 15

Area = (base * height) / 2

print(Area)

#6.	Write a program to calculate the perimeter of a rectangle using length and width variables.

length = 10
width = 20

perimeter = 2*(length + width)
print(perimeter)

#7.	Write a program that uses the modulus operator (%) to find the remainder when dividing two numbers.

A = int(input("Enter 1st Number "))
B = int(input("Enter 2nd Number "))

remainder = A%B
print("remainder of ",A," & ",B" is ",remainder)

#8.	Write a program to compare two numbers and print whether the first is greater, smaller, or equal to the second using relational operators.

A=10
B=20

if A>B:
    print("A is greater than B ")
elif A<B:
    print("A is smaller than B")
elif A==B:
    print("A is equal to B")
else:
    print("None is true")

#9.	Write a program that takes two integers and performs both floor division (//) and modulo (%) operations. Print the results

A=10
B=2

Floor_Division = A//B
print("Floor_Division of A & B " , Floor_Division )


modulus = A%B
print("modulus of A & B " , modulus )

#10. Write a program that prints the grade based on the score input using if-else statements (A for 90-100, B for 80-89, etc.).

N = 79

if N<=100 and N>=90:
    print("A Grade")
elif N<=89 & N>=80:
    print("B Grade")
elif N<=79 & N>=70:
    print("C Grade")
elif N<=69 & N>=60:
    print("D Grade")
elif N<=59 & N>=50:
    print("E Grade")
else :
    print("Fail")