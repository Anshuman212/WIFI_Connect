from .network_manager import get_known_networks
from .speed_test import darth_speed_server,measure_download_speed,measure_upload_speed
from .wifi_con import connect_to_network
from .utils import darth_connection_wait
import time
import threading

def darth_query_network():
    networks=get_known_networks()
    best_net=None
    best_speed=0
    server_thread=threading.Thread(target=darth_speed_server)
    server_thread.daemon=True
    server_thread.start()
    
    time.sleep(5) #time for server to get ready 
    
    for network in networks:
        try:
            connect_to_network(network)
            if darth_connection_wait():
                download_speed=measure_download_speed()
                print(f"Network: {network} -Download Speed: {download_speed:.2f} Mbps")
                if download_speed>best_speed:
                    best_speed=download_speed
                    best_net=network
            else:
                print(f"{network} is lost in dreams. Skipping it!!!")
        except Exception as e:
            print(f"Failed to Connect might be bug read the error\n: {e}")
    if best_net:
        print(f"Connecting to the best available network: {best_net}")
        connect_to_network(best_net)
    else:
        print(f"Change the Location doesn't have good internet.")
        
if __name__=="__main__":
    darth_query_network()