resource "google_container_cluster" "dev" {
  name = "gencan-dev"

  location                 = "us-central1"
  enable_autopilot         = true
  enable_l4_ilb_subsetting = true

  network    = google_compute_network.gencan.id
  subnetwork = google_compute_subnetwork.gencan-uc1-dev.id

  deletion_protection = false
}
