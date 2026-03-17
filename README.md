# AI Log Analyzer

Serverless AI-powered log analysis tool using Claude API and AWS infrastructure.

## Overview

This project automatically analyzes application logs using Claude AI (Anthropic) and provides:
- Summary of issues found
- Severity classification (critical/warning/info)
- Recommended actions

Built with **AWS Lambda**, **API Gateway**, and deployed via **Terraform** (Infrastructure as Code).

## Architecture
```
User Request (HTTP POST)
         |
         v
    API Gateway
         |
         v
    AWS Lambda (Python 3.12)
         |
         v
    Claude API (Anthropic)
         |
         v
    JSON Response (AI Analysis)
```
## Tech Stack

- **Cloud**: AWS (Lambda, API Gateway, IAM)
- **AI**: Claude Sonnet 4 (Anthropic)
- **Language**: Python 3.12
- **IaC**: Terraform
- **Libraries**: anthropic, boto3

## Project Structure
```
ai-log-analyzer/
├── lambda/
│ ├── lambda_function.py # Main Lambda handler
│ └── (anthropic libraries)
├── terraform/
│ ├── main.tf # Infrastructure definition
│ ├── variables.tf # Configuration variables
│ ├── outputs.tf # API endpoint outputs
│ └── terraform.tfvars # Variable values (not in repo)
└── README.md
```
## Quick Start

### Prerequisites

- AWS Account with CLI configured
- Terraform >= 1.0
- Anthropic API key

### Deployment

1. Clone repository
```
git clone https://github.com/marand85/ai-log-analyzer
cd ai-log-analyzer
```
2. Configure variables
```
cd terraform
cp terraform.tfvars.example terraform.tfvars
Edit terraform.tfvars with your Anthropic API key
```
3. Deploy infrastructure
```
terraform init
terraform apply
```
4. Get API endpoint
```
terraform output api_endpoint
```
## Usage

### Test the API
```
curl -X POST https://your-api-endpoint/ai-log-analyzer \
  -H "Content-Type: application/json" \
  -d '{"logs": "ERROR 2025-01-16 12:00:00 Database connection timeout\nCRITICAL Payment processing failed"}'
```
### Example Response
```
{
  "status": "success",
  "analysis": "## Log Analysis Report\n\n### Summary\n- Database timeout\n- Payment failure\n\n### Severity: CRITICAL\n\n### Recommended Actions\n- Check database connectivity\n- Review payment gateway status..."
}
```
## Key Features

- Serverless - No infrastructure management
- AI-Powered - Claude Sonnet 4 for intelligent analysis
- Infrastructure as Code - Full Terraform deployment
- Scalable - Auto-scaling Lambda + API Gateway
- Cost-Effective - Pay only for actual usage

## Development

### Local Testing

Package Lambda dependencies:
```
cd lambda
pip install anthropic -t .
```
Update code (use your preferred editor):
```
nano lambda_function.py
# or: code lambda_function.py
# or: vim lambda_function.py
```
Redeploy:
```
cd ../terraform
terraform apply
```
## Security

- API key stored as encrypted environment variable
- IAM roles with least privilege access
- HTTPS-only API endpoint
- No authentication on API (add API Gateway authorizer for production)

## Cost Estimate

| Service     | Usage                   |     Cost     |
|-------------|-------------------------|--------------|
| Lambda      | 1000 requests/month     |    ~$0.20    |
| API Gateway | 1000 requests/month     |    ~$0.01    |
| Claude API  | 1000 requests           |    ~$3.00    |
| **Total**   |                         | **~$3.21/month** |

Based on Free Tier + typical usage

## Future Enhancements

- Add authentication (API Gateway Authorizer)
- Store analysis results in DynamoDB
- Add CloudWatch dashboards
- Support multiple AI models (GPT-4, etc.)
- Batch log processing

## Author

Mariusz Andrzejewski
AI Platform Engineer

- GitHub: https://github.com/marand85/ai-log-analyzer  

## License

MIT License
