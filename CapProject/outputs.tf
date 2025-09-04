output "input_bucket_name" {
  description = "The name of the S3 bucket for input files."
  value       = aws_s3_bucket.input_bucket.bucket
}

output "output_bucket_name" {
  description = "The name of the S3 bucket for output files."
  value       = aws_s3_bucket.output_bucket.bucket
}
