from mis_model import ManagerialModel

class ManagerialApp:
    def __init__(self):
        self.model = ManagerialModel()

    def get_report(self, report_id):
        return self.model.get_report(report_id)