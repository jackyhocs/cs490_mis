from mis_dao import ManagerialDAO

class ManagerialModel:
    def __init__(self, db=None):
        self.dao = ManagerialDAO(db)

    def get_report(self, report_id):
        return {"id": report_id, "data": "stub"}
