# 1. Define the trust policy for the EC2 service to assume this role
data "aws_iam_policy_document" "assume_role_policy" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["ec2.amazonaws.com"]
    }
  }
}

# 2. Create the IAM Role
resource "aws_iam_role" "ec2_s3_read_only_role" {
  name               = "ec2-s3-read-only-role"
  assume_role_policy = data.aws_iam_policy_document.assume_role_policy.json
  
  tags = {
    Terraform = "true"
    Project   = "EC2-Instance-Role"
  }
}

# 3. Define the permissions policy (e.g., S3 Read-Only)
data "aws_iam_policy_document" "s3_read_only_policy_doc" {
  statement {
    effect = "Allow"
    actions = [
      "s3:GetObject",
      "s3:ListBucket",
    ]
    resources = [
      "arn:aws:s3:::your-bucket-name",      # ARN for the bucket itself
      "arn:aws:s3:::your-bucket-name/*",    # ARN for objects within the bucket
    ]
  }
}

# 4. Attach the inline policy to the role
resource "aws_iam_role_policy" "ec2_s3_read_only_policy" {
  name   = "ec2-s3-read-only-policy"
  role   = aws_iam_role.ec2_s3_read_only_role.id
  policy = data.aws_iam_policy_document.s3_read_only_policy_doc.json
}


# 5. Create the instance profile to be attached to the EC2 instance
resource "aws_iam_instance_profile" "ec2_profile" {
  name = "ec2-instance-profile"
  role = aws_iam_role.ec2_s3_read_only_role.name
}


resource "aws_instance" "app_server" {
  ami           = "ami-0c55b159cbfafe1f0" # Example AMI ID, change to your desired one
  instance_type = "t2.micro"

  # Attach the instance profile created above
  iam_instance_profile = aws_iam_instance_profile.ec2_profile.name

  tags = {
    Name = "AppServer"
  }
}