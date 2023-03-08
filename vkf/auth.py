import os
import http.server
import webbrowser
import socketserver


VK_API_ID = os.environ.get("VK_API_ID")  # also known as client_id
REDIRECT_URI = "http://127.0.0.1:3434"


class ServerClose(KeyboardInterrupt):
    pass


class GetTokenServer(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        path: str = self.path
        print("path", path)

        self.send_response(code=200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        if path.startswith("/?code="):
            code = path.split("/?code=")[-1]
            print("parsed code", code)

            self.wfile.write(
                "<h1>Auth complete. You can close this tab</h1>".encode(),
            )
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
        "&response_type=code"
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
