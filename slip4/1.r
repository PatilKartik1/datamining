# Q1. Write a R program to calculate the sum of two matrices of given size

# Create two matrices of size 2x3
matrix1 <- matrix(1:6, nrow = 2, ncol = 3)  # First matrix
matrix2 <- matrix(7:12, nrow = 2, ncol = 3) # Second matrix

# Print the original matrices
cat("Matrix 1:\n")
print(matrix1)
cat("Matrix 2:\n")
print(matrix2)

# Calculate the sum of the two matrices
matrix_sum <- matrix1 + matrix2

# Print the result
cat("Sum of the two matrices:\n")
print(matrix_sum)
