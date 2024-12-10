import threading

from services.vulnerability_service import VulnerabilityService
from services.port_scan_service import PortScanService
from services.service_scan_service import ServiceScanService
from utils.report_generator import ReportGenerator
from services.base_service import BaseService

report_generator = ReportGenerator()

class SecurityAnalysisService(BaseService):
    def __init__(self):
        super().__init__()        
        self.analysis_lock = threading.Lock()
        
    def scan(self, hostname):
        with self.analysis_lock:
            if self.progress is not None:
                return {'error': 'A Global analysis is already in progress'}
            self._set_progress(0)
            
        vulnerability_service = VulnerabilityService()
        port_scan_service = PortScanService()
        service_scan_service = ServiceScanService()
        self._set_progress(10)

        vulnerabilities = vulnerability_service.scan(hostname)
        self._set_progress(30)
        open_ports = port_scan_service.scan(hostname)
        self._set_progress(60)
        services = service_scan_service.scan(hostname)
        self._set_progress(90)

        results = {
            'hostname': hostname,
            'vulnerabilities': vulnerabilities,
            'open_ports': open_ports,
            'services': services
        }
        
        report_generator.generate_report(results, 'csv', 'global')
        report_generator.generate_report(results, 'pdf', 'global')
        
        self._set_progress(None)

        return results
