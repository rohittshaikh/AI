import http.server
import ssl
host="localhost"
port=4443
sd=(host,port)

httpd=http.server.HTTPServer(
    sd,http.server.SimpleHTTPRequestHandler)

context=ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(
    c="server.crt",
    k="server.key")

httpd.socket=context.wrap_socket(
    httpd.socket,
    server_side=True)

print("server started")
print("open : https://localhost:4443")
httpd.server_forever()

#openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.key -out server.crt -days 365 -nodes -subj "/CN=localhost"
#openssl x509 -in server.crt -text -noout
