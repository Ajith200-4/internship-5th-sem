# 1) gretest of three number
# n1=int(input())
# n2=int(input())
# n3=int(input())
# if n1>n2:
#     print("gretest number is",n1 )
# elif n2>n3:
#     print("gretest number is",n2 )
# else:
#     print("gretest number is",n3 )


# 2) finding even or odd
# num=int(input("enter number:"))

# if num%2==0:
#     print("even")
# else:
#     print("odd")
# 3 
# age = int(input("Enter age: "))

# if age < 18:
#     print("Not allowed")
#     if age >= 75:
#       print("Risk")
#     elif age >= 25:
#       print("Panic")
# elif age > 18:
#     print("Don't do nonsense")
# else:
#     print("Allowed")
# # 4 watermelon
# w=int(input("enter a weight between 1 and 100:"))
# if w>=1 and w<=100:
#     if w%2==0:
#         x=w//2
#         if x%2==0:
#             print("yes",x,x)
#         else:
#             print(x-1,x+1)
#             print("Yes")
#     else:
#         print("No")
# else:
#     print("corret weight as given for above conditions ")

#5th 
# x = int(input())
# steps = x // 5
# if x % 5 != 0:
#     steps += 1
# print(steps)
# n=int(input('Enter a number '))
# if n%7==0 or n%10==7:
#     print('Buzz number')
# else:
#     print('Not a buzz number')

# # Input two numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if a == b:
#     print("yes")
# else:
#     print("no")
# even numbers
# for i in range (1,50,2):
#         print(i,end=" ")
# prime numbers
# n= int(input("enter number: "))
# for i in range(2,n):
#     if n%i==0:
#         print("not prime")
#         break
# else:
#     print("prime").

## cout of prime in a range
# def isprime(n):
#     for i in range(2,(n//2)+1):
#         if n%i==0:
#             return False
#     return True
# l=int(input())
# r=int(input())
# c=0
# for i in range(l,r+1):
#     if isprime(i):
#         c+=1
# print(c)

# n=int(input("Enter number"))
# sum=0
# while n!=0:
#     d=n%10
#     sum=sum-d
#     n=n//10
# print(sum)

#
# n=int(input("Enter number"))
# count=0
# while n!=0:
#     count+=1
#     n=n//10
# print(count)

# n=int(input("Enter number"))
# rev=0
# while n!=0:
#      count+=1
#      n=n//10
# print(rev)
# for i in range(5):
#     if i<3:
#         break 
#     print(i)
t=tuple(map(int,input().split()))
i=int(input())
