from services.service_scan_service import ServiceScanService
from routes.base_routes import BaseRoutes

class ServiceScanRoutes(BaseRoutes):
    def __init__(self, app):
        super().__init__(app,ServiceScanService(), 'services')