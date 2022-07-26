import socket

try:
    IP = input("Enter IP address: ")
    PORT = int(input("Enter port number: "))
except exception as err:
    print('Modo de uso:'
          '\nEndereço site.com\n'
          'Porta ex.: 80')
try:
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.settimeout(0.6)
    code = c.connect_ex((IP, PORT))

    if code == 0:
        print(f'Port {PORT} -> OPEN')
    else:
        print(f'Port {PORT} -> CLOSED')
except Exception as err:
    pass