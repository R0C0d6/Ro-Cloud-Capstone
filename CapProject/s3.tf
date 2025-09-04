resource "aws_s3_bucket" "input_bucket" {
  bucket = var.request_bucket_name

  tags = {
    Name = "CapProject Input Bucket"
  }
}

resource "aws_s3_bucket_lifecycle_configuration" "input_bucket_lifecycle" {
  bucket = aws_s3_bucket.input_bucket.id

  rule {
    id     = "log"
    status = "Enabled"

    filter {}

    transition {
      days          = 30
      storage_class = "STANDARD_IA"
    }

    expiration {
      days = 365
    }

    abort_incomplete_multipart_upload {
      days_after_initiation = 7
    }
  }
}

resource "aws_s3_bucket" "output_bucket" {
  bucket = var.response_bucket_name

  tags = {
    Name = "CapProject Output Bucket"
  }
}

resource "aws_s3_bucket_lifecycle_configuration" "output_bucket_lifecycle" {
  bucket = aws_s3_bucket.output_bucket.id

  rule {
    id     = "log"
    status = "Enabled"

    filter {}

    transition {
      days          = 30
      storage_class = "STANDARD_IA"
    }

    expiration {
      days = 365
    }

    abort_incomplete_multipart_upload {
      days_after_initiation = 7
    }
  }
}
