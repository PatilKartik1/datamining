# Q1. Write a R program to get the first 20 Fibonacci numbers

# Initialize the length of the Fibonacci sequence
n <- 20

# Create a numeric vector to store Fibonacci numbers
fibonacci <- numeric(n)

# Set the first two Fibonacci numbers
fibonacci[1] <- 0
fibonacci[2] <- 1

# Generate the remaining Fibonacci numbers
for (i in 3:n) {
  fibonacci[i] <- fibonacci[i-1] + fibonacci[i-2]
}

# Print the first 20 Fibonacci numbers
print(fibonacci)
