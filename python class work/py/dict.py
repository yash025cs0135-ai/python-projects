# ============================================================
# Dictionary Practice Set 3.4
# Q1 to Q7 - Combined Program
# ============================================================


# Q1. Create a dictionary containing employee details
print("\n========== Q1 ==========")

employee = {
    "Name": "Amit",
    "Department": "IT",
    "Salary": 45000,
    "Designation": "Developer"
}

print("Employee Name:", employee["Name"])
print("Department:", employee["Department"])
print("Salary:", employee["Salary"])
print("Designation:", employee["Designation"])


# Q2. Add new key-value pairs
print("\n========== Q2 ==========")

employee["Email"] = "amit@gmail.com"
employee["Phone Number"] = "9876543210"

print("Updated Dictionary:")
print(employee)


# Q3. Update the salary
print("\n========== Q3 ==========")

print("Before:", employee)

employee["Salary"] = 52000

print("After:", employee)


# Q4. Remove specific key and last inserted item
print("\n========== Q4 ==========")

student = {
    "Name": "Rahul",
    "Age": 20,
    "Branch": "CSE",
    "Marks": 85
}

print("Original Dictionary:", student)

# Remove specific key
student.pop("Age")
print("After removing Age:", student)

# Remove last inserted item
student.popitem()
print("After removing last item:", student)


# Q5. Print all keys, values and key-value pairs
print("\n========== Q5 ==========")

student = {
    "Roll": 101,
    "Name": "Rahul",
    "Branch": "CSE",
    "Sem": 5
}

print("All Keys:", student.keys())
print("All Values:", student.values())
print("All Key-Value Pairs:", student.items())


# Q6. Check whether a given key exists
print("\n========== Q6 ==========")

key = input("Enter a key to search: ")

if key in student:
    print("Key Found")
else:
    print("Key Not Found")


# Q7. Count total number of key-value pairs
print("\n========== Q7 ==========")

print("Total number of key-value pairs:", len(student))

# ============================================================
# Dictionary Practice Set 3.4
# Q8 to Q11 - Combined Code
# ============================================================


# Q8. Create a dictionary from two lists
print("\n========== Q8 ==========")

keys = ["ID", "Name", "Age", "City"]
values = [101, "Ankit", 20, "Delhi"]

student_dict = dict(zip(keys, values))

print("Dictionary:", student_dict)


# Q9. Create a nested dictionary for three students
print("\n========== Q9 ==========")

students = {
    "Student1": {
        "Name": "Rahul",
        "Branch": "CSE",
        "Semester": 5,
        "CGPA": 8.5
    },

    "Student2": {
        "Name": "Ankit",
        "Branch": "ECE",
        "Semester": 5,
        "CGPA": 8.2
    },

    "Student3": {
        "Name": "Aman",
        "Branch": "ME",
        "Semester": 5,
        "CGPA": 7.9
    }
}

print("Complete Nested Dictionary:")
print(students)


# Q10. Print specific information from nested dictionary
print("\n========== Q10 ==========")

print("Name of Student 2:", students["Student2"]["Name"])

print("Branch of Student 3:", students["Student3"]["Branch"])

print("CGPA of Student 1:", students["Student1"]["CGPA"])


# Q11. Nested dictionary for departments
print("\n========== Q11 ==========")

departments = {
    "CSE": {
        "HOD": "Dr. Sharma",
        "Faculty": 25,
        "Students": 300
    },

    "ECE": {
        "HOD": "Dr. Verma",
        "Faculty": 20,
        "Students": 250
    },

    "ME": {
        "HOD": "Dr. Singh",
        "Faculty": 18,
        "Students": 200
    }
}


# 1. Print HOD of ECE department
print("\n1. HOD of ECE:", departments["ECE"]["HOD"])


# 2. Print number of students in CSE department
print("2. Students in CSE:", departments["CSE"]["Students"])


# 3. Update faculty count of ME department
departments["ME"]["Faculty"] = 22

print("3. Updated ME Faculty:",
      departments["ME"]["Faculty"])


# 4. Add a new department named Civil
departments["Civil"] = {
    "HOD": "Dr. Gupta",
    "Faculty": 15,
    "Students": 180
}

print("4. Civil Department Added")


# 5. Print all department names
print("\n5. All Department Names:")

for department in departments:
    print(department)


# 6. Print complete nested dictionary
print("\n6. Complete Department Dictionary:")
print(departments)