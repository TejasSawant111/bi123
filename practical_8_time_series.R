# Practical 8 A and B
# Aim: Time Series Analysis and Decomposition

sales <- c(120,130,150,170,160,180,200,220,210,230,250,270,
           125,135,155,175,165,185,205,225,215,235,255,275)

ts_data <- ts(sales, start = c(2023,1), frequency = 12)

# Decomposition
decomp <- decompose(ts_data, type = "additive")
plot(decomp)

# Moving Average
ma <- filter(ts_data, rep(1/3, 3), sides = 2)
plot(ts_data, col = "blue")
lines(ma, col = "red")

# Install and load tseries package
install.packages("tseries")
library(tseries)

# ADF Test
adf.test(ts_data)

# Choose CRAN mirror
chooseCRANmirror()

# Install and load forecast package
install.packages("forecast")
library(forecast)

# Auto ARIMA
auto.arima(ts_data)

model <- auto.arima(ts_data)
summary(model)

# Forecast
future <- forecast(model, h = 6)
plot(future)

accuracy(future)

# Save output
png(file = "bi_25191.png")
# or
save.image("C:\Users\bscit\Desktop\bi_25191\p7.RData")
