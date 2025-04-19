from database.DAO import DAO


class Model:
    def __init__(self):
        pass
    def getCodins(self):
        return DAO.getCodins()

    def getAllCorsi(self):
        return DAO.getAllCorsi()

    def getCorsiPD(self, pd):
        return DAO.getCorsiPD(pd)
