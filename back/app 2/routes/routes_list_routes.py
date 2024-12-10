from flask import jsonify

class RouteList:
    def __init__(self, app):
        self.app = app

        # Register route list route
        self.app.add_url_rule('/routes', 'routes', self.get_routes, methods=['GET'])

    def get_routes(self):
        routes = []
        for rule in self.app.url_map.iter_rules():
            view_func = self.app.view_functions.get(rule.endpoint)
            if view_func is not None:
                routes.append({
                    'endpoint': rule.endpoint,
                    'methods': ','.join(rule.methods),
                    'path': str(rule),
                    'params': list(rule.arguments),
                    'view_func': view_func.__name__
                })
        return jsonify({'routes': routes})