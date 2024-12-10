from services.port_scan_service import PortScanService
from routes.base_routes import BaseRoutes

class PortScanRoutes(BaseRoutes):
    def __init__(self, app):
        super().__init__(app,PortScanService(), 'ports')