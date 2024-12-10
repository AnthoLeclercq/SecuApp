import csv
import os
from datetime import datetime
from reportlab.lib.pagesizes import letter,landscape, portrait
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from database.models import Report
from database.db import Database
from utils.logger import Logger

db = Database().get_db()
logger = Logger().get_logger()

class ReportManagementService:
    def __init__(self):
        self.report_folder = os.environ.get('PATH_REPORT_FOLDER')

    def generate_report(self, data, format):
        if not data:
            return False

        logger.debug(f"Contenu de data : {data}")
        
        if format.lower() == 'csv':
            file_path = self.generate_csv_report(data)
        elif format.lower() == 'pdf':
            file_path = self.generate_pdf_report(data)
        else:
            return False

        if not file_path:
            return False

        report = Report(file_path=file_path)
        db.session.add(report)
        db.session.commit()

        return report

    def generate_csv_report(self, data):
        if not data:
            return False

        fieldnames = ['Host', 'Type', 'Protocol', 'Port', 'Service', 'Version', 'State', 'Vulnerability', 'Summary', 'CVSS']
        now = datetime.now()
        
        file_name = f"report_{now.strftime('%Y-%m-%d_%H-%M-%S')}.csv"

        file_path = os.path.join(self.report_folder, file_name)

        with open(file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            item = data
            logger.debug(f"Contenu de item : {item}")

            if isinstance(item, dict):
                for vulnerability in item.get('vulnerabilities', []):
                    if isinstance(vulnerability, dict):
                        writer.writerow({
                            'Host': item.get('hostname', ''),
                            'Type': 'Vulnerability',
                            'Protocol': '',
                            'Port': '',
                            'Service': '',
                            'Version': '',
                            'State': '',
                            'Vulnerability': vulnerability.get('Vulnerability', ''),
                            'Summary': vulnerability.get('Summary', ''),
                            'CVSS': vulnerability.get('CVSS', '')
                        })

                for port in item.get('open_ports', []):
                    if isinstance(port, dict):
                        writer.writerow({
                            'Host': item.get('hostname', ''),
                            'Type': 'Port',
                            'Protocol': port.get('Protocol', ''),
                            'Port': port.get('Port', ''),
                            'Service': port.get('Service', ''),
                            'Version': port.get('Version', ''),
                            'State': port.get('State', ''),
                            'Vulnerability': '',
                            'Summary': '',
                            'CVSS': ''
                        })

                for service in item.get('services', []):
                    if isinstance(service, dict):
                        writer.writerow({
                            'Host': item.get('hostname', ''),
                            'Type': 'Service',
                            'Protocol': service.get('Protocol', ''),
                            'Port': service.get('Port', ''),
                            'Service': service.get('Service', ''),
                            'Version': service.get('Version', ''),
                            'State': service.get('State', ''),
                            'Vulnerability': '',
                            'Summary': '',
                            'CVSS': ''
                        })

        return file_path
    
    def generate_pdf_report(self, data):
        if not data:
            return False

        fieldnames = ['Host', 'Type', 'Protocol', 'Port', 'Service', 'Version', 'State', 'Vulnerability', 'Summary', 'CVSS']
        now = datetime.now()
        file_name = f"report_{now.strftime('%Y-%m-%d_%H-%M-%S')}.pdf"
        file_path = os.path.join(self.report_folder, file_name)

        doc = SimpleDocTemplate(file_path, pagesize=landscape(letter))
        table_data = self.fill_table_data(data, fieldnames)
        
        # Créer le tableau
        report_table = self.create_table(fieldnames, table_data)
        report_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                          ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                          ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                          ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                          ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                          ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                          ('GRID', (0, 0), (-1, -1), 1, colors.black)]))


        doc.build([report_table])
            
        return file_path
      
    def fill_table_data(self, data, fieldnames):
        table_data = []
        item = data

        for vulnerability in item.get('vulnerabilities', []):
            table_data.append([
                item.get('hostname', ''),
                'Vulnerability',
                '',
                '',
                '',
                '',
                '',
                vulnerability.get('Vulnerability', ''),
                vulnerability.get('Summary', ''),
                vulnerability.get('CVSS', '')
            ])

        for port in item.get('open_ports', []):
            table_data.append([
                item.get('hostname', ''),
                'Port',
                port.get('Protocol', ''),
                port.get('Port', ''),
                port.get('Service', ''),
                port.get('Version', ''),
                port.get('State', ''),
                '',
                '',
                ''
            ])

        for service in item.get('services', []):
            table_data.append([
                item.get('hostname', ''),
                'Service',
                service.get('Protocol', ''),
                service.get('Port', ''),
                service.get('Service', ''),
                service.get('Version', ''),
                service.get('State', ''),
                '',
                '',
                ''
            ])

        return table_data

    def create_table(self, fieldnames, table_data):
        return Table([fieldnames] + table_data)