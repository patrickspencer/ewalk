#!/usr/bin/env Rscript

args = commandArgs(trailingOnly=TRUE)
# first argument is company symbol e.g. 'YHOO'
# second argument is one of the following:
#     open, low, high, close, adj_close
if (length(args)==0) {
    stop("At least one argument must be supplied (input file).n", call.=FALSE)
}

library(dplyr)
library(prophet)
require("RPostgreSQL")
source("/etc/stockwalk_db_settings.R")

drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, dbname = db_name,
		 host = db_host, port = db_port,
		 user = db_user, password = db_pass)

symbol <- args[1]
query = paste("SELECT date,", args[2], " FROM stockwalk_quotes JOIN stockwalk_companies ON stockwalk_companies.id = stockwalk_quotes.company_id WHERE stockwalk_companies.symbol = '", symbol, "';", sep="")

print(query)
df <- dbGetQuery(con, query)
cnames <- colnames(df)
print(paste("colnames: ", cnames))
colnames(df) <- c("ds", "y")

# df <- read.csv('../data/peyton.csv') %>%
#     mutate(y = log(y))
m <- prophet(df)
future <- make_future_dataframe(m, periods = 365)
forecast <- predict(m, future)
name = c(symbol, "_", args[2], ".png")
graph_folder <- path.expand("~/stockwalk_graphs/")
l = c(graph_folder, name)
filename <- paste(l, collapse='')
print(filename)
png(filename=filename)
plot(m, forecast)
dev.off()
