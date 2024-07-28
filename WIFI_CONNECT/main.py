from .network_manager import get_known_networks
from .speed_test import darth_speed_server,measure_download_speed,measure_upload_speed
from .wifi_con import connect_to_network
from .utils import darth_connection_wait
import time
import threading



def darth_query_network():
    networks=get_known_networks()
    best_network=None
    best_speed=0
    server_thread=threading.Thread(target=darth_speed_server)
    server_thread.daemon=True
    server_thread.start()
    
    time.sleep(5) #time for server to get ready 
    
    for network in networks:
        try:
            connect_to_network(network)
            if darth_connection_wait():
                print("Upload Speed Testing computer[================>]server")
                upload_speed=measure_upload_speed()
                time.sleep(5)
                print("Download Speed Testing computer[<===============]server")
                download_speed=measure_download_speed()
                # download_speed=0
                print(f"Network: {network} \n-Download Speed: {download_speed:.2f} Mbps | Upload Speed: {upload_speed:.2f} Mbps")
                net_score=0.7*download_speed+0.3*upload_speed
                if net_score>best_speed:
                    best_speed=net_score
                    best_network=network
            else:
                print(f"{network} is lost in dreams. Skipping it!!!")
        except Exception as e:
            print(f"Failed to Connect might be bug read the error\n: {e}")
    if best_network:
        print(f"{best_network} seems good for now. Connecting!!!...")
        connect_to_network(best_network)
    else:
        print(f"Change the Location doesn't have good internet.")
 
if __name__=="__main__":
    darth_query_network()