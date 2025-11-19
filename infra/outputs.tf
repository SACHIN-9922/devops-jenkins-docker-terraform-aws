output "jenkins_public_ip" {
  value = aws_instance.jenkins.public_ip
}

output "jenkins_public_dns" {
  value = aws_instance.jenkins.public_dns
}

output "rds_endpoint" {
  value = aws_db_instance.postgres.address
}

output "s3_bucket_name" {
  value = aws_s3_bucket.artifacts.bucket
}
