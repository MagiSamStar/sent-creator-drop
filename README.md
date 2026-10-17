# Sent Creator Drop

A Python integration project demonstrating how to connect an application to the Sent messaging API and submit template-based messaging requests in sandbox mode.

## Overview

Sent Creator Drop accepts a content title from the user, passes it to a configured Sent message template, and displays the API response.

The project explores API integration, environment-based configuration, reusable Python modules, and error handling.

## Features

- Accepts a content title through terminal input.
- Loads credentials and configuration from environment variables.
- Sends template-based requests using the Sent Python SDK.
- Uses sandbox mode to validate requests without delivering real messages.
- Separates application flow from API communication.
- Handles common connection, rate-limit, API, and configuration errors.

## Tech Stack

- Python
- Sent Python SDK (`sentdm`)
- `python-dotenv`
- Sent messaging API

## Project Structure

```text
sent-creator-drop/
├── main.py
├── sent_client.py
├── test_sandbox.py
├── .env.example
├── .gitignore
└── README.md
```

## Setup

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install the dependencies:

   ```bash
   pip install sentdm python-dotenv
   ```

4. Create a `.env` file using `.env.example` as a guide.
5. Add your own Sent API key, template ID, and authorized test number.
6. Run the application:

   ```bash
   python main.py
   ```

## Configuration

The application expects these environment variables:

- `SENT_DM_API_KEY`
- `SENT_TEMPLATE_ID`
- `SENT_TEST_PHONE`

Keep `.env` out of version control. Never commit API keys or private credentials.

## Sandbox Safety

The application currently uses sandbox mode. Requests validate the integration without delivering real messages. A queued sandbox response does not mean a real notification was delivered.

## Learning Goals

This project demonstrates practical experience with:

- API client initialization and request construction.
- Environment variables and secret management.
- Python functions, modules, imports, and return values.
- Exception handling and API response inspection.
- Building and documenting a small integration from the ground up.

## Current Status

Working prototype. Sandbox integration verified. Live message delivery is intentionally not enabled.
