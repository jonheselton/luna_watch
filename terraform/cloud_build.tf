resource "google_secret_manager_secret" "github_token_secret" {

    secret_id = "GH_OAuth"
    replication {
        user_managed {
            replicas {
                location = "us-central1"
            }
            replicas {
                location = "us-east1"
            }
        }
    }
}

resource "google_secret_manager_secret_version" "github_token_secret_version" {
    secret = google_secret_manager_secret.github_token_secret.id
    secret_data = var.github_cloud_build_oauth_token

}

data "google_iam_policy" "serviceagent_secretAccessor" {
    binding {
        role = "roles/secretmanager.secretAccessor"
        members = ["serviceAccount:service-478491545012@gcp-sa-cloudbuild.iam.gserviceaccount.com"]
    }
}

resource "google_secret_manager_secret_iam_policy" "policy" {

  secret_id = google_secret_manager_secret.github_token_secret.secret_id
  policy_data = data.google_iam_policy.serviceagent_secretAccessor.policy_data
}

resource "google_cloudbuildv2_connection" "my_connection" {
    location = "us-central1"
    name = "jonheselton-github"

    github_config {
        app_installation_id = "53886057"
        authorizer_credential {
            oauth_token_secret_version = google_secret_manager_secret_version.github_token_secret_version.id
        }
    }
    depends_on = [google_secret_manager_secret_iam_policy.policy]
}
