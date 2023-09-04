
import socket, datetime
from request import Request
from response import Response

def parser(request):
    lines = request.split(b'\r\n')
    request_line = lines[0].decode("UTF-8")
    method, uri, version = request_line.split(' ')
    if(uri == '/'):
        uri = '/index.html'
    else:
        uri+= '.html'
    headers = {}
    text_start = 0
    for i in range(1, len(lines)):
        line = lines[i].decode("UTF-8")
        if not line.strip():
            text_start = i+1
            break
        key, value = line.split(': ', 1)
        headers[key] = value
    text = b'\r\n'.join(lines[text_start:])
    return Request(method, uri, version, text, headers)

def middleware_request(next):
    def middlware(my_input):
        # Do something with my_input (optional)
        print(f"Request received: {my_input.uri}")
        res = next(my_input) # call the next middleware in the chain
        # do something with res (optional)
        return res # don't forget this step!
    
    return middlware # don't forget this step!

def middleware_response(my_input):
    res = router(my_input.uri)
    print(f"Response sent: {res.version} {res.code} {res.reason}")
    encoded_response = encode_response(res)
    return encoded_response

def router(uri):
    if(uri == '/info.html'):
            con =open('templates/index.html', 'r', encoding='UTF-8')
            html = con.read()
            con.close()
            return Response(
                version="HTTP/1.1",
                code=301,
                reason="Moved Permanently",
                headers={
                    "Date": datetime.datetime.now(),
                    "Server": "Esper Server",
                    "Connection": "close",
                    "Cache-Control": "max-age=1",
                    "Location": "/about"
                },
                text= html
            )
    elif '.' in uri:
        res = response(uri)
        if(res == None):
            res = Response(
                version="HTTP/1.1",
                code=404,
                reason="Not Found",
                headers={
                    "Date": datetime.datetime.now(),
                    "Content-Type": "text/html",
                    "Server": "Esper Server",
                    "Connection": "close",
                    "Cache-Control": "max-age=1"
                },
                text=""
            )
        return res
    else:
        return Response(
            version="HTTP/1.1",
            code=404,
            reason="Not Found",
            headers={
                "Date": datetime.datetime.now(),
                "Content-Type": "text/html",
                "Server": "Esper Server",
                "Connection": "close",
                "Cache-Control": "max-age=1"
            },
            text=""
        )
    # Handle cases where the URI does not match any endpoint

def encode_response(response):
    http_response = f"{response.version} {response.code} {response.reason}\n"

    for key, value in response.headers.items():
        http_response += f"{key}: {value}\n"
    
    http_response += f"Content Length: {len(http_response)}"

    http_response += "\n"

    http_response += response.text

    return http_response

def response(file):
    response_text = f'templates{file}'
    try:
        with open(response_text, 'r', encoding='UTF-8') as file:
            content = file.read()
            file.close()
            response = Response(
            version="HTTP/1.1",
            code=200,
            reason="OK",
            headers={
                "Date": datetime.datetime.now(),
                "Content-Type": "text/html",
                "Server": "Esper Server",
                "Connection": "close",
                "Cache-Control": "max-age=1"
            },
            text=content
        )
            return response
    except FileNotFoundError as e:
        print(f"Error occurred: {e}")
        return None

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("127.0.0.1", 8000))
    s.listen()
    print("listening on port 8000")

    while True:
        connection, addr = s.accept()
        with connection:
            data = connection.recv(8192)

            request = parser(data)

            middleware_chain = middleware_request(middleware_response)
            response = middleware_chain(request)
            connection.send(bytes(response, "UTF-8"))
            break
    s.close()

