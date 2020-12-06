import socket, threading, json

class SenderThread:
    ip = ""
    port = 0

    def __init__(self, ip, port):             #target ip and port
        self.ip = ip
        self.port = port

    def add_headers(self, message, acknowledge = False):
        headers = {"ACK": acknowledge}
        finalMessage = {"HEAD": headers, "MESSAGE": message}
        print(finalMessage["HEAD"])
        finalMessageStr = json.dumps(finalMessage)
        print("sending message: %s" % message)
        return finalMessageStr

    def send(self, message):
        print(message)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        addr = (self.ip, self.port)                                                         # TODO: buffer size stuff !
        sock.sendto(message, addr)

    def start_sender(self):
        message = input("type what you wanna send")
        messageJSONstring = bytes(self.add_headers(message, True), "utf-8")
        self.send(messageJSONstring)
