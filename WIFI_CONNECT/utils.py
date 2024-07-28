import time
import socket
def darth_connection_wait(host="8.8.8.8", port=53, timeout=5):
    for _ in range(10): #retrying 10 times i.e for 10 seconds
        try:
            socket.create_connection((host, port), timeout=timeout)
            return True
        except OSError:
            time.sleep(1) #simply trying to stablize the network once done sending iteration forward.
            
    return False