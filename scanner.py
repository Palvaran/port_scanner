import socket

ip_address = input("Please enter the IP address of the computer: ")

print("Scanning the ports on IP address:", ip_address)

for port in range(1336,1338):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip_address, port))
    if result == 0:
        print("Port {}: Open".format(port))
    else:
        print("Port {}: Closed".format(port))
    sock.close()
