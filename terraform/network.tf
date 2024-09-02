resource "google_compute_network" "gencan" {
  name                    = "vpc-gencan"
  auto_create_subnetworks = false
}

resource "google_compute_router" "nat-router-us-central1" {
  name    = "nat-router-us-central1"
  network = google_compute_network.gencan.name
}

resource "google_compute_router_nat" "nat-config" {
  name                               = "nat-config"
  router                             = google_compute_router.nat-router-us-central1.name
  nat_ip_allocate_option             = "AUTO_ONLY"
  source_subnetwork_ip_ranges_to_nat = "ALL_SUBNETWORKS_ALL_IP_RANGES"
}

resource "google_compute_subnetwork" "gencan-uc1-dev" {
  name = "internal-gencan-uc1-dev"

  ip_cidr_range = "172.16.0.0/24"
  purpose       = "PRIVATE"
  stack_type    = "IPV4_ONLY"
  network       = google_compute_network.gencan.name
}

resource "google_compute_subnetwork" "gencan-uc1-stage" {
  name = "internal-gencan-uc1-stage"

  ip_cidr_range = "172.16.1.0/24"
  purpose       = "PRIVATE"
  stack_type    = "IPV4_ONLY"
  network       = google_compute_network.gencan.name
}

resource "google_compute_subnetwork" "gencan-uc1-prod" {
  name = "internal-gencan-uc1-prod"

  ip_cidr_range = "172.16.2.0/24"
  purpose       = "PRIVATE"
  stack_type    = "IPV4_ONLY"
  network       = google_compute_network.gencan.name
}

resource "google_compute_global_address" "private_service_addresses" {
  name          = "private-service-ip-addresses"
  purpose       = "VPC_PEERING"
  address_type  = "INTERNAL"
  address       = "172.31.255.0"
  prefix_length = "24"
  network       = google_compute_network.gencan.id
}

resource "google_service_networking_connection" "google_private_services_connection" {
  network                 = google_compute_network.gencan.id
  service                 = "servicenetworking.googleapis.com"
  reserved_peering_ranges = [google_compute_global_address.private_service_addresses.name]
}
