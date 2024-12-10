from flask import request, jsonify
from database.models import IPAddress
from database.db import Database
from utils.logger import Logger

logger = Logger().get_logger()

# Obtenir l'instance de la base de données
db = Database().get_db()

class IPAddressRoutes:
    def __init__(self, app):
        self.app = app

        # Route pour créer une adresse IP
        self.app.add_url_rule('/ip-addresses', 'create_ip_address', self.create_ip_address, methods=['POST'])

        # Route pour obtenir toutes les adresses IP
        self.app.add_url_rule('/ip-addresses', 'get_all_ip_addresses', self.get_all_ip_addresses, methods=['GET'])

        # Route pour obtenir une adresse IP spécifique par ID
        self.app.add_url_rule('/ip-addresses/<int:id>', 'get_ip_address', self.get_ip_address, methods=['GET'])

        # Route pour mettre à jour une adresse IP spécifique par ID
        self.app.add_url_rule('/ip-addresses/<int:id>', 'update_ip_address', self.update_ip_address, methods=['PUT'])

        # Route pour supprimer une adresse IP spécifique par ID
        self.app.add_url_rule('/ip-addresses/<int:id>', 'delete_ip_address', self.delete_ip_address, methods=['DELETE'])

    def create_ip_address(self):
        # JSON attendu pour la création d'une adresse IP : {"ip_address": "192.168.1.1", "status": "active"}
        data = request.get_json()
        if not data or 'ip_address' not in data or 'status' not in data:
            return jsonify({'error': 'Invalid request format'}), 400

        ip_address = data['ip_address']
        logger.debug(data['status'])
        status = bool(data['status'])
        logger.debug(status)
        
        ip = IPAddress(ip_address=ip_address, status=status)
        db.session.add(ip)
        db.session.commit()

        return jsonify({'message': 'IP address created successfully'}), 201

    def get_all_ip_addresses(self):
        # Renvoie toutes les adresses IP sous forme de JSON
        ip_addresses = IPAddress.query.all()
        return jsonify({'ip_addresses': [{'id': ip.id, 'ip_address': ip.ip_address, 'status': ip.status} for ip in ip_addresses]})

    def get_ip_address(self, id):
        # Renvoie une adresse IP spécifique par ID sous forme de JSON
        ip = IPAddress.query.get(id)
        if not ip:
            return jsonify({'error': 'IP address not found'}), 404

        return jsonify({'id': ip.id, 'ip_address': ip.ip_address, 'status': ip.status})

    def update_ip_address(self, id):
        # JSON attendu pour mettre à jour une adresse IP : {"ip_address": "192.168.1.1", "status": "inactive"}
        data = request.get_json()
        if not data or 'ip_address' not in data or 'status' not in data:
            return jsonify({'error': 'Invalid request format'}), 400

        ip = IPAddress.query.get(id)
        if not ip:
            return jsonify({'error': 'IP address not found'}), 404

        ip.ip_address = data['ip_address']
        logger.debug(data['status'])
        ip.status =  bool(data['status'])
        logger.debug(ip.status)
        
        db.session.commit()

        return jsonify({'message': 'IP address updated successfully'})

    def delete_ip_address(self, id):
        # Supprime une adresse IP spécifique par ID
        ip = IPAddress.query.get(id)
        if not ip:
            return jsonify({'error': 'IP address not found'}), 404

        db.session.delete(ip)
        db.session.commit()

        return jsonify({'message': 'IP address deleted successfully'})
