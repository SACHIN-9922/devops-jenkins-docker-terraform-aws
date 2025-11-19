variable "aws_region" {
  type = string
}

variable "project_name" {
  type = string
}

variable "instance_type" {
  type    = string
  default = "t3.small"
}

variable "ssh_public_key_path" {
  type = string
}

variable "allowed_ssh_cidr" {
  type    = string
  default = "0.0.0.0/0"
}

variable "db_username" {
  type = string
}

variable "db_password" {
  type      = string
  sensitive = true
}

variable "db_allocated_storage" {
  type    = number
  default = 20
}
