from flask import request, jsonify
from database.models import IPAddress 
from utils.logger import Logger

logger = Logger().get_logger()

class BaseRoutes:
    def __init__(self, app, service, route_name):
            self.app = app
            self.service = service
            self.route_name = route_name
            
            # Register routes
            self.app.add_url_rule(f'/{self.route_name}', f'scan_with_json_{self.route_name}', self.scan, methods=['POST'])
            self.app.add_url_rule(f'/{self.route_name}/progress', f'get_progress_{self.route_name}', self.get_progress, methods=['GET'])
            self.app.add_url_rule(f'/{self.route_name}/scan', f'scan_{self.route_name}', self.start_scans, methods=['GET'])

    def scan(self):
        data = request.get_json()
        logger.debug(f'scan avec le data :{data}')
        jsonInValid = "hostname" not in data
        
        if jsonInValid : 
            return jsonify({'error': 'Missing hostname parameter'}), 400

        hostname = data['hostname']
        
        result = self.service.scan(hostname)
        return jsonify(result)
        
    def get_progress(self):
        
        progress = self.service.get_scan_progress()
        return jsonify(progress)
    
    
    def start_scans(self):
        active_ips = IPAddress.query.filter_by(status=True).all()
        logger.debug(f'ActiveIp :{active_ips}')
        
        results = []
        
        for ip in active_ips:
            result = self.service.scan(ip.ip_address)
            results.append(result)
        
        return jsonify(results)
