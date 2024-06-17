# Exploratory Data Analysis Script (R)

# Load libraries
library(tidyverse)
library(ggplot2)

# Resolve project root robustly (Rscript --file=..., source(), or cwd candidates)
resolve_project_root <- function(marker_file = file.path("data", "fraud_data.csv")) {
  args <- commandArgs(trailingOnly = FALSE)
  file_arg <- grep("^--file=", args, value = TRUE)
  if (length(file_arg) > 0) {
    script_path <- normalizePath(sub("^--file=", "", file_arg), winslash = "/", mustWork = FALSE)
    root <- normalizePath(file.path(dirname(script_path), "..", ".."), winslash = "/", mustWork = FALSE)
    if (file.exists(file.path(root, marker_file))) return(root)
  }
  for (i in seq_len(sys.nframe())) {
    ofile <- sys.frame(i)$ofile
    if (!is.null(ofile)) {
      root <- normalizePath(file.path(dirname(ofile), "..", ".."), winslash = "/", mustWork = FALSE)
      if (file.exists(file.path(root, marker_file))) return(root)
    }
  }
  candidates <- c(
    getwd(),
    normalizePath(file.path(getwd(), "..", ".."), winslash = "/", mustWork = FALSE),
    normalizePath(file.path(getwd(), ".."), winslash = "/", mustWork = FALSE)
  )
  for (cand in unique(candidates)) {
    if (file.exists(file.path(cand, marker_file))) {
      return(normalizePath(cand, winslash = "/", mustWork = FALSE))
    }
  }
  normalizePath(getwd(), winslash = "/", mustWork = FALSE)
}
project_root <- resolve_project_root()

# Load data
data_path <- file.path(project_root, "data", "fraud_data.csv")
output_dir <- file.path(project_root, "outputs", "figures")
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

df <- read.csv(data_path, stringsAsFactors = FALSE)
cat("Data loaded:", dim(df), "\n")

# Target variable distribution
target_counts <- table(df$isFraud)
cat("Target Distribution:\n")
print(target_counts)

# Missing values
missing_data <- df %>%
  summarise_all(~sum(is.na(.))) %>%
  gather(key = "Column", value = "Missing_Count") %>%
  filter(Missing_Count > 0) %>%
  arrange(desc(Missing_Count))

cat("\nMissing Values:\n")
print(head(missing_data, 20))

# Transaction Amount Analysis
if("TransactionAmt" %in% colnames(df)) {
  cat("\nTransaction Amount Statistics:\n")
  cat("Mean:", mean(df$TransactionAmt, na.rm = TRUE), "\n")
  cat("Median:", median(df$TransactionAmt, na.rm = TRUE), "\n")
  cat("Std:", sd(df$TransactionAmt, na.rm = TRUE), "\n")
  
  # Save plot
  png(file.path(output_dir, "transaction_amount_r.png"), width = 800, height = 600)
  hist(df$TransactionAmt, main = "Transaction Amount Distribution", 
       xlab = "Transaction Amount", col = "steelblue")
  dev.off()
}

cat("\nEDA Complete!\n")
