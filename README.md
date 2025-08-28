# Python SMS Sender (Twilio)

This project demonstrates how to send an SMS using Python and Twilio API.

## Steps
1. Copy `env.example.txt` to `.env` and fill in your credentials.
2. Load environment variables:
   ```bash
   source load_env.sh
   ```
3. Install Twilio library:
   ```bash
   pip install twilio
   ```
4. Run the script:
   ```bash
   python3 send_sms.py
   ```

## Notes
- You need a Twilio account and a phone number enabled for SMS.
- Phone numbers must be in **E.164 format** (e.g., +9198xxxxxxx).
- Twilio free trial accounts can only send to verified numbers.
