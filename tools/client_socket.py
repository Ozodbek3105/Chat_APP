import errno
import json
import socket

from PySide6.QtCore import QThread, Signal, Slot

from tools.turli import malumotni_formatla

HEADER_LENGTH = 10
IP = "192.168.33.56"
PORT = 1234


class ClientSocket(QThread):
    received = Signal(str, str)
    connected = Signal()
    disconnected = Signal()
    kirdi = Signal(str)
    chiqdi = Signal(str)

    def __init__(self, username, ip=IP, port=PORT, parent=None):
        super().__init__(parent)
        self.username = username
        self.ip = ip
        self.port = port
        self.client_socket = None
        self.running = False

    def close_socket(self):
        self.client_socket.close()

    def run(self):
        """Main thread execution function."""
        self.running = True
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.ip, self.port))
        self.client_socket.setblocking(True)

        # yanfgi foydalanuvchi kirganligi haqida jo'nat
        # habar_turi:
        #     0 - foydalanuvchi kirdi/chiqdi haqida
        #     1 - oddiy habar
        data = malumotni_formatla(habar_turi=0, kirdi=True, foydalanuvchi=self.username)

        username_header = f"{len(data):<{HEADER_LENGTH}}".encode('utf-8')
        self.client_socket.send(username_header + data)

        self.connected.emit()  # Emit connected signal

        while self.running:
            try:
                self.habarni_qabul_qilish()
            except IOError as e:
                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print("Reading error", e)
                    break
            except Exception as e:
                print('General error', e)
                break

        self.disconnected.emit()  # Emit disconnected signal
        self.client_socket.close()

    @Slot(str)
    def send_message(self, message):
        """Handles sending messages to the server."""
        if self.client_socket and self.running:
            try:
                message = malumotni_formatla(habar=message, habar_turi=1, foydalanuvchi=self.username)

                message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
                self.client_socket.send(message_header + message)
                print("message:", message)
                print("message_header:", message_header)
            except (OSError, BrokenPipeError):
                print("Disconnected from server.")
                self.running = False

    # def foydalanuvchi_chiqdi(self):
    #     malumot = malumotni_formatla(kirdi=False, habar_turi=0, foydalanuvchi=self.username)
    #     message_header = f"{len(malumot):<{HEADER_LENGTH}}".encode('utf-8')
    #     self.client_socket.send(message_header + malumot)

    def habarni_qabul_qilish(self):
        """Handles receiving messages from the server."""

        message_header = self.client_socket.recv(HEADER_LENGTH)
        message_length = int(message_header.decode('utf-8'))
        malumot = self.client_socket.recv(message_length).decode('utf-8')
        malumot = json.loads(malumot)
        if malumot['habar_turi'] == 0:
            if malumot['kirdi']:
                print(f"{malumot['kimdan']} foydalanuvchi kirdi")
                if isinstance(malumot['kimdan'],list):
                    foydalanuvchilar = list(malumot['kimdan'])
                    for foydalanuvchi in foydalanuvchilar:
                        self.kirdi.emit(foydalanuvchi)
                else:
                    self.kirdi.emit(malumot['kimdan'])
            else:
                print(f"{malumot['kimdan']} foydalanuvchi chiqdi")
                self.chiqdi.emit(malumot['kimdan'])

        else:
            # print("username:", username)
            # print("username_length:", username_length)
            # print("username_header:", username_header)
            # print("malumot:", malumot)
            # print("message_header:", message_header)
            # print("message_length:", message_length)
            # print(f"{username} > {malumot}")
            self.received.emit(malumot['kimdan'], malumot['habar'])

    def stop(self):
        """Stops the thread and closes the connection."""
        self.running = False
        self.quit()
        self.wait()
