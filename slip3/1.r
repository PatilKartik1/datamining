# Q1. Write a R program to reverse a number and also calculate the sum ofdigits of that
# number.

# Function to reverse a number and calculate the sum of its digits
reverse_and_sum <- function(num) {
  original_num <- num
  rev <- 0
  sum_digits <- 0
  
  while (num > 0) {
    digit <- num %% 10          # Get the last digit
    rev <- rev * 10 + digit    # Build the reversed number
    sum_digits <- sum_digits + digit # Sum the digits
    num <- num %/% 10          # Remove the last digit
  }
  
  cat("Original Number:", original_num, "\n")
  cat("Reversed Number:", rev, "\n")
  cat("Sum of Digits:", sum_digits, "\n")
}

# Example usage
number <- 12345
reverse_and_sum(number)
