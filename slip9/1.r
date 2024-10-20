# Q1. Write an R program to create a Data frames which contain details of 5 employees and display
# summary of the data.

# Create vectors for employee details
names <- c("John Doe", "Jane Smith", "Alice Johnson", "Bob Brown", "Eve Davis")
ages <- c(28, 34, 29, 45, 38)
designations <- c("Software Engineer", "Data Scientist", "Product Manager", "HR Manager", "Marketing Specialist")
salaries <- c(70000, 80000, 75000, 60000, 72000)

# Create a data frame
employees <- data.frame(Name = names, Age = ages, Designation = designations, Salary = salaries)

# Display the data frame
print("Employee Details:")
print(employees)

# Display summary of the data
print("Summary of Employee Data:")
summary(employees)
