import subprocess

def connect_to_network(network_name):
    try:
        command=f"netsh wlan connect name=\"{network_name}\""
        print(f"Connecting to Network: {network_name}")
        subprocess.run(['cmd.exe', '/c', command],check=True,capture_output=True,text=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to connect to Network:{network_name}: {e}")