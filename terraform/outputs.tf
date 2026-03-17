output "api_endpoint" {
  description = "API Gateway endpoint URL"
  value       = "${aws_apigatewayv2_stage.stage.invoke_url}${var.project_name}"
}

output "lambda_function_name" {
  description = "Lambda function name"
  value       = aws_lambda_function.analyzer.function_name
}

output "curl_example" {
  description = "Example curl command to test the API"
  value       = <<-EOT
    curl -X POST ${aws_apigatewayv2_stage.stage.invoke_url}${var.project_name} \
      -H "Content-Type: application/json" \
      -d '{"logs": "ERROR 2025-01-16 12:00:00 Database timeout"}'
  EOT
}
