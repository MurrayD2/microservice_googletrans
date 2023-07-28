# Demo program for using the microservice.
# Start up the microservice in one terminal, then
# run this in another to test.

import requests

def test_translate(text: str) -> str:
    """
    Uses requests to send a json message to the designate 
    port on the local machine for inter-process communication.
    Takes a string and returns a translated string.
    text: input string
    returns: translated string
    """
    url = "http://localhost:5555/route"
    payload = {
        "text": str(text)
    }
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return response.json()['translation']
    else:
        return "Error: ", response.json()['error']


if __name__ == "__main__":
    notEnglish = "這個不是英文"
    print(test_translate(notEnglish))
    