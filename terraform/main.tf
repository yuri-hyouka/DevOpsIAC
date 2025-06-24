terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region  = "us-east-1"
}


resource "aws_instance" "app_server" {
  #subnet_id     = aws_subnet.main.id
  key_name      = "iac-alura"
  ami           = "ami-0779caf41f9ba54f0"
  instance_type = "t2.micro"

  tags = {
    Name = "Terraform Ansible Python"
  }
}



/*
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "main-vpc"
  }
}

resource "aws_subnet" "main" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"
  availability_zone = "us-east-1a"

  tags = {
    Name = "main-subnet"
  }
}
*/


/*
user_data = <<-EOF
                #!/bin/bash
                cd /home/admin
                echo "<h1>Mensagem a ser mostrada</h1>" > index.html
                nohup busybox httpd -f -p 8080 &
                EOF
*/