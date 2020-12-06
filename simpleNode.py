from SenderThread import SenderThread
from ReceiverThread import ReceiverThread
import threading


def start_sender(ip, port):
    sender = SenderThread(ip, port)
    while True:
        # criticalSenderThread = threading.Thread(target=sender.send, args=(messageJSON,))
        senderThread = threading.Thread(target = sender.start_sender)
        senderThread.start()

def start_receiver():
    receiver = ReceiverThread()
    receiverThread = threading.Thread(target = receiver.start_listening)
    receiverThread.start()

def main():
    print("before sending")
    start_receiver()
    ip = bytes(input("enter target ip: "), "utf-8")
    port = int(input("enter target port: "))
    start_sender(ip, port)

if __name__ == '__main__':
    main()
