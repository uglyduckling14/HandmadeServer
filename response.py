class Response:
    def __init__(
            self,
            version, #string
            code, #number
            reason, #string
            headers, #dict, the keys are the header names and values are the header values 
            text, #string
    ):
        self.version = version
        self.code = code # code num
        self.reason = reason # Not found /OK etc
        self.headers = headers
        self.text = text
# HTTP/1.1 200 OK
# Content-Type: text/html
# Content-Length: 575
# Connection: close
# Cache-Control: no-cache
# Server: Joseph's Server
# Date: 2023-07-19 18:53:53.844846+00:00
