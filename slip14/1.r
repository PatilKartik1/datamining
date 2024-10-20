# Q1. Write a script in R to create a list of employees (name) and perform thefollowing:
# a. Display names of employees in the list.
# b. Add an employee at the end of the list
# c. Remove the third element of the list.

# Step 1: Create a list of employee names
employees <- list("Alice", "Bob", "Charlie", "David", "Eve")

# Step 2: a. Display names of employees in the list
print("Employee Names:")
print(employees)

# Step 3: b. Add an employee at the end of the list
employees <- append(employees, "Frank")
print("Updated Employee List after adding Frank:")
print(employees)

# Step 4: c. Remove the third element of the list
employees <- employees[-3]  # Removing Charlie (the third element)
print("Employee List after removing the third element:")
print(employees)
