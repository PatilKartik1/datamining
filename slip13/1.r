# Q1. Draw a pie chart using R programming for the following datadistribution:
# Digits on
# Dice
# 1 2 3 4 5 6
# Frequency of
# getting each
# number
# 7 2 6 3 4 8

# Step 1: Define the data
dice_numbers <- c(1, 2, 3, 4, 5, 6)
frequencies <- c(7, 2, 6, 3, 4, 8)

# Step 2: Create the pie chart
pie(frequencies, 
    labels = dice_numbers, 
    main = "Pie Chart of Dice Roll Frequencies", 
    col = rainbow(length(frequencies)))

# Optional: Add a legend
legend("topright", 
       legend = dice_numbers, 
       fill = rainbow(length(frequencies)), 
       title = "Dice Numbers")
