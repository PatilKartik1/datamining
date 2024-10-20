# Q1. Write an R program to calculate the multiplication table using afunction.

# Function to print the multiplication table
multiplication_table <- function(num) {
  cat("Multiplication Table of", num, ":\n")
  for (i in 1:10) {
    cat(num, "x", i, "=", num * i, "\n")
  }
}

# Get user input
number <- as.integer(readline(prompt = "Enter a number: "))

# Call the function
multiplication_table(number)
