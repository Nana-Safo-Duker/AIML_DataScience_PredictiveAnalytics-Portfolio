# Helper functions for path resolution in R scripts
# Works when run from project root or from scripts/r/

resolve_project_paths <- function(data_filename = "Advertisement.csv",
                                  data_subdir = "data",
                                  output_subdir = "output") {
  candidates <- list(
    list(
      data = file.path(data_subdir, data_filename),
      output = output_subdir
    ),
    list(
      data = file.path("..", "..", data_subdir, data_filename),
      output = file.path("..", "..", output_subdir)
    ),
    list(
      data = file.path("..", data_subdir, data_filename),
      output = file.path("..", output_subdir)
    )
  )

  for (candidate in candidates) {
    if (file.exists(candidate$data)) {
      if (!dir.exists(candidate$output)) {
        dir.create(candidate$output, recursive = TRUE, showWarnings = FALSE)
      }
      return(candidate)
    }
  }

  stop(paste0(
    "Cannot find ", data_filename, ". Tried:\n",
    paste("  -", vapply(candidates, function(c) c$data, character(1)), collapse = "\n"),
    "\nCurrent working directory: ", getwd()
  ))
}

find_data_file <- function() {
  resolve_project_paths()$data
}

get_output_dir <- function() {
  resolve_project_paths()$output
}

initialize_paths <- function() {
  paths <- resolve_project_paths()
  cat("Data path:", paths$data, "\n")
  cat("Output dir:", paths$output, "\n")
  return(list(data_path = paths$data, output_dir = paths$output))
}
