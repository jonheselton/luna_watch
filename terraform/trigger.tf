resource "google_cloudbuildv2_repository" "repo_luna_watch" {
  name              = "my-repo"
  parent_connection = google_cloudbuildv2_connection.my_connection.id
  remote_uri        = "https://github.com/jonheselton/luna_watch.git"
}

resource "google_cloudbuild_trigger" "repo-trigger" {
  location = "us-central1"

  repository_event_config {
    repository = google_cloudbuildv2_repository.repo_luna_watch.id
    pull_request {
      branch          = "main"
      comment_control = "COMMENTS_ENABLED"
    }
  }
  include_build_logs = "INCLUDE_BUILD_LOGS_WITH_STATUS"
  filename           = "cloudbuild.yaml"
  service_account    = "projects/affable-berm-432217-i2/serviceAccounts/478491545012-compute@developer.gserviceaccount.com"
}

