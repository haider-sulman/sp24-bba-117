# Create the student dictionary
student = {
    "name": "haider",
    "age": 20,
    "grade": "B",
    "GPA": 3.2,
    "major": "Business",
    "year": 3,
    "city": "Lahore",
    "country": "Pakistan",
    "email": "hs.vains@gmail.com",
    "phone": "0321-4633828"
}

# No.1. get() - Retrieve the student's email
print("1. Haider's email is:", student.get("email"))

# No.2. keys() - List all the keys (attributes of Haider)
print("2. List of attributes:", list(student.keys()))

# No.3. values() - List all the values (information about Haider)
print("3. Information about Haider:", list(student.values()))

# No.4. items() - Display all key-value pairs
print("4. Student attributes and their values:")
for attribute, value in student.items():
    print(f"   {attribute}: {value}")

# No.5. update() - Update Haider's grade
student.update({"grade": "A"})
print("5. Haider's updated grade:", student["grade"])

# No.6. pop() - Remove Haider's phone number and return it
removed_phone = student.pop("phone")
print("6. Haider's phone number was removed:", removed_phone)

# No.7. popitem() - Remove the last inserted item (likely 'phone')
last_entry = student.popitem()
print("7. Last entry removed (likely phone):", last_entry)

# No.8. copy() - Create a backup copy of the dictionary
student_backup = student.copy()
print("8. Backup of Haider's information:", student_backup)

# No.9. setdefault() - Add a new attribute only if it doesn't exist
student.setdefault("address", "Not provided")
print("9. Haider's information with address added:", student)

# No.10. fromkeys() - Create a new dictionary with default values for new attributes
new_attributes = ["hobby", "favorite_subject"]
default_values = dict.fromkeys(new_attributes, "Not specified")
print("10. New attributes with default values:", default_values)

# clear() - Would remove all items from the dictionary
student.clear()
print("All student data cleared:", student)