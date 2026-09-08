# Practice set 3.2 



# 1. Create a tuple of five integers and print all elements. Access the first, last, and
# middle elements of a tuple.
tupl = (1,2,3,4,5,4,6,7,8,9,10)
a,*c,b = tupl
print(a),print(b),print(*c)

# 2. Count occurrence of a specific value. Also, find the index of a given element.
print(tupl.count(4))
print(tupl.index(4))
#  3. Concatenate two tuples & display the result. Also, Repeat a tuple three times.
tupl_2 = (1,22,33,44,55,66,77,88,99,10)
t = tupl + tupl_2
print(t)
print(t*5)
#  4. Reverse a tuple using slicing, find the max, min, sum, & average.
print(tupl[: : -1])
print(max(t))
print(min(t))
print(sum(t))

# 5. Convert a list into a tuple and a tuple into a list.

# List
my_list = [10, 20, 30, 40, 50]

# Convert List to Tuple
my_tuple = tuple(my_list)

print("List :", my_list)
print("Tuple:", my_tuple)
print(type(my_list))
print(type(my_tuple))
# Tuple
my_tuple = (100, 200, 300, 400)

# Convert Tuple to List
my_list = list(my_tuple)

print("Tuple:", my_tuple)
print("List :", my_list)
print(type(my_tuple))
print(type(my_list))



# 6. Perform tuple packing and unpacking for student details. Demonstrate
student = "yash","b.tech","2C",2502300101135
name, course, section, rollno = student
print(name, course,section,rollno )

# 7. Create a nested tuple and access inner elements.
nested = ((1,2,3,),(4,5,6),(7,8,9))
print(nested[1])
print(nested[0][2])

# 8. Store student records as tuples inside a list and display names with marks.
# Student records stored as tuples inside a list

students = [
    ("Yash", 90),
    ("Rahul", 85),
    ("Priya", 92),
    ("Aman", 78),
    ("Neha", 88)
]

print("Student Records")
print("-" * 25)

for student in students:
    print("Name :", student[0])
    print("Marks:", student[1])
    print("-" * 25)

    # 9. Swap two variables using tuple unpacking.
a,b = 1,2
print(a,b)
a,b = b,a
print("after the swap:",a,b)




# 10.Generate squares of numbers from 1 to 10 and store them in a tuple using tuple(x*x for x in range(1, 11))

squre = list(x*x for x in range(1,11) )
print(tuple(squre))
print(squre)

