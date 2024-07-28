import socket
import time
import threading
def darth_speed_server(host='0.0.0.0',port=8700):
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    bound = False
    while not bound:
        try:
            server.bind((host, port))
            bound = True
        except OSError as e:
            if e.errno == 98:  # port in use
                port += 1
            else:
                raise e
    server.listen(5)
    print(f"Starting Speed server on {host}:{port}")
    
    def handle_darth_client(client_socket):
        try:
            data=b'0'*1024 #1kb of data
            end_time=time.time()+10 #send data after 10seconds
            while time.time()<end_time:
                try:
                    client_socket.sendall(data)
                except ConnectionError:
                    break
        finally:
            client_socket.close()
    
    while True:
        client_socket,addr=server.accept()
        client_handler=threading.Thread(target=handle_darth_client,args=(client_socket,))
        client_handler.start()


def measure_download_speed(host='127.0.0.1',port=8700,duration=5):
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((host,port))
    start_time=time.time()
    total_data=0
    while time.time()-start_time<duration:
        data=client.recv(1024)
        if not data:
            break
        total_data+=len(data)
    client.close()
    download_speed=(total_data*8)/(duration*1024*1024) #mbps
    return download_speed


def measure_upload_speed(host='127.0.0.1',port=8700,duration=5):
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((host,port))
    
    start_time=time.time()
    total_data=0
    data=b'0'*1024 #1kb of data send
    
    while time.time()-start_time<duration:
        client.sendall(data)    
        total_data+=len(data)
        data = client.recv(1024)
    client.close()
    upload_speed=(total_data*8)/(duration*1024*1024) #mbps mega bits per sec
    
    return upload_speed