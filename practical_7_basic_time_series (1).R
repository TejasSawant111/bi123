# Practical 7: Time Series Analysis
# Aim: Time-Series Analysis using R

# Get the data points in the form of R vector
rainfall <- c(799, 1174.8, 865.1, 1334.6, 635.4, 418.5,
              685.5, 998.6, 784.2, 985, 882.8, 1071)

# Convert into time-series object
rainfall.timeseries <- ts(rainfall, start = c(2023,1), frequency = 12)

# Print time series
print(rainfall.timeseries)

# Visualization
png(file = "rainfall.png")

# Plot the graph of time series
plot(rainfall.timeseries)

# Save file
dev.off()
