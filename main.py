import requests
import json
import os



# Define the API endpoint and headers
url = "https://texttospeech.googleapis.com/v1/text:synthesize"
headers = {
    "Content-Type": "application/json",
    "X-Goog-User-Project": os.getenv("GOOGLE_PROJECT_ID"),
    "Authorization": f"Bearer {os.getenv('GOOGLE_API_KEY')}",
}

# Define the request payload
data = {
    "input": {
        "markup": "Movies, oh my gosh, I just just absolutely love them. They are like time machines taking you to different worlds and landscapes, and um, and I just can\u0027t get enough of it."
    },
    "voice": {
        "languageCode": "en-US",
        "name": "en-US-Chirp3-HD-Achernar"
    },
    "audioConfig": {
        "audioEncoding": "LINEAR16"
    }
}

# Make the POST request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Print the response
print(response.status_code)
print(response.json())