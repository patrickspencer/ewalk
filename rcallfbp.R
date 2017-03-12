#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)
if (length(args)==0) {
stop("At least one argument must be supplied (input file).n", call.=FALSE)
}

library(prophet)
library(dplyr)
df <- read.csv('data/data.csv') %>%
    mutate(y = log(y))
m <- prophet(df)
future <- make_future_dataframe(m, periods = 365)
forecast <- predict(m, future)
x <- c(args[1], ".png")
filename <- paste(x, collapse='')
print(filename)
png(filename=filename)
plot(m, forecast)
dev.off()
