# Helper functions for path resolution in R scripts
# Works when run from project root or from scripts/r/

resolve_project_paths <- function(data_filename = "Cybersecurity_attacks.csv",
                                  data_subdir = "data",
                                  viz_subdir = "visualizations",
                                  results_subdir = "results") {
  candidates <- list(
    list(
      data = file.path(data_subdir, data_filename),
      viz = viz_subdir,
      results = results_subdir
    ),
    list(
      data = file.path("..", "..", data_subdir, data_filename),
      viz = file.path("..", "..", viz_subdir),
      results = file.path("..", "..", results_subdir)
    ),
    list(
      data = file.path("..", data_subdir, data_filename),
      viz = file.path("..", viz_subdir),
      results = file.path("..", results_subdir)
    )
  )

  for (candidate in candidates) {
    if (file.exists(candidate$data)) {
      if (!dir.exists(candidate$viz)) {
        dir.create(candidate$viz, recursive = TRUE, showWarnings = FALSE)
      }
      if (!dir.exists(candidate$results)) {
        dir.create(candidate$results, recursive = TRUE, showWarnings = FALSE)
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
