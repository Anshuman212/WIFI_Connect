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
            #identify whether it is upload or download test
            test_type=client_socket.recv(1024).decode()
            print(f"Client test type: {test_type}")
            if test_type=='download':
                data=b'0'*1024 #1kb of data
                end_time=time.time()+10 #send data after 10seconds
                while time.time()<end_time:
                    try:
                        #Sending data to client for download speed test
                        client_socket.sendall(data)
                    except ConnectionError:
                        break
            elif test_type=='upload':
                total_data_received=0
                end_time=time.time()+10
                while time.time()<end_time:
                    try:
                        received_data=client_socket.recv(1024)
                        if not received_data:
                            break
                        total_data_received+=len(received_data)
                    except ConnectionError:
                        break
                upload_speed=(total_data_received*8)/(10*1024*1024)
                print(f"Upload speed measured: {upload_speed:.2f} Mbps")
        finally:
            client_socket.close()
    
    while True:
        client_socket,addr=server.accept()
        client_handler=threading.Thread(target=handle_darth_client,args=(client_socket,))
        client_handler.start()


def measure_download_speed(host='127.0.0.1',port=8700,duration=5):
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((host,port))
    
    # Inform the server about the upload test
    client.sendall(b"download")
    # print("starting download test")
    start_time=time.time()
    total_data=0
    while time.time()-start_time<duration:
        data=client.recv(1024)
        if not data:
            break
        total_data+=len(data)
    client.close()
    
    # print("Ending download test")
    download_speed=(total_data*8)/(duration*1024*1024) #mbps
    # print("download speed",download_speed)
    return download_speed


def measure_upload_speed(host='127.0.0.1',port=8700,duration=5):
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((host,port))
    
    # Inform the server about the upload test
    client.sendall(b"upload")
    # print("upload test starting ")
    start_time=time.time()
    total_data=0
    data=b'0'*1024 #1kb of data send
    
    while time.time()-start_time<duration:
        try:
            client.sendall(data)
            total_data += len(data)
        except socket.error as e:
            print(f"Send error: {e}")
            break
    client.close()
    # print("upload test complete")
    upload_speed=(total_data*8)/(duration*1024*1024) #mbps mega bits per sec
    # print("upload speed",upload_speed)
    return upload_speed