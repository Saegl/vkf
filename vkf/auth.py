"""
This modules can load access token through webbrowser
It uses vk.com implicit flow and opens server on localhost
to catch token.

Flow:
1. Open new tab at https://oauth.vk.com/authorize
2. Get redirect to `localhost/#...` with access token in fragment identifier
3. Use js to send access token from fragment identfier to `localhost/?...`
4. Catch access token with localhost server and show it
"""

import http.server
import pathlib
import socketserver
import webbrowser

import pydantic

from vkf.api import VK_API_VERSION
from vkf.config import logger


STATIC_DIR = pathlib.Path(__file__).parent / "static"


class AuthResponse(pydantic.BaseModel):
    access_token: str
    expires_in: int
    user_id: int


class ServerClose(KeyboardInterrupt):
    pass


def parse_auth_response(path: str) -> AuthResponse:
    params_string = path.split("/?")[-1]
    params = params_string.split("&")

    data = {}
    for param in params:
        key, value = param.split("=")
        data[key] = value

    # You don't need to manually convert str to int
    # pydantic will do it itself
    # that is why `# type: ignore` is here
    return AuthResponse(**data)  # type: ignore


class GetTokenServer(http.server.BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == "/":
            self.vk_redirect_handler()
        elif self.path.startswith("/?"):
            self.access_token_handler()

    def vk_redirect_handler(self) -> None:
        self.send_response(code=200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        with open(STATIC_DIR / "vk_redirect.html", mode="rb") as f:
            self.wfile.write(f.read())

    def access_token_handler(self) -> None:
        try:
            auth_data = parse_auth_response(self.path)
        except pydantic.ValidationError:
            print("Cannot parse access token, did you accept vk oauth?")
            logger.critical("Access token is not parsed")

        print("Access token successfully catched and parsed")
        print(f"Access token: {auth_data.access_token}")
        print(f"Expires in: {auth_data.expires_in} seconds")
        print(f"UserID: {auth_data.user_id}")
        logger.info("Access token successfully catched and parsed")

        raise ServerClose()


def web_auth(client_id: int, host: str = "127.0.0.1", port: int = 3434) -> None:
    redirect_uri = f"http://{host}:{port}"
    url = (
        "https://oauth.vk.com/authorize"
        f"?client_id={client_id}"
        "&display=page"
        f"&redirect_uri={redirect_uri}"
        "&scope=friends"
        "&response_type=token"
        f"&v={VK_API_VERSION}"
    )

    with socketserver.TCPServer((host, port), GetTokenServer) as httpd:
        logger.info(f"Acquire host and port successfully {(host, port)}")

        webbrowser.open_new_tab(url)
        logger.info("Open new browser tab")
        try:
            logger.info("Start serving token catcher at localhost")
            httpd.serve_forever()
        except ServerClose:
            logger.info("Server closed")
