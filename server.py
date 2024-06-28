import json
import socket
import select
from tools.turli import malumotni_formatla

# Doimiylar
HEADER_LENGTH = 10

IP = "192.168.33.56"
PORT = 1234

# TCP/IP soketi yaratish
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Soketni qayta ishlatish uchun sozlashlar
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Soketni manzil va portga ulash
server_socket.bind((IP, PORT))

# Kiruvchi ulanishlarni kutish
server_socket.listen()

# Kuzatiladigan soketlar ro'yxati
soketlar_royhati = [server_socket]

# Mijozlarni va ularning ma'lumotlarini kuzatish uchun lug'at
clients = {}

def habarni_hammaga_jonat(client_socket_list, malumot: dict, yuboruvchi_soketi):
    for client_socket in client_socket_list:
        if client_socket != server_socket and yuboruvchi_soketi != client_socket:
            habarni_jonat(client_socket, malumot)

def habarni_jonat(client_socket, malumot: dict):
    if isinstance(malumot, dict):
        malumot = json.dumps(malumot).encode('utf-8')

    message_header = f"{len(malumot):<{HEADER_LENGTH}}".encode('utf-8')
    client_socket.send(message_header + malumot)
    print("message:", malumot)
    print("message_header:", message_header)

def foydalanuvchini_ochir(foydalanuvchilar, soket):
    for foydalanuvchi, foydalanuvchi_soketi in foydalanuvchilar.items():
        if soket == foydalanuvchi_soketi:
            del foydalanuvchilar[foydalanuvchi]
            break

def habarni_qabul_qil(client_socket):
    """Mijozdan xabar olish funksiyasi.
        return {"header": <int>, "data": <dict>}
            header - o'lchami
            data - malumot
    """
    try:
        # Xabar sarlavhasini o'qish
        message_header = client_socket.recv(HEADER_LENGTH)
        print("message_header:", message_header)
        # Agar hech qanday ma'lumot olinmasa, mijoz uzilgan
        if not len(message_header):
            return False

        # Xabar uzunligini aniqlash
        message_length = int(message_header.decode('utf-8').strip())

        # Sarlavha va ma'lumotni o'z ichiga olgan lug'atni qaytarish
        malumot = client_socket.recv(message_length)
        malumot = json.loads(malumot.decode('utf-8'))

        return malumot
    except:
        return False

def kirganligi_haqida_jonat(client_socket):
    client_socket.send(malumot['header'] + malumot['data'])

try:  # Qo'shildi
    while True:
        try:
            # Soketlarda faoliyatni kutish uchun select funksiyasidan foydalanish
            habar_kelgan_soketlar, _, exception_sockets = select.select(soketlar_royhati, [], soketlar_royhati)

            for habar_kelgan_soket in habar_kelgan_soketlar:
                if habar_kelgan_soket == server_socket:
                    # Yangi ulanish
                    ulangan_mijoz_soketi, client_address = server_socket.accept()
                    soketlar_royhati.append(ulangan_mijoz_soketi)

                    # kirgan foydalanuvchilar royxati
                    foydalanuvchilar = list(clients.keys())
                    print(foydalanuvchilar)
                    foydalanuvchilar = json.dumps(foydalanuvchilar)
                    malumot = malumotni_formatla(kirdi=True, habar_turi=0, foydalanuvchi=foydalanuvchilar)
                    habarni_jonat(ulangan_mijoz_soketi, malumot)
                else:
                    # Mavjud mijozdan xabar
                    malumot = habarni_qabul_qil(habar_kelgan_soket)

                    # Agar malumot False bo'lsa, mijoz uzilgan
                    if malumot is False:
                        yangi_malumot = malumotni_formatla(kirdi=False, habar_turi=0, foydalanuvchi=None)
                        habarni_hammaga_jonat(habar_kelgan_soketlar, yangi_malumot, habar_kelgan_soket)
                        soketlar_royhati.remove(habar_kelgan_soket)
                        foydalanuvchini_ochir(clients, habar_kelgan_soket)
                        continue
                    else:
                        if malumot['habar_turi'] == 0 and malumot['kirdi'] is True:
                            clients[malumot['kimdan']] = habar_kelgan_soket

                    print(f"{malumot['kimdan']} foydalanuvchidan xabar olindi: {malumot['habar']}")

                    # Xabarni barcha mijozlarga yuborish
                    if not malumot['kimga']:
                        habarni_hammaga_jonat(soketlar_royhati, malumot, habar_kelgan_soket)
                    else:
                        mijoz_soket = clients[malumot['kimga']]
                        habarni_jonat(mijoz_soket, malumot)

            # Istisno soketlarni boshqarish
            for habar_kelgan_soket in exception_sockets:
                soketlar_royhati.remove(habar_kelgan_soket)
                foydalanuvchini_ochir(clients, habar_kelgan_soket)
                print("Istisno soketi o'chirildi")

        except KeyboardInterrupt:  # Qo'shildi
            print("\nServer to'xtatildi.")
            break

finally:  # Qo'shildi
    for soket in soketlar_royhati:
        soket.close()
    print("Barcha soketlar yopildi.")
