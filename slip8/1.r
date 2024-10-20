# Q1. Write a R program to get the first 10 Fibonacci numbers.

# Initialize the Fibonacci sequence
fibonacci <- numeric(10)  # Create a vector to hold the first 10 Fibonacci numbers
fibonacci[1] <- 0          # First Fibonacci number
fibonacci[2] <- 1          # Second Fibonacci number

# Generate the Fibonacci sequence
for (i in 3:10) {
  fibonacci[i] <- fibonacci[i - 1] + fibonacci[i - 2]
}

# Print the Fibonacci numbers
print("First 10 Fibonacci numbers:")
print(fibonacci)
