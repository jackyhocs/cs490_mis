class ManagerialDAO:
    def  __init__(self, db=None):
        if db:
            self.db = db
        else:
            #initialize DB
            pass

    def get_report(self, id):
        return {"id": id, "data": "stubbed data"}
