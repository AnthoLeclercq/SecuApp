import nmap
import threading
from services.base_service import BaseService
from utils.logger import Logger
from utils.report_generator import ReportGenerator

logger = Logger().get_logger()
report_generator = ReportGenerator()

class PortScanService(BaseService):
    def __init__(self):
        super().__init__()        
        self.analysis_lock = threading.Lock()
    
    def scan(self, hostname):        
        with self.analysis_lock:
            if self.progress is not None:
                    return {'error': 'An analysis of ports is already in progress'}
            self._set_progress(0)

        results = self.service_logique(hostname)
                    
        self._set_progress(None)
        
        if(len(results)>0):
            report_generator.generate_report(results, 'csv','port')
            report_generator.generate_report(results, 'pdf','port')
        
        return results

    def service_logique(self, hostname):
        scanner = nmap.PortScanner()
        self._set_progress(25)
        
        scanner.scan(hostname, arguments='-Pn -sV -O')
        self._set_progress(50)

        results = []
        for host in scanner.all_hosts():
            for proto in scanner[host].all_protocols():
                ports = scanner[host][proto].keys()
                for port in ports:
                    result = {
                        'Host': host,
                        'Protocol': proto,
                        'Port': port,
                        'State': scanner[host][proto][port]['state'],
                        'Service': scanner[host][proto][port]['name']
                    }
                    results.append(result)
        
        return results