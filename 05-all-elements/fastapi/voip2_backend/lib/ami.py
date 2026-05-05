def make_call(from_ext: str, to_ext: str):
    import socket, time

    HOST = "asterisk"
    PORT = 5038
    USER = "amiuser"
    SECRET = "amipass"

    CHANNEL = f"PJSIP/{to_ext}"
    EXTEN = to_ext
    CONTEXT = "from-internal"
    PRIORITY = 1
    CALLERID = f"Test <{from_ext}>"

    s = socket.socket()
    s.connect((HOST, PORT))

    def send(sock, data):
        sock.sendall(data.encode())

    def recv(sock):
        time.sleep(0.5)
        data = sock.recv(65535).decode()
        print(data)
        return data

    recv(s)
    send(s, f"Action: Login\r\nUsername: {USER}\r\nSecret: {SECRET}\r\n\r\n")
    recv(s)

    send(s, f"Action: Originate\r\nChannel: {CHANNEL}\r\nContext: {CONTEXT}\r\nExten: {EXTEN}\r\nPriority: {PRIORITY}\r\nCallerID: {CALLERID}\r\nAsync: true\r\n\r\n")
    recv(s)

    send(s, "Action: Logoff\r\n\r\n")
    recv(s)

    s.close()
