# Q1. Write a R program to create a data frame from four given vectors

# Create four vectors
Rollno <- c(101, 102, 103, 104, 105)
Studname <- c("John", "Alice", "David", "Mary", "Bob")
Address <- c("New York", "Los Angeles", "Chicago", "Houston", "Miami")
Marks <- c(85, 90, 78, 92, 88)

# Create a data frame from the vectors
students_df <- data.frame(Rollno, Studname, Address, Marks)

# Display the data frame
print(students_df)
