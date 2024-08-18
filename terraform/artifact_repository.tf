resource "google_artifact_registry_repository" "repo_luna_watch" {
  location      = "us-central1"
  repository_id = "gencan-luna-watch"
  description   = "gencan repository for the luna_watch web app"
  format        = "DOCKER"
}


