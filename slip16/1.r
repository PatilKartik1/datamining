# Q1. Write a R program to create a simple bar plot of given data
# Year Export Import
# 2001 26 35
# 2002 32 40
# 2003 35 50

# Create the data
Year <- c(2001, 2002, 2003)
Export <- c(26, 32, 35)
Import <- c(35, 40, 50)

# Convert data to a data frame
data <- data.frame(Year, Export, Import)

# Set the bar width and position
bar_width <- 0.4
positions <- seq(1:length(Year))

# Create the bar plot
barplot(height = as.matrix(data[, -1]), 
        beside = TRUE, 
        names.arg = data$Year, 
        col = c("lightblue", "lightgreen"), 
        legend.text = c("Export", "Import"), 
        main = "Export and Import Data (2001-2003)", 
        xlab = "Year", 
        ylab = "Value", 
        ylim = c(0, 60))

# Add gridlines
grid(nx = NULL, ny = NULL)
