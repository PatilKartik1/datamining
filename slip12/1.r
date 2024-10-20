# Q1. Write a R program to create a Dataframes which contain details of 5employees and
# display the details.
# Employee contain (empno,empname,gender,age,designation)

# Step 1: Create a data frame
employee_data <- data.frame(
  empno = c(101, 102, 103, 104, 105),
  empname = c("Alice", "Bob", "Charlie", "David", "Eva"),
  gender = c("Female", "Male", "Male", "Male", "Female"),
  age = c(28, 34, 29, 45, 30),
  designation = c("Manager", "Developer", "Analyst", "Designer", "Tester")
)

# Step 2: Display the data frame
print(employee_data)
