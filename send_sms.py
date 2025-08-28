import os
from twilio.rest import Client

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
sms_from = os.getenv("TWILIO_SMS_FROM")  # Twilio phone number
sms_to = os.getenv("SMS_TO")             # Recipient number

if not all([account_sid, auth_token, sms_from, sms_to]):
    raise SystemExit("Missing required environment variables. Check your env.example.txt.")

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello! This is a test SMS from Python via Twilio.",
    from_=sms_from,
    to=sms_to
)

print(f"✅ SMS sent successfully. SID: {message.sid}")
