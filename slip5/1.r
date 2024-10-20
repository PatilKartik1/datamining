# Q1. Write a R program to concatenate two given factors

# Create two factors
factor1 <- factor(c("Apple", "Banana", "Cherry"))
factor2 <- factor(c("Date", "Elderberry", "Fig"))

# Concatenate the two factors
combined_factor <- factor(c(as.character(factor1), as.character(factor2)))

# Display the combined factor
print(combined_factor)
