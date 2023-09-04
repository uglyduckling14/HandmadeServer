# Assn1



## Requirements:

### Architecture:

Server -> passes Bytes -> Encoder
Encoder -> passes Request Obj -> Server
Server -> sends request -> Router
Router -> sends request -> Endpoint
Endpoint -> sends response -> Router
Router -> sends response -> Server
Server -> sends response -> Encoder
Encoder -> returns bytes -> Server

### Parsing:

Implement a socket and turn bytes into data using parse/request.

Middleware will return response.

Parser will turn response into valid HTTP string

### Pseudocode

Static files:
    .js
        will print something to console
    .css
        will style html files
Templates:
    index
        * css
        * links
        * name
        * purpose
        * js
    about
        * about yourself
        * css
    experience
        * last three jobs + time
    projects page
        * 3 programming projects
server:
    receives request-> convert to request object
    request object-> sent to middleware
    middleware -> parse to response
    return response string
    send response as bytes
response:
    contains version, code, reason, headers, text
    headers:
        servername
        date
        connection: 
        cache-control
        content length
        content-type mime types
        location: only for 301 responses
request:
    contains headers, text, method, uri and version
middleware:
    must be in middlware factory style
    logs request/response
    gets specific files by name
        - send correct content-type header
    call endpoint that belongs to uri
        return endpoint
        else
            return endpoint not found
endpoint:
    fetch file belonging to each uri

