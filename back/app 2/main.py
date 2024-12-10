from flask import Flask
from flask_cors import CORS

from routes.vulnerability_routes import VulnerabilityRoutes
from routes.port_scan_routes import PortScanRoutes
from routes.service_scan_routes import ServiceScanRoutes
from routes.local_network_scan_routes import LocalNetworkScanRoutes
from routes.report_management_routes import ReportManagementRoutes
from routes.security_analysis_routes import SecurityAnalysisRoutes
from routes.service_by_port_routes import ServiceByPortRoutes
from routes.ip_address_routes import IPAddressRoutes
from routes.status_routes import StatusRoutes
from routes.routes_list_routes import RouteList
from routes.report_routes import ReportRoutes
from flask_migrate import Migrate
from database.config import Config
from database.db import Database

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
database = Database(app)
database.init_app(app)
db = database.get_db()
migrate = Migrate(app, db)

# Register API routes
VulnerabilityRoutes(app)
PortScanRoutes(app)
ServiceScanRoutes(app)
LocalNetworkScanRoutes(app)
ReportManagementRoutes(app)
SecurityAnalysisRoutes(app)
ServiceByPortRoutes(app)
IPAddressRoutes(app)
StatusRoutes(app)
RouteList(app)
ReportRoutes(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
