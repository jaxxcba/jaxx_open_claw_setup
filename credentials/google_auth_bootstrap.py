#!/usr/bin/env python3
import json
import os
from pathlib import Path

from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/gmail.modify",
    # Optional explicit send scope (uncomment if you added it in Data access)
    # "https://www.googleapis.com/auth/gmail.send",
]

BASE = Path.home() / ".openclaw" / "credentials"
CLIENT_FILE = BASE / "google_oauth_client.json"
TOKEN_FILE = BASE / "google_token.json"

def main():
    BASE.mkdir(parents=True, exist_ok=True)

    if not CLIENT_FILE.exists():
        raise SystemExit(f"Missing OAuth client file: {CLIENT_FILE}")

    flow = InstalledAppFlow.from_client_secrets_file(str(CLIENT_FILE), SCOPES)
    creds = flow.run_local_server(port=0, prompt="consent")

    # Basic sanity check: refresh token should exist after first consent
    if not getattr(creds, "refresh_token", None):
        print("WARNING: No refresh_token received. If you have authorized before, revoke access and retry.")
        print("Revoke at: https://myaccount.google.com/permissions")
        # still save what we got
    data = json.loads(creds.to_json())
    TOKEN_FILE.write_text(json.dumps(data, indent=2))
    print(f"Saved token to: {TOKEN_FILE}")

if __name__ == "__main__":
    main()