# 1. toprint all even & odd numbers separately from 1 to 50 using a loop and conditional statements.

# print("Even")
# for i in range(1,51):
#     if (i%2==0):
#         print(i)

# print("Odd")
# for i in range(1,51):
#     if(i%2 != 0):
#         print(i)

# 2. tofind the sum of all numbers between 1 and 100 that are divisible by both 3 and 5.

# a = 0
# for i in range(1,101):
#     if (i%3==0)and(i%5==0):
#         a = a + i
# print(a)

# 3. to accept 10 numbers from the user and count how many are positive, negative, and zero using a loop and conditional statements.

# positive = 0 
# negative = 0
# zero = 0

# for i in range(1,11):
#     a = float(input("enter the value"))
 
#     if (i>0):
#         positive +=1
#     elif (i<0):
#         negative +=1
#     elif (i==0):
#         zero +=1
#     else:
#         print()
# print ("the count of the positive input is :",positive)
# print ("the count of the negative input is :",negative)
# print ("the count of the zero input is :",zero)

# 4. to check whether a given number is an Armstrong number or not using a loop and conditional statements.

# a =int (input ("enter the number :"))

# b = str(a)
# p = len(b)
# po = int(p)
# t = 0
# for i in b:
#     d = int(i)
#     t += pow(d,po)
# if t == a :
#     print ("the no is armstrong ")
# else:
#     print ("the no is not armstrong")

# 5. to generate the multiplication tables from 1 to 5. For each table, display only those multiples that are even.

# b = 0 

# for i in range(1,6):
#    for j in range (1,11):
#       b = i * j 
#       if b%2==0:
#          print(b)

# 6. using nested loops to print the following pattern:
# 7. using nested loops to print all pairs (i, j) where i and j range from 1 to 5, but display only those
# pairs whose sum is even.
# a = 0

# for i in range(1,6):
#     for j in range(1,6):
#         a = i +j
#         if a%2==0:
#             print(i,j)   

# 8. using nested loop to print the multiplication tables from 2 to 5, with each table containing multiples
# from 1 to 10. Use a conditional statement to display only the multiples that are divisible by 3.
# b=0

# for i in range(2,6):
#     for j in range(1,11):
#         b = i *j
#         if b%3==0:
#             print(b)

# 9. to print numbers from 1 to 20, but use continue to skip all numbers that are divisible by 3.

# for i in range (1,21):
#     if i %3== 0 :
#         continue
#     print(i)

# 10. that repeatedly accepts numbers from the user and calculates their sum. Terminate the loop using
# break when the user enters 0.

# for i in range(100):
#     a = int(input("enter the first number :"))
#     if (a == 0 ):
#         print("error : The given value of a is zero")
#         break

#     b = int (input("enter the second number :"))
#     if (b == 0 ):
#         print("error : The given value of b is zero")
#         break
#     c = a + b
#     print (c) 

# 11. to print numbers from 1 to 10. Use pass when the number is 5 and observe that the loop
# continues normally. Also display all the numbers.

for i in range (1,11):
    if i == 5 :
        pass
    print(i)