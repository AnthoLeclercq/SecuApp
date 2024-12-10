from flask import request, jsonify
from services.local_network_scan_service import LocalNetworkScanService

class LocalNetworkScanRoutes:
    def __init__(self, app):
        self.app = app
        self.service = LocalNetworkScanService()

        # Register routes
        self.app.add_url_rule('/local-network/scan', 'scan_local_network', self.scan_local_network, methods=['GET'])

    def scan_local_network(self):
        """
        Example JSON output:
        [
            {
                "Host": "192.168.1.1",
                "Status": "up",
                "OpenPorts": [
                    {
                        "Port": 22,
                        "Service": "ssh",
                        "Protocol": "tcp"
                    },
                    ...
                ]
            },
            ...
        ]
        """
        local_network_scan_results = self.service.scan_local_network()
        return jsonify(local_network_scan_results)
