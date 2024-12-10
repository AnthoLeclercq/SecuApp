from flask import request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import os
from services.report_management_service import ReportManagementService
from utils.report_generator import ReportGenerator

report_generator = ReportGenerator()

class ReportManagementRoutes:
    def __init__(self, app):
        self.app = app
        self.service = ReportManagementService()

        # Register routes
        self.app.add_url_rule('/reports', 'generate_report', self.generate_report, methods=['POST'])

    def generate_report(self):
        """
        Example JSON input:
        {
            "data": {
                "hostname": "127.0.0.1",
                "vulnerabilities": [
                    {
                        "Vulnerability": "CVE-XXXX-XXXX",
                        "Summary": "Description of the vulnerability",
                        "CVSS": "CVSS score"
                    },
                    ...
                ],
                "open_ports": [
                    {
                        "Protocol": "tcp",
                        "Port": 22,
                        "Service": "ssh",
                        "Version": "OpenSSH 7.9p1",
                        "State": "open"
                    },
                    ...
                ],
                "services": [
                    {
                        "Protocol": "tcp",
                        "Port": 22,
                        "Service": "ssh",
                        "Version": "OpenSSH 7.9p1",
                        "State": "open"
                    },
                    ...
                ]
            },
            "format": "csv"
        }

        Example JSON output:
        {
            "message": "Report generated successfully"
        }
        """
        data = request.get_json()
        if not data or 'data' not in data or 'format' not in data:
            return jsonify({'error': 'Invalid request format'}), 400

        report_data = data['data']
        report_format = data['format']
        report = report_generator.generate_report(report_data, report_format , 'global')
        #report= self.service.generate_report(report_data, report_format)
        if not report:
            return jsonify({'error': 'Failed to generate report'}), 500

        file = report.file_path
        if file:
            return jsonify({'message': 'Report generated successfully', 'report_id': report.id, 'path': report.file_path}), 201
