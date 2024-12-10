import threading
from time import sleep
from database.models import IPAddress

class ScanThread(threading.Thread):
    def __init__(self, ip_address):
        super().__init__()
        self.ip_address = ip_address

    def run(self):
        print(f"Scanning IP: {self.ip_address}")
        sleep(3)
        print(f"Scan for IP {self.ip_address} finished")

def start_scans():
    active_ips = IPAddress.query.filter_by(status='Active').all()
    threads = []
    for ip in active_ips:
        thread = ScanThread(ip.ip_address)
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

