# Q1. Write a R programto create a data frame using two given vectors and displaythe duplicate
# elements

# Define two vectors
vector1 <- c(10, 20, 10, 30, 40, 50, 20)
vector2 <- c("A", "B", "A", "C", "D", "E", "B")

# Create a data frame using the two vectors
df <- data.frame(Column1 = vector1, Column2 = vector2)

# Display the data frame
print("Data Frame:")
print(df)

# Identify and display duplicated elements
duplicated_rows <- df[duplicated(df) | duplicated(df, fromLast = TRUE), ]
print("Duplicated Elements:")
print(duplicated_rows)
