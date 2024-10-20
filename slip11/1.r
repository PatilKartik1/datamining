# Q1. Write a R program to find all elements of a given list that are not inanother given list.
# = list("x", "y", "z")
# = list("X", "Y", "Z", "x", "y", "z")

# Define the two lists
list1 <- list("x", "y", "z")
list2 <- list("X", "Y", "Z", "x", "y", "z")

# Convert lists to vectors for easier comparison
vec1 <- unlist(list1)
vec2 <- unlist(list2)

# Find elements in list1 that are not in list2
result <- vec1[!vec1 %in% vec2]

# Print the result
print(result)
