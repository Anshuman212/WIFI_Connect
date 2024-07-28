import unittest
from WIFI_CONNECT.network_manager import get_known_networks
from WIFI_CONNECT.wifi_con import connect_to_network
from WIFI_CONNECT.speed_test import measure_upload_speed,measure_download_speed,darth_speed_server
import time
import threading

class TestWifiConnect(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Starting the server before any tests are run"""
        # cls.server_thread=threading.Thread(target=darth_speed_server,daemon=True)
        # cls.server_thread.start()
        time.sleep(2)
        
    @classmethod
    def tearDownClass(cls):
        """shut down the started server"""
        pass
    
    def test_get_known_networks(self):
        networks=get_known_networks()
        self.assertIsInstance(networks,list,"should be a list")
        self.assertTrue(len(networks)>0,"There has to be atleast one known network otherwise why waste time")
        
    def test_connect_to_network(self):
        network_name = input("Enter the network to connect to: ")
        result = connect_to_network(network_name)
        self.assertTrue(result, f"Failed to connect to the network: {network_name}")
    
    

if __name__ == '__main__':
    unittest.main()