import subprocess
import time


def refresh_network_list():
    refresh_network_list='netsh wlan disconnect'
    refresh_result=subprocess.run(['cmd.exe','/c',refresh_network_list],capture_output=True,text=True,check=True)
    print("Refreshing the available Network List\n")
    time.sleep(2) 

def get_known_networks():
    show_all_known_networks ='netsh wlan show profiles'
    show_all_active_networks='netsh wlan show networks'
    result_all_known_network = subprocess.run(['cmd.exe', '/c', show_all_known_networks], capture_output=True, text=True,check=True)
    refresh_network_list()
    result_all_active_network = subprocess.run(['cmd.exe', '/c', show_all_active_networks], capture_output=True, text=True,check=True)
    networks_all_known=[]
    networks_all_active=[]
    for line in result_all_known_network.stdout.split('\n'):
        if 'All User Profile' in line:
            parts=line.split(':')
            if len(parts)>1:
                networks_all_known.append(parts[1].strip())
    networks_known_available=[]
    for line in result_all_active_network.stdout.split('\n'):
        if 'SSID' in line:
            parts=line.split(':')
            if(len(parts)>1):
                networks_all_active.append(parts[1].strip())
    for net in networks_all_known:
        if net in networks_all_active:
            networks_known_available.append(net)
    return networks_known_available

