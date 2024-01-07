import sys, getopt
import socket
import time

def wait_for_port(port: int, host: str = 'localhost', timeout: float = 5.0):
    start_time = time.perf_counter()
    while True:
        try:
            with socket.create_connection((host, port), timeout=timeout):
                break
        except Exception:
            time.sleep(0.01)
            if time.perf_counter() - start_time >= timeout:
                raise TimeoutError() from None

try:
    for port in sys.argv[1:]:
        wait_for_port(port, timeout=60)
        print(port)
    exit(0)
except Exception:
    print("Se ha excedido el tiempo esperando la apertura del puerto por el servicio")
    exit(1)