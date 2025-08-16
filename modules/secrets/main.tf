resource "aws_secretsmanager_secret" "api_key" {
  name = "football-api-key"
}

resource "aws_secretsmanager_secret_version" "api_key_value" {
  secret_id     = aws_secretsmanager_secret.api_key.id
  secret_string = "no_key_needed" # Placeholder value
}