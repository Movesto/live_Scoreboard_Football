variable "subnet_id" {
  description = "The ID of the subnet to launch the instance in."
  type        = string
}

variable "security_group_id" {
  description = "The ID of the security group to attach."
  type        = string
}

variable "iam_instance_profile_name" {
  description = "The name of the IAM instance profile to attach."
  type        = string
}