# OIDC With Cognito and FastAPI

## Local execution
- Install `poetry` and `Python 3.12` on your machine. Make sure poetry is available on your PATH.
- In a terminal inside this directory, execute `poetry install`.
- Execute `poetry run python -m app.main` to start a local server.

## Cognito setup
- Make sure you have a working AWS Cognito User Pool available.
- Pass the configuration values as specified in `example.env` to a `.env` file in the root directory.

## Testing
- The easiest way to test the device flow is through the Swagger UI Docs. 
- Start up your server and go to `http://localhost:5050/docs`
- Authenticate using your Cognito client id and secret.

### Device flow
- Execute Get Device Token
- Copy and paste the verification URI in your browser
- Click confirm and authenticate
- Now the Get Jwt Token call will succeed.