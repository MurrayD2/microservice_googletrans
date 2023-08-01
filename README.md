# English Google Translator Microservice API

This is a simple application that handles most of the work of interacting with Google Translate's API. It takes a string from the user in any language and translates it to English.
To run, this application uses the requests, json, and flask packages. Ensure that your Python environment has these packages and that they are up-to-date before running.
The application requires that you provide your own Google Authentication key to use the Google Translate API. This will require an active Google Cloud account and that you have set up your account to use the Google Translate API.
Enter replace the text "YOUR KEY GOES HERE" with your authentication key in line 6:
```
key = "YOUR TEXT GOES HERE"
```

## Endpoint

**Translate text to English**

- Path: `/route`
- Method: `POST`
- Request Content-Type: `application\json`
- Request Content-Type `application\json`

### Request

The app requires that the request contain a body with one property, 'text':
- `text` (required): A string of text in any language.

Example request body:
```
{
"text": "這不是英文"
}
```

### Response

The app responds with a body that containts one propety, 'translation':
- `translation`: A string of English text upon a succesful translation. Accuracy is in no way guaranteed.

Example response body:
```
{
"translation": "this is not English"
}
```

### Error Handling

If translation fails for any reason, the app will respond with an error message and a status of 400. 
There are several reasons a translation could fail - network issue, Google authentication key error, etc. The error message does not distinguish between these various potential errors.

Example of Error response:
```
{
"error": "Error: failed translation"
}
```

## Local Development

To run the application locally, execute the below command in a terminal from the folder where you have saved the file:
```
python3 translator.py
```

The application uses http://localhost:5555 to operate.

## UML
```
+-----------------------------------+
|          Flask Application        |
+-----------------------------------+
| -app: Flask                       |
| -key: string                      |
| -target: string                   |
| -url: string                      |
+-----------------------------------+
| +translate(body: json): string    |
+-----------------------------------+
| +build_body(input: str): json     |
+-----------------------------------+
| +googleTrans()                    |
+-----------------------------------+
```
