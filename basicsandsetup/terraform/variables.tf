variable "bq_dataset_name" {
  description = "My BQ Dataset Name"
  default     = "demo_dataset_terraform"
}

variable "gcs_bucket_name" {
  description = "The name of the GCS bucket"
  default     = "tonal-land-475120-v3-terrabucket"
  
}

variable "gcs_storage_class" {
  description = "The storage class for the GCS bucket"
  default     = "STANDARD"
}

variable "location" {
  description = "The location for GCP resources"
  default     = "US"
}

variable "project_id" {
  description = "The GCP project ID"
  default     = "tonal-land-475120-v3"
}
variable "region" {
  description = "region"
  default = "us-central1"
}

variable "credentials" {
  description = "key"
  default     = "/Users/rohanjhunjhunwala/Downloads/tonal-land-475120-v3-6a713a11bac9.json"
}