# Univariate, Bivariate, and Multivariate Analysis Script (R)

# Load libraries
library(tidyverse)
library(ggplot2)
library(corrplot)

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

# Univariate analysis
if("TransactionAmt" %in% colnames(df)) {
  cat("Univariate Analysis: TransactionAmt\n")
  cat("Mean:", mean(df$TransactionAmt, na.rm = TRUE), "\n")
  cat("Median:", median(df$TransactionAmt, na.rm = TRUE), "\n")
  cat("Std:", sd(df$TransactionAmt, na.rm = TRUE), "\n")
}

# Bivariate analysis
if("TransactionAmt" %in% colnames(df)) {
  corr <- cor(df$TransactionAmt, df$isFraud, use = "complete.obs")
  cat("Correlation between TransactionAmt and isFraud:", corr, "\n")
}

# Multivariate analysis
key_features <- c("TransactionAmt", "card1", "card2", "card3", "card5", "isFraud")
key_features <- key_features[key_features %in% colnames(df)]

if(length(key_features) > 1) {
  corr_matrix <- cor(df[key_features], use = "complete.obs")
  png(file.path(output_dir, "correlation_matrix_r.png"), width = 800, height = 600)
  corrplot(corr_matrix, method = "color", type = "upper")
  dev.off()
  cat("Multivariate analysis complete!\n")
}

cat("Analysis Complete!\n")
