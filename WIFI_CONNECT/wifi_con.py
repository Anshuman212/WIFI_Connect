import subprocess

def connect_to_network(network_name):
    try:
        command=f"netsh wlan connect  name=\"{network_name}\""
        subprocess.run(['cmd.exe', '/c', command],check=True)
        print(f"connecting to network: {network_name}")
    except subprocess.CalledProcessError as e:
        print(f"failed to connect to network:{network_name}: {e}")