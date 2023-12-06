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
    wait_for_port(port=5000, timeout=60)
    wait_for_port(port=9090, timeout=60)
    exit(0)
except Exception:
    print("Se ha excedido el tiempo esperando la inicialización de los servicios flask y wiremock")
    exit(1)