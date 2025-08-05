student_profile = {}

# Get user input and assign to dictionary
student_profile["name"] = input("Enter the student's name: ")
student_profile["age"] = input("Enter the student's age: ")
student_profile["enrolled"] = input("Is the student enrolled? (yes/no) ").strip().lower()

# Display the profile
print("Student Profile")
print(f"Name: {student_profile['name']}")
print(f"Age: {student_profile['age']}")
print(f"Enrolled: {student_profile['enrolled']}")