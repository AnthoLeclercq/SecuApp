import nmap
import threading
from services.base_service import BaseService
from utils.report_generator import ReportGenerator

report_generator = ReportGenerator()

class ServiceScanService(BaseService):
    def __init__(self):
        super().__init__()        
        self.analysis_lock = threading.Lock()

    def scan(self, hostname):        
        with self.analysis_lock:
            if self.progress is not None:
                    return {'error': 'An analysis of Service is already in progress'}
            self._set_progress(0)

        results = self.service_logique(hostname)
                    
        self._set_progress(None)
        
        if(len(results)>0):
            report_generator.generate_report(results, 'csv','service')
            report_generator.generate_report(results, 'pdf','service')

        return results

    def service_logique(self, hostname):
        scanner = nmap.PortScanner()
        self.progress = 25
        
        scanner.scan(hostname, arguments='-sV')
        self.progress = 50

        results = []
        for host in scanner.all_hosts():
            for proto in scanner[host].all_protocols():
                ports = scanner[host][proto].keys()
                for port in ports:
                    result = {
                        'Host': host,
                        'Protocol': proto,
                        'Port': port,
                        'Service': scanner[host][proto][port]['name'],
                        'Version': scanner[host][proto][port]['version'],
                        'State': scanner[host][proto][port]['state']
                    }
                    results.append(result)

        return results