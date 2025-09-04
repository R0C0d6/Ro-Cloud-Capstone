variable "aws_region" {
  description = "The AWS region to deploy the resources in."
  type        = string
  default     = "us-east-1"
}

variable "request_bucket_name" {
  description = "The name of the S3 bucket for input files."
  type        = string
  default     = "roland-capstone-bucket-input"
}

variable "response_bucket_name" {
  description = "The name of the S3 bucket for output files."
  type        = string
  default     = "roland-capstone-bucket-output"
}

variable "lambda_function_name" {
  description = "The name of the Lambda function."
  type        = string
  default     = "capproject-translator-lambda"
}
