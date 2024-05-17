import os
import time
from twilio.rest import Client
from flask import Flask, request
from dotenv import load_dotenv
import ast

load_dotenv()
app = Flask(__name__)

#Environment Variables
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
from_number = os.getenv("FROM_NUMBER")
numbers = os.getenv("TO_NUMBERS")
to_numbers = ast.literal_eval(numbers)

@app.route('/alert', methods=['POST'])
def handle_alert():
    data = request.json
    alert_message = data['alerts'][0]['annotations']['description']

    for to_number in to_numbers:
        print("Calling:", to_number)
        client = Client(account_sid, auth_token)
        call = client.calls.create(
            # You can change the language: https://www.twilio.com/docs/voice/twiml/say/text-speech#available-voices-and-languages
            twiml='<Response><Say voice="woman" language="pt-BR"> Host Down! ' + alert_message + '</Say></Response>',
            to=to_number,
            from_=from_number
        )
        time.sleep(10)
        print(f"Calling to {to_number}. SID: {call.sid}")

    return 'All done!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
