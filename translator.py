import requests
import json
from flask import Flask, request, jsonify

app = Flask(__name__)
key = "YOUR KEY GOES HERE" 
target = "en"
url = "https://translation.googleapis.com/language/translate/v2"

def build_body(input: str) -> json:
    """
    Builds body of POST for Google translate API. Takes a string of text.
    Returns: json body of HTTP POST 
    """
    data = {
        'q': input,
        'target': target,
        'format': 'text',
        'key': key
    }
    return data

def translate(body: json) -> str:
    """
    Takes a json body for an HTTP POST to be sent to the url defined
    by the url variable at the top of the file. 
    returns: translated string on success, 0 otherwise
    """
    response = requests.post(url, body)
    if response.status_code == 200:
        return response.json()['data']['translations'][0]['translatedText']
    else:
        return 0


@app.route('/route', methods=['POST'])
def googleTrans():
    """
    Uses Flask to communicate with program on localhost.
    Uses the build_body() and translate() functions to translate
    the input json.
    Takes input json in form of {"text": "STRING HERE"}.
    Returns: json in form of {"translation": "TRANSLATION HERE"}. On 
    failure returns error in form of {"error": "ERROR HERE"}
    """
    data = request.get_json()
    body = build_body(str(data.get("text")))
    translation = translate(body)
    if translation != 0:
        return jsonify({'translation': translation})
    else:
        return jsonify({'error': "Error: failed translation"}), 400
    

if __name__ == '__main__':
    app.run(port=5555)

