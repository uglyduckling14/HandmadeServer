# Assn1



## Requirements:

### Architecture:

Should follow lesson 1.4

### Parsing:

Implement a socket and turn bytes into data using parse/request.

Example:

class Request:
    def __init__(
        self,
        method, #string
        uri, #string
        version, #string
        text, #string
        headers, #dict, the keys are the header names and values are the header values
    ):
        self.method = method
        self.uri = uri
        self.version = version
        self.text = text
        self.headers = headers

Middleware will return response.

Example:

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
        self.code = code
        self.reason = reason
        self.headers = headers
        self.text = text

Parser will turn response into valid HTTP string

Example:

HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 575
Connection: close
Cache-Control: no-cache
Server: Joseph's Server
Date: 2023-07-19 18:53:53.844846+00:00
