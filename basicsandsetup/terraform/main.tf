# Define the Terraform configuration
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"  # Use the Google provider
      version = "7.8.0"  # Specify the provider version
    }
  }
}

# Configure the Google Cloud provider
provider "google" {
  project     = var.project_id  # Project ID from variables
  credentials = file(var.credentials)  # Path to credentials file
  region      = var.region  # Region from variables
}

# Create a Google Cloud Storage bucket
resource "google_storage_bucket" "demo-bucket" {
  name          = var.gcs_bucket_name  # Bucket name from variables
  location      = var.location  # Location from variables
  force_destroy = true  # Allow deletion of non-empty buckets

  # Define lifecycle rules for the bucket
  lifecycle_rule {
    condition {
      age = 1  # Delete objects older than 1 day
    }
    action {
      type = "Delete"  # Delete action
    }
  }

  lifecycle_rule {
    condition {
      age = 1  # Abort incomplete uploads older than 1 day
    }
    action {
      type = "AbortIncompleteMultipartUpload"  # Abort action
    }
  }
}

resource "google_bigquery_dataset" "demo_dataset" {
  dataset_id = var.bq_dataset_name
  location   = var.location
}

