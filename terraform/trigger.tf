resource "google_cloudbuildv2_repository" "repo_luna_watch" {
  name = "my-repo"
  parent_connection = google_cloudbuildv2_connection.my_connection.id
  remote_uri = "https://github.com/jonheselton/luna_watch.git"
}

resource "google_cloudbuild_trigger" "repo-trigger" {
  location = "us-central1"

  repository_event_config {
    repository = google_cloudbuildv2_repository.repo_luna_watch.id
    pull_request {
      branch = "main"
    }
  }
  include_build_logs = "INCLUDE_BUILD_LOGS_WITH_STATUS"
  filename = "cloudbuild.yaml"
  service_account = "113479310004597445170"
}
# resource "google_cloudbuild_trigger" "luna-watch-trigger" {
#     name     = "luna-watch-build-on-pr"
#     filename = "cloudbuild.yaml"

#     github {
#             owner = "jonheselton"
#             name  = "luna_watch"
#             pull_request {
#                 branch = "^main$"
#             }
#     }

#     include_build_logs = "INCLUDE_BUILD_LOGS_WITH_STATUS"
# }
