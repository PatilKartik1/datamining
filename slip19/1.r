# Q1. Write aR program to create a Dataframes which contain details of 5 Studentsand display the
# details.
# Students contain (Rollno,Studname,Address,Marks)

# Create a Data Frame in R

# Define vectors for student details
Rollno <- c(101, 102, 103, 104, 105)
Studname <- c("John", "Mary", "Alice", "Bob", "David")
Address <- c("New York", "London", "Paris", "Berlin", "Tokyo")
Marks <- c(85, 90, 78, 88, 92)

# Create the Data Frame
student_df <- data.frame(Rollno, Studname, Address, Marks)

# Display the Data Frame
print("Student Details:")
print(student_df)
