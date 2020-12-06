import socket, threading, json

class ReceiverThread:
    senders = []
    sock = 0

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, # Internet
                          socket.SOCK_DGRAM) # UDP
        self.senders = []

    def start_listening(self):
        ip = bytes(input("enter receiving ip: "), "utf-8")
        port = int(input("enter receiving port: "))
        self.sock.bind((ip, port))

        while True:
                print("listening...")
                data, addr = self.sock.recvfrom(1024)                                                        # buffer size is 1024 bytes
                print("received message: %s" % data)
                actingThread = threading.Thread(target=self.act_on, args = (data, addr))
                actingThread.start()

    def act_on(self,data, addr):
        addr_is_new = True

        for s in self.senders:
            if(s == addr):
                addr_is_new = False

        if(addr_is_new):
            self.senders.append(addr)
        print(data)
        dataStr = data.decode("utf-8")
        print("do something with " + dataStr)                                                              # this part -> computing logics          ?
        data = json.loads(dataStr)
        print("message: " + data["MESSAGE"])
