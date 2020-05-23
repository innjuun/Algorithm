import socket
import time


def scanning():
    print("This program will print the number of web servers plus your input+10")
    subnetA, subnetB = map(int, input(
        "input the address of subnets(Ex. 177.200): ").split('.'))
    print()

    count = 0
    start_time = time.time()

    for i in range(subnetB, subnetB+10):
        addr = f"166.104.{subnetA}.{i}"
        port = 80

        socket.setdefaulttimeout(1)

        socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            result = socket_obj.connect((addr, port))
            print(f"Address: {addr} Port: {port} and Success to connect",)
            try:
                hostname = socket.gethostbyaddr(addr)[0]
                print(f"Hostname: {hostname}", end='\n\n')

            except socket.herror:
                print(f"Hostname: The information of domain is hidden", end='\n\n')

            count += 1
        except socket.timeout:
            print(f"Address: {addr} Port: {port} and Failed to connect")
        except BlockingIOError:
            print(f"Address: {addr} Port: {port} and Failed to connect")

        socket_obj.close()

    elapsed_time = round(time.time() - start_time, 3)
    print(f"Total number of web servers: {count}")
    print(f"Scan duration:{elapsed_time}")


scanning()
