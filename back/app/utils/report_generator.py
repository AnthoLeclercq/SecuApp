import csv
import os
from datetime import datetime
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from database.models import Report
from database.db import Database
from utils.logger import Logger

db = Database().get_db()
logger = Logger().get_logger()


class ReportGenerator:
    def __init__(self):
        self.report_folder = os.environ.get('PATH_REPORT_FOLDER')

    def generate_report(self, data, format, report_type):
        if format.lower() == 'csv':
            format='csv'
            if report_type.lower() == 'global':
                file_path =  self.generate_csv_global_report(data)
            elif report_type.lower() == 'vulnerabilite':
                file_path = self.generate_csv_vulnerabilite_report(data)
            elif report_type.lower() == 'port':
                file_path = self.generate_csv_port_report(data)
            elif report_type.lower() == 'service':
                file_path = self.generate_csv_service_report(data)
            else:
                return False
        elif format.lower() == 'pdf':
            format='pdf'
            if report_type.lower() == 'global':
                file_path = self.generate_pdf_global_report(data)
            elif report_type.lower() == 'vulnerabilite':
                file_path = self.generate_pdf_vulnerabilite_report(data)
            elif report_type.lower() == 'port':
                file_path = self.generate_pdf_port_report(data)
            elif report_type.lower() == 'service':
                file_path = self.generate_pdf_service_report(data)
            else:
                return False
        else:
            return False
        
        now = datetime.now()
        report_name=  f"report_{report_type.lower()}_{now.strftime('%Y-%m-%d_%H-%M-%S')}"
        report = Report(file_path=file_path,format=format, type=report_type.lower(), name=report_name)
        db.session.add(report)
        db.session.commit()
        
        return report

    # -------------- CSV
    def generate_csv_global_report(self, data):
        if not data:
            return False

        fieldnames = ['Host', 'Type', 'Protocol', 'Port', 'Service', 'Version', 'State', 'Vulnerability', 'Summary', 'CVSS']
        now = datetime.now()
        file_name = f"global_report_{now.strftime('%Y-%m-%d_%H-%M-%S')}.csv"
        file_path = os.path.join(self.report_folder, file_name)

        with open(file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            
            
            if isinstance(data, dict):
                for vulnerability in data.get('vulnerabilities', []):
                    if isinstance(vulnerability, dict):
                        writer.writerow({
                            'Host': data.get('hostname', ''),
                            'Type': 'Vulnerability',
                            'Vulnerability': vulnerability.get('Vulnerability', ''),
                            'Summary': vulnerability.get('Summary', ''),
                            'CVSS': vulnerability.get('CVSS', '')
                        })

                for port in data.get('open_ports', []):
                    if isinstance(port, dict):
                        writer.writerow({
                            'Host': data.get('hostname', ''),
                            'Type': 'Port',
                            'Protocol': port.get('Protocol', ''),
                            'Port': port.get('Port', ''),
                            'Service': port.get('Service', ''),
                            'Version': port.get('Version', ''),
                            'State': port.get('State', '')
                        })

                for service in data.get('services', []):
                    if isinstance(service, dict):
                        writer.writerow({
                            'Host': data.get('hostname', ''),
                            'Type': 'Service',
                            'Protocol': service.get('Protocol', ''),
                            'Port': service.get('Port', ''),
                            'Service': service.get('Service', ''),
                            'Version': service.get('Version', ''),
                            'State': service.get('State', '')
                        })

        return file_path

    def generate_csv_vulnerabilite_report(self, data):
        if not data:
            return False

        fieldnames = ['Vulnerability', 'Summary', 'CVSS']
        now = datetime.now()
        file_name = f"vulnerabilite_report_{now.strftime('%Y-%m-%d_%H-%M-%S')}.csv"
        file_path = os.path.join(self.report_folder, file_name)

        with open(file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for vulnerability in data:
                if isinstance(vulnerability, dict):
                    writer.writerow({
                        'Vulnerability': vulnerability.get('Vulnerability', ''),
                        'Summary': vulnerability.get('Summary', ''),
                        'CVSS': vulnerability.get('CVSS', '')
                    })

        return file_path

    def generate_csv_port_report(self, data):
        if not data:
            return False

        fieldnames = ['Host', 'Protocol', 'Port', 'Service', 'State']
        now = datetime.now()
        file_name = f"port_report_{now.strftime('%Y-%m-%d_%H-%M-%S')}.csv"
        file_path = os.path.join(self.report_folder, file_name)

        with open(file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
        
            for port in data:
                if isinstance(port, dict):
                    writer.writerow({
                        'Host': port.get('Host', ''),
                        'Protocol': port.get('Protocol', ''),
                        'Port': port.get('Port', ''),
                        'Service': port.get('Service', ''),
                        'State': port.get('State', '')
                    })

        return file_path

    def generate_csv_service_report(self, data):
        if not data:
            return False

        fieldnames = ['Host', 'Protocol', 'Port', 'Service', 'Version', 'State']
        now = datetime.now()
        file_name = f"service_report_{now.strftime('%Y-%m-%d_%H-%M-%S')}.csv"
        file_path = os.path.join(self.report_folder, file_name)

        with open(file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            
            for service in data:
                if isinstance(service, dict):
                    writer.writerow({
                        'Host': service.get('Host', ''),
                        'Protocol': service.get('Protocol', ''),
                        'Port': service.get('Port', ''),
                        'Service': service.get('Service', ''),
                        'Version': service.get('Version', ''),
                        'State': service.get('State', '')
                    })

        return file_path

    def generate_header(self, title, type):
        now = datetime.now()
        generated_date = now.strftime('%Y-%m-%d %H:%M:%S')
        # style par défaut pour les paragraphes
        styles = getSampleStyleSheet()
        normal_style = styles["Normal"]
        
        # Ajouter le titre
        title_style = ParagraphStyle(name='Title', fontSize=20, alignment=TA_CENTER)
        title_paragraph = Paragraph(title, title_style)
        title_spacing = Spacer(1, 12)

        # Ajouter le paragraphe avec la date et le type de document
        info_text = f"Generated on: {generated_date}<br/>Rapport Type: {type}"
        info_paragraph = Paragraph(info_text, normal_style)
        horizontal_line = HRFlowable(width="33%", color=colors.black, thickness=1)

        return [title_paragraph, title_spacing,horizontal_line, info_paragraph, Spacer(1, 12), horizontal_line, Spacer(1, 12)]
    
    def generate_logo(self):
        image_path = "/app/assets/img/logo512.png"
        return Image(image_path, width=300, height=200)
    
    # -------------- PDF
    def generate_pdf_global_report(self, data):
        if not data:
            return False

        fieldnames = ['Host', 'Type', 'Protocol', 'Port', 'Service', 'Version', 'State', 'Vulnerability', 'Summary', 'CVSS']
        now = datetime.now()
        file_name = f"report_global_{now.strftime('%Y-%m-%d_%H-%M-%S')}.pdf"
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

        content = self.generate_header('Rapport Global', 'global')
        content.append(report_table)
        content.append(Spacer(1, 12))
        content.append(HRFlowable(width="33%", color=colors.black, thickness=1))
        content.append(Spacer(1, 12))    
        content.append(self.generate_logo())
        doc.build(content)
            
        return file_path
    
    
    def fill_table_data(self, data, fieldnames):
        table_data = []
        data

        for vulnerability in data.get('vulnerabilities', []):
            table_data.append([
                data.get('hostname', ''),
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

        for port in data.get('open_ports', []):
            table_data.append([
                data.get('hostname', ''),
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

        for service in data.get('services', []):
            table_data.append([
                data.get('hostname', ''),
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
    
    def generate_pdf_vulnerabilite_report(self, data):
        if not data:
            return False

        fieldnames = ['Vulnerability', 'Summary', 'CVSS']
        now = datetime.now()
        file_name = f"vulnerabilite_report_{now.strftime('%Y-%m-%d_%H-%M-%S')}.pdf"
        file_path = os.path.join(self.report_folder, file_name)

        doc = SimpleDocTemplate(file_path, pagesize=letter)
        table_data = self.fill_table_data_vulnerabilite(data)
        
        # Créer le tableau
        report_table = self.create_table(fieldnames, table_data)
        report_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                        ('GRID', (0, 0), (-1, -1), 1, colors.black)]))


        content = self.generate_header('Rapport Vulnerabilite', 'vulnérabilités')
        content.append(report_table)
        content.append(Spacer(1, 12))
        content.append(HRFlowable(width="33%", color=colors.black, thickness=1))
        content.append(Spacer(1, 12))    
        content.append(self.generate_logo())
        doc.build(content)
            
        return file_path

    def fill_table_data_vulnerabilite(self, data):
        table_data = []

        for vulnerability in data:
            if isinstance(vulnerability, dict):
                table_data.append([
                    vulnerability.get('Vulnerability', ''),
                    vulnerability.get('Summary', ''),
                    vulnerability.get('CVSS', '')
                ])

        return table_data

    def generate_pdf_port_report(self, data):
        if not data:
            return False

        fieldnames = ['Host', 'Protocol', 'Port', 'Service', 'State']
        now = datetime.now()
        file_name = f"port_report_{now.strftime('%Y-%m-%d_%H-%M-%S')}.pdf"
        file_path = os.path.join(self.report_folder, file_name)

        doc = SimpleDocTemplate(file_path, pagesize=letter)
        table_data = self.fill_table_data_port(data)
        
        # Créer le tableau
        report_table = self.create_table(fieldnames, table_data)
        report_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                        ('GRID', (0, 0), (-1, -1), 1, colors.black)]))

        content = self.generate_header('Rapport Port', 'ports')
        content.append(report_table)
        content.append(Spacer(1, 12))
        content.append(HRFlowable(width="33%", color=colors.black, thickness=1))
        content.append(Spacer(1, 12))    
        content.append(self.generate_logo())
        doc.build(content)
            
        return file_path

    def fill_table_data_port(self, data):
        table_data = []

        for port in data:
            if isinstance(port, dict):
                table_data.append([
                    port.get('Host', ''),
                    port.get('Protocol', ''),
                    port.get('Port', ''),
                    port.get('Service', ''),
                    port.get('State', '')
                ])

        return table_data

    def generate_pdf_service_report(self, data):
        if not data:
            return False

        fieldnames = ['Host', 'Protocol', 'Port', 'Service', 'Version', 'State']
        now = datetime.now()
        file_name = f"service_report_{now.strftime('%Y-%m-%d_%H-%M-%S')}.pdf"
        file_path = os.path.join(self.report_folder, file_name)

        doc = SimpleDocTemplate(file_path, pagesize=landscape(letter))
        table_data = self.fill_table_data_service(data)
        
        # Créer le tableau
        report_table = self.create_table(fieldnames, table_data)
        report_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                        ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
        
        content = self.generate_header('Rapport Services', 'services')
        content.append(report_table)
        content.append(Spacer(1, 12))
        content.append(HRFlowable(width="33%", color=colors.black, thickness=1))
        content.append(Spacer(1, 12))    
        content.append(self.generate_logo())

        doc.build(content)
            
        return file_path

    def fill_table_data_service(self, data):
        table_data = []

        for service in data:
            if isinstance(service, dict):
                table_data.append([
                    service.get('Host', ''),
                    service.get('Protocol', ''),
                    service.get('Port', ''),
                    service.get('Service', ''),
                    service.get('Version', ''),
                    service.get('State', '')
                ])

        return table_data