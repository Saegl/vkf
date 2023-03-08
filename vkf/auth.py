import os
import http.server
import pathlib
import socketserver
import webbrowser

import pydantic


filepath = pathlib.Path(__file__).parent
VK_API_ID = os.environ.get("VK_API_ID")  # also known as client_id
REDIRECT_URI = "http://127.0.0.1:3434"


class AuthResponse(pydantic.BaseModel):
    access_token: str
    expires_in: int
    user_id: int


class ServerClose(KeyboardInterrupt):
    pass


class GetTokenServer(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        path: str = self.path

        self.send_response(code=200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        if path == "/":
            code = path.split("/?code=")[-1]
            print("parsed code", code)

            self.wfile.write(
                "<h1>Auth complete. You can close this tab</h1>".encode(),
            )
            self.wfile.write("<script>\n".encode())

            with open(filepath / "auth.js", mode="rb") as f:
                self.wfile.write(f.read())

            self.wfile.write("</script>\n".encode())

        elif path.startswith("/?"):
            params_string = path.split("/?")[-1]
            params = params_string.split("&")

            print("Path: ", path)
            print("Params string: ", params_string)
            print("Got params:", params)

            data = {}
            for param in params:
                print("Param: ", param)
                key, value = param.split("=")
                data[key] = value

            auth_data = AuthResponse(**data)
            print("AUTH data: ", auth_data)
            raise ServerClose()

        else:
            self.wfile.write(
                "<h1>Error when parsing token, try again</h1>".encode(),
            )


def web_auth():
    url = (
        "https://oauth.vk.com/authorize"
        f"?client_id={VK_API_ID}"
        "&display=page"
        f"&redirect_uri={REDIRECT_URI}"
        "&scope=friends"
        "&response_type=token"
        "&v=5.131"
    )

    with socketserver.TCPServer(("127.0.0.1", 3434), GetTokenServer) as httpd:
        print("Open new tab")
        webbrowser.open_new_tab(url)
        print("Tab opened")
        print("Start server")
        try:
            httpd.serve_forever()
        except ServerClose:
            print("complete!")
