from flask import jsonify

class StatusRoutes:
    def __init__(self, app):
        self.app = app

        # Register status route
        self.app.add_url_rule('/status', 'status', self.get_status, methods=['GET'])

    def get_status(self):
        return jsonify({'status': 'API is running'})
