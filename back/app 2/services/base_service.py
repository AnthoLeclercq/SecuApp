class BaseService:
    def __init__(self):
        self.progress = None

    def _set_progress(self, value):
        self.progress = value

    def get_scan_progress(self):
        status = 'Stopped'  # Valeur par défaut
        if self.progress is not None:
            if self.progress == 100:
                status = 'Completed'
            elif self.progress >= 0:
                status = 'Running'

        return {'status': status, 'progress': self.progress}
