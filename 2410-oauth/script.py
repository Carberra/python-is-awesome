import hashlib
import json
import os
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qsl, urlencode

import requests

SCOPES = [
    "https://www.googleapis.com/auth/yt-analytics.readonly",
    "https://www.googleapis.com/auth/yt-analytics-monetary.readonly",
    "openid",
    "https://www.googleapis.com/auth/userinfo.profile",
    "https://www.googleapis.com/auth/userinfo.email",
]
HOST = "localhost"
PORT = 8080


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.server: "Server"
        self.server.query_params = dict(parse_qsl(self.path.split("?")[1]))
        self.wfile.write(b"<h1>Authorised!</h1>")


class Server(HTTPServer):
    def __init__(self, host: str, port: int) -> None:
        super().__init__((host, port), RequestHandler)
        self.query_params: dict[str, str] = {}


def authorise(secrets: dict[str, str]) -> dict[str, str]:
    redirect_uri = f"{secrets['redirect_uris'][0]}:{PORT}"

    params = {
        "response_type": "code",
        "client_id": secrets["client_id"],
        "redirect_uri": redirect_uri,
        "scope": " ".join(SCOPES),
        "state": hashlib.sha256(os.urandom(1024)).hexdigest(),
        "access_type": "offline",
    }
    url = f"{secrets['auth_uri']}?{urlencode(params)}"
    if not webbrowser.open(url):
        raise RuntimeError("Failed to open browser")

    server = Server(HOST, PORT)
    try:
        server.handle_request()
    finally:
        server.server_close()

    if params["state"] != server.query_params["state"]:
        raise RuntimeError("Invalid state")

    code = server.query_params["code"]

    params = {
        "grant_type": "authorization_code",
        "client_id": secrets["client_id"],
        "client_secret": secrets["client_secret"],
        "redirect_uri": redirect_uri,
        "code": code,
    }
    with requests.post(
        secrets["token_uri"],
        data=params,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    ) as response:
        if response.status_code != 200:
            raise RuntimeError("Failed to authorise")

        return response.json()


def check_access_token(access_token: str) -> dict[str, str]:
    with requests.post(
        f"https://www.googleapis.com/oauth2/v3/tokeninfo?access_token={access_token}"
    ) as response:
        if response.status_code != 200:
            raise RuntimeError("Failed to check access token")

        return response.json()


def refresh_token(secrets: dict[str, str], refresh_token: str) -> dict[str, str]:
    params = {
        "grant_type": "refresh_token",
        "client_id": secrets["client_id"],
        "client_secret": secrets["client_secret"],
        "refresh_token": refresh_token,
    }
    with requests.post(
        secrets["token_uri"],
        data=params,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    ) as response:
        if response.status_code != 200:
            raise RuntimeError("Failed to refresh token")

        return response.json()


if __name__ == "__main__":
    secrets = json.loads(Path("secrets.json").read_text())["installed"]

    tokens = authorise(secrets)
    print(f"Tokens: {tokens}")

    token_info = check_access_token(tokens["access_token"])
    print(f"Token info: {token_info}")

    refreshed_tokens = refresh_token(secrets, tokens["refresh_token"])
    print(f"\nRefreshed tokens: {refreshed_tokens}")
