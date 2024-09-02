resource "google_sql_database" "luna_watch_db" {
  name     = "luna_watch_db"
  instance = google_sql_database_instance.luna_watch_db_instance.name
}

resource "google_sql_database_instance" "luna_watch_db_instance" {
  depends_on       = [google_service_networking_connection.google_private_services_connection]
  name             = "luna-watch-database-instance"
  database_version = "POSTGRES_15"
  settings {
    tier = "db-f1-micro"
    ip_configuration {
      ipv4_enabled                                  = false
      private_network                               = google_compute_network.gencan.self_link
      enable_private_path_for_google_cloud_services = true
    }
  deletion_protection_enabled = "false"
  }
}
