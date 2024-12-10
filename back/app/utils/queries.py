from flask import jsonify
from database.models import IPAddress 

def get_active_ips_to_json(self):
    active_ips = IPAddress.query.filter_by(status=True).all()
    
    ip_list = [{'id': ip.id, 'ip_address': ip.ip_address} for ip in active_ips]
    
    return jsonify(ip_list)