import json
import anthropic

def lambda_handler(event, context):
	# Get logs from request
	body = event.get('body', '')

	if isinstance(body, str) and body:
		try:
			body = json.loads(body)
		except json.JSONDecodeError:
			body = {'logs' : body}

	logs = body.get('logs', '') if isinstance(body, dict) else ''

	if not logs:
		return {
			'statusCode': 400,
			'headers': {'Content-Type': 'application/json'},
			'body': json.dumps({'error': 'No logs provided'})
		}

	# Call Claude API
	client = anthropic.Anthropic()

	message = client.messages.create(
		model="claude-sonnet-4-20250514",
		max_tokens=1024,
		messages=[
			{
				"role":"user",
				"content": f"""Analaze these application logs and provide:
1. Summary of issues found
2. Severity level (critical/warning/info)
3. Recommended actions

Logs:
{logs}"""
			}
		]
	)

	analysis = message.content[0].text

	return {
		'statusCode': 200,
		'headers': {'Content-Type': 'application/json'},
		'body': json.dumps({
			'status': 'success',
			'analysis': analysis
		})
	}
