library(tidyverse)
library(rvest)
library(janitor)

#NEPSE LIVE DATA

url <- 'https://merolagani.com/LatestMarket.aspx'

# EXTRACT HTML

url_html <- read_html(url)

# TABLE EXTRACTION

url_tables <- url_html %>% html_table(fill = TRUE)

live_data <- url_tables[[1]]

live_data %>%
  select(1:9) -> live_data

live_data %>% clean_names() -> live_data
