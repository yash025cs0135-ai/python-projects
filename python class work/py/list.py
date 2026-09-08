# 1. Create a list of your five favorite movies and display the list
movies = ["KGF","FAST AND FAURIOS","LONDAN HAS FALLEN","HUNTER KILLER","KINGSMEN","KGF2","TOXIC"]
print(movies)

# 2. Create a list containing 10 numbers and display: First, Last, Middle element

num = [1,2,3,4,5,6,7,8,9,10]
a,*c,b = num
print(a,)
print(b,)
print(*c ,)

# 3. Create a list of five cities and print the list in reverse order using slicing

cities =["modinager","delhi","muradnager","gujrat","agra","Noida"]
print(cities[::-1])


# 4. Create two lists of five numbers each and combine.
# 6. Create a list of five fruits and add one more fruit. Now, Insert your favorite color
# at the second position of a list.
# 8. Remove the third element using `del`. Now, remove all element.
# 11. Create a copy of a list using `copy()` and print both lists.
# 12. Create a list containing duplicate values and count the occurrence of a particular
# value using `count()`.
# 13. Find the index of a given element using the `index()`.
# 14. Create a nested list representing a 3×3 matrix and print it.
# 15. Perform the following slicing opera


# 4. Create two lists of five numbers each and combine.
list_1=[1,2,3,4,5]
list_2 =[6,7,8,9,10]
list = list_1 + list_2
print(list)
 

# 5. Create a list and display it three times.
fruits = ["mango","grapes","dates","apple","pinapple"]
print(fruits *3)



# 6. Create a list of five fruits and add one more fruit. Now, Insert your favorite color
# at the second position of a list  
fruits = ["mango","grapes","dates","apple","pinapple"]
print(fruits.extend([" water melon","fig","bannana"]))
print(fruits.insert(1,"black"))
print(fruits)

# 7. Create two lists & combine them using `extend()`.Now, remove last element.
list_1 =[1,2,3,4,5]
list_2 =[6,7,8,9,10]
print(list_1.extend(list_2))
print(list_1)
print(list_1.pop())

# 8. Remove the third element using `del`. Now, remove all element.
list =[11,22,33,44,555,66,77]
print(list.pop(3))
print(list.clear())
print(list)

# 9. Create a list of numbers and sort it in ascending and descending order.

num = [1,2,3,11,12,13,5,6,7,14,15]
print(num.sort())
print(num)
print(num.sort(reverse=True))
print(num)

# 10. Reverse a list using the `reverse()` method.
a = ["A","b","c","d","e"]
print(a.reverse())
print(a)
