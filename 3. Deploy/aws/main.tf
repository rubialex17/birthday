resource "aws_db_instance" "birthday" {
  allocated_storage    = 20
  storage_type         = "gp2"
  engine               = "postgres"
  engine_version       = "12.7"
  instance_class       = "db.t2.micro"
  username             = "mydbuser"
  password             = "mypassword"
  parameter_group_name = "default.postgres12"
  skip_final_snapshot  = true
}

output "db_endpoint" {
  value = aws_db_instance.birthday.endpoint
}
