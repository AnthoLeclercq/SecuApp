from flask import request, jsonify
from services.service_by_port_service import ServiceByPortService

class ServiceByPortRoutes:
    def __init__(self, app):
        self.app = app
        self.service = ServiceByPortService()

        # Register routes
        self.app.add_url_rule('/services/<int:port>', 'get_services_by_port', self.get_services_by_port, methods=['GET'])

    def get_services_by_port(self, port):
        """
        Example JSON output:
        [
            {
                "Host": "127.0.0.1",
                "Protocol": "tcp",
                "Port": 22,
                "Service": "ssh",
                "Version": "OpenSSH 7.9p1",
                "State": "open"
            },
            ...
        ]
        """
        services = self.service.get_services_by_port(port)
        return jsonify(services)
