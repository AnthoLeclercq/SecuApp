from services.security_analysis_service import SecurityAnalysisService
from routes.base_routes import BaseRoutes

class SecurityAnalysisRoutes(BaseRoutes):
    def __init__(self, app):
        super().__init__(app,SecurityAnalysisService(), 'analysis')