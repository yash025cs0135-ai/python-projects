# ============================================================
# Q1. Write program to add following elements to an existing
# set: 25, 35, 45. Print new set.
# ============================================================

my_set = {10, 20, 30}

my_set.add(25)
my_set.add(35)
my_set.add(45)

print("Q1 - New Set:", my_set)


# ============================================================
# Q2. Write a Python program to remove elements from a set
# using remove(), discard(), pop().
# Display the set after each operation.
# ============================================================

my_set = {10, 20, 30, 40, 50}

my_set.remove(20)
print("Q2 - After remove():", my_set)

my_set.discard(30)
print("Q2 - After discard():", my_set)

my_set.pop()
print("Q2 - After pop():", my_set)


# ============================================================
# Q3. Write a Python program to create two sets and perform:
# Union, Intersection, Difference, Symmetric Difference.
# ============================================================

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Q3 - Union:", A.union(B))
print("Q3 - Intersection:", A.intersection(B))
print("Q3 - Difference (A-B):", A.difference(B))
print("Q3 - Symmetric Difference:", A.symmetric_difference(B))


# ============================================================
# Q4. Write a Python program to determine whether two sets
# are disjoint.
# ============================================================

A = {1, 2, 3}
B = {5, 6, 7}

print("Q4 - Are sets disjoint?", A.isdisjoint(B))


# ============================================================
# Q5. Write a Python program to remove duplicate values
# from the list using a set.
# ============================================================

numbers = [10, 20, 10, 30, 20, 40, 30, 50]

unique_numbers = set(numbers)

print("Q5 - Original List:", numbers)
print("Q5 - After removing duplicates:", unique_numbers)


# ============================================================
# Q6. Write a Python program to find the common subjects
# chosen by two students.
#
# Student1 = {"Python", "Java", "SQL", "Excel"}
# Student2 = {"Python", "C", "Excel", "Power BI"}
# ============================================================

Student1 = {"Python", "Java", "SQL", "Excel"}
Student2 = {"Python", "C", "Excel", "Power BI"}

common_subjects = Student1.intersection(Student2)

print("Q6 - Common Subjects:", common_subjects)


# ============================================================
# Q15. A college has two clubs:
#
# Science Club = {"Aman","Riya","Rahul","Priya","Ankit"}
# Coding Club = {"Rahul","Ankit","Simran","Rohit","Riya"}
#
# Write a Python program to:
# 1. Display all students enrolled in either club.
# 2. Display students enrolled in both clubs.
# 3. Display students only in Science Club.
# 4. Display students only in Coding Club.
# 5. Check whether two clubs have any common members.
# 6. Add a new student to Coding Club.
# 7. Remove one student from Science Club.
# ============================================================

Science_Club = {"Aman", "Riya", "Rahul", "Priya", "Ankit"}
Coding_Club = {"Rahul", "Ankit", "Simran", "Rohit", "Riya"}


# 1. Students enrolled in either club
either_club = Science_Club.union(Coding_Club)
print("Q15.1 - Either Club:", either_club)


# 2. Students enrolled in both clubs
both_clubs = Science_Club.intersection(Coding_Club)
print("Q15.2 - Both Clubs:", both_clubs)


# 3. Students only in Science Club
only_science = Science_Club.difference(Coding_Club)
print("Q15.3 - Only Science Club:", only_science)


# 4. Students only in Coding Club
only_coding = Coding_Club.difference(Science_Club)
print("Q15.4 - Only Coding Club:", only_coding)


# 5. Check whether clubs have common members
print("Q15.5 - Common Members Exist:",
      not Science_Club.isdisjoint(Coding_Club))


# 6. Add a new student to Coding Club
Coding_Club.add("Yash")
print("Q15.6 - After adding Yash:", Coding_Club)


# 7. Remove one student from Science Club
Science_Club.remove("Priya")
print("Q15.7 - After removing Priya:", Science_Club)