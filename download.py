#qs
# a = 5
# b = 4
# c = a+b#9
# a = c-a#a = 4
# b = c-a#b = 5
# age = int(input("enter the age: "))

# if age >= 18 and age <= 60:
#     print("you are eligible")
# else:
#     print("you are not eligible")

# age1 = int(input("enter the age: "))
# age2 = int(input("enter the age: "))
# if age1>21 or age2 >21:
#     print("allowed")
# else:
#     print("not allowed")
# age = int(input("enter the age: "))
# email = input("do you have vailid email address? (yes/no): ")
# if age >=18 and email =="yes":
#     print("you are eligible to participate")
# else:
#     print("you are not eligible to participate")

#bitwise operator
# x , y = 10 , 6
# a = x&y
# print(bin(a))
# b = x|y
# print(bin(b))
# c = x^y
# print(bin(c))
# d = ~x
# print(bin(d))
# e = x <<2
# print(bin(e))
# f = x >>2
# print(bin(f))
# x ,y = 6,7
# a = x is not y
# print(a)
# print(id(x))
# print(id(y))

# str = 'hellohowareyou'
# print("h" not in str)
# num = int(input("enter the number: "))
# if num > 0:
#     print("positive")
# elif num < 0:
#     print("negative")
# elif num ==0:
#     print("zero")
# else:
#     print("none")
# age = int(input("enter the age: "))
# if age > 18:
#     print('eligible')
# elif age < 18:
#     print("not")
# else:
#     print("n")


# set
# s1 = {1,2,3,7,8,8,9,9,10}
# print(s1)
# s2 = set('hello ')
# print(s2)

# writ a program to remove all duplicate in the list and return list





# for i in s1:
#     print(i)
# print(len(s1))
# print(min(s1))
# print(max(s1))
# print(sum(s1))
# print(sorted(s1))

# my_set = {1, 2, 3, 4}
# my_set.add(5)
# print(my_set)  # Output: {1, 2, 3, 4, 5}

# set1 = 
# set2 =
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set2-set1)
  
#dict
# d1 = {102:"ram",13:"sohan",14:"sita"}
# print(type(d1))
# d2 =dict(a="102",b="123",c="345")
# print(type(d2))

# d1 = {102:"ram",13:"sohan",14:"sita",15:"kamani",19:"gapati"}
# print(d1[102],d1[13],d1[14])
# for k in d1:
#     print(k,d1[k])
#how to edit 
#d1 = {102:"ram",13:"sohan",14:"sita",15:"kamani",19:"gapati"}
# print(d1.keys())
# print(d1.values())

#dict comprehension

# dct2 ={a:a**2 for a in range(1,10,1)}
# print(dct2)

#QUESTION PRECITS OF DIFFERENT ITREABLE
# list = [1,2,3,4,5]
# list.append(6)
# print(list)

# latters= ['a','b','c','d','e']
# latters.reverse()
# print(latters)
# latters.pop()
# latters.pop()
# latters.pop()
# print(latters)
# latters.reverse()
# print(latters)
#qs
# l1 =[a**2 for a in range(1,11,1)]
# print(l1)

# how to add corresponding element of two list
l1 = [1,3,5,7,9]
l2 = [2,3,4,6,8]

# list = []
# for i in range(len(l1)):
#     list.append(l1[i] + l2[i])
# print( list)
# print(max(list))
# print(min(list))
# print(sum(list))

# """
# fibonacci searies - learn what is this
# implement  -

# iterative approach       # home work
# recursive - approach
# sub array problem - string
# # """
# Html  - history


#qs on recursion  calculate sum of square of n natural number

# def sumsquare(n):
#     if n == 1:
#         return 1
#     s = n*n + sumsquare(n-1)
#     return s

# x = sumsquare(4)
# print(x)

# num = int(input("enter the number: "))
# a , b = 0,1
# for i in range (0,num):
#     if i <= 1:
#         print(i)
#     else:
#         c = a+b 
#         a = b
#         b = c
#         print(c)   
 # fibonacci series using while loop  
# num = 56
# a , b,c  = 0,1,0
# print(a)
# print(b)
# i = 1
# while i < num:
#     c = a+b
#     a = b
#     b = c
#     i = i+1
#     print(c)

 #new concept how does work function object
# def add(a,b):
#     return a+b
# x =add         
# print(id(add))
# print(id(x))
# print(x is add)

#lambda expression

# k =(lambda a,b:a+b)(4,5)
# print(k)
# f1 = lambda a,b ,c,d:a+b+c+d
# print(f1(20,45,67,78))

#HOW TO CALCULATE FACTORIAL USING RECURRISION

# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return n*fact(n-1)
# x = fact(10)
# print(x)

#HOW TO CALCULATE FACTORIAL USING LAMBDA

# f = lambda n : 1 if n==0 or n ==1 else n*f(n-1)
# print(f(18))

#question pr
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return n*fact(n-1)
# print(fact(8))
# #qs
# a,b =0,1
# for i in  range(0,5):
#     if i <=1:
#         print(i)
#     else:
#         c = a+b
#         a = b 
#         b =c
#         print(c)

#QESTION BASED ON LIST 
#SWAP ELEMENT IN THE LIST
# l1 = [34,56,78,23,89]
# pos1,pos2,pos0,pos3= 2,1,3,0
# l1[pos1],l1[pos2],l1[pos0],l1[pos3]= l1[pos2],l1[pos1],l1[pos3],l1[pos0]
# print(l1)
#SWAP FIRST AND LAST ELEMENT
# l1 = [346,56,78,23,89,987]
# pos0,pos5= 5,0
# l1[pos0],l1[pos5]= l1[pos5],l1[pos0]
# print(l1)


# QUESTION PRACTICS
# list = [3,4,5,2,7,9,8,6,5]
# count = sum(list)
# print(count/len(list))#average


# CREATING ARRAYS
# from array import *
# a1 = array('b'[23,67])
# print(type(a1))
    
import array
print(array.array('b'[23,45]))
























































