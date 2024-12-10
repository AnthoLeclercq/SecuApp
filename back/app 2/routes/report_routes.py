from flask import request, jsonify, send_file
from database.models import Report
from database.db import Database

# Obtenir l'instance de la base de données
db = Database().get_db()

class ReportRoutes:
    def __init__(self, app):
        self.app = app

        # Route pour créer un rapport
        self.app.add_url_rule('/reports', 'create_report', self.create_report, methods=['POST'])

        # Route pour obtenir tous les rapports
        self.app.add_url_rule('/reports', 'get_all_reports', self.get_all_reports, methods=['GET'])

        # Route pour obtenir un rapport spécifique par ID
        self.app.add_url_rule('/reports/<int:id>', 'get_report', self.get_report, methods=['GET'])

        # Route pour mettre à jour un rapport spécifique par ID
        self.app.add_url_rule('/reports/<int:id>', 'update_report', self.update_report, methods=['PUT'])

        # Route pour supprimer un rapport spécifique par ID
        self.app.add_url_rule('/reports/<int:id>', 'delete_report', self.delete_report, methods=['DELETE'])

        # Route pour télécharger un rapport par ID
        self.app.add_url_rule('/reports/download/<int:id>', 'download_report', self.download_report, methods=['GET'])

    def create_report(self):
        # JSON attendu pour la création d'un rapport : {"data": "contenu du rapport", "format": "pdf", "file_path": "/chemin/du/fichier"}
        data = request.get_json()
        if not data or 'data' not in data or 'format' not in data or 'file_path' not in data:
            return jsonify({'error': 'Invalid request format'}), 400

        report_data = data['data']
        report_format = data['format']
        file_path = data['file_path']
        report = Report(data=report_data, format=report_format, file_path=file_path)
        db.session.add(report)
        db.session.commit()

        return jsonify({'message': 'Report created successfully'}), 201

    def get_all_reports(self):
        # Renvoie tous les rapports sous forme de JSON
        reports = Report.query.all()
        return jsonify({'reports': [{'id': report.id, 'name': report.name, 'type': report.type, 'format': report.format, 'file_path': report.file_path, 'created_at': report.formatted_created_at} for report in reports]})

    def get_report(self, id):
        # Renvoie un rapport spécifique par ID sous forme de JSON
        report = Report.query.get(id)
        if not report:
            return jsonify({'error': 'Report not found'}), 404

        return jsonify({'id': report.id, 'name': report.name, 'type': report.type, 'format': report.format, 'file_path': report.file_path, 'created_at': report.formatted_created_at})

    def update_report(self, id):
        # JSON attendu pour mettre à jour un rapport : {"data": "nouveau contenu du rapport", "format": "pdf", "file_path": "/chemin/du/fichier"}
        data = request.get_json()
        if not data or 'data' not in data or 'format' not in data or 'file_path' not in data:
            return jsonify({'error': 'Invalid request format'}), 400

        report = Report.query.get(id)
        if not report:
            return jsonify({'error': 'Report not found'}), 404

        report.data = data['data']
        report.format = data['format']
        report.file_path = data['file_path']
        db.session.commit()

        return jsonify({'message': 'Report updated successfully'})

    def delete_report(self, id):
        # Supprime un rapport spécifique par ID
        report = Report.query.get(id)
        if not report:
            return jsonify({'error': 'Report not found'}), 404

        db.session.delete(report)
        db.session.commit()

        return jsonify({'message': 'Report deleted successfully'})

    def download_report(self, id):
        # Récupérer le rapport correspondant à l'ID de la base de données
        report = Report.query.get_or_404(id)

        # Renvoyer le fichier en tant que réponse à la requête HTTP
        return send_file(report.file_path, as_attachment=True)