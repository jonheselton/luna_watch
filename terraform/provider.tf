variable "GCP_PROJECT_ID" {}
variable "github_cloud_build_oauth_token" {
    description = "oauth toekn to authentice to the GH Cloud Build app"
    type = string
    sensitive = true
    default = "value"
    
}

provider "google" {
  project = var.GCP_PROJECT_ID
  region  = "us-central1"
  zone    = "us-central1-c"
}
