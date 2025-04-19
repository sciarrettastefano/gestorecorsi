from database.DB_connect import DBConnect
from model.corso import Corso


class DAO():

    @staticmethod
    def getCodins():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT c.codins
                   FROM corso c"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row["codins"])
        # processa res

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllCorsi():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT * 
                   FROM corso c"""
        cursor.execute(query)

        res = []
        for row in cursor:
            """res.append(Corso(codins=row["codins"],
                             crediti=row["crediti"],
                             nome=row["nome"],
                             pd=row["pd"]))"""
            res.append(Corso(**row))  # fa unpack del dizionario di cursor e ci crea gli oggetti Corso

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCorsiPD(pd):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT *
                   FROM corso c 
                   WHERE c.pd = %s"""
        cursor.execute(query, (pd,))

        res = []
        for row in cursor:
            res.append(Corso(**row))

        #cursor.close()
        cnx.close()
        return res

if __name__ == '__main__':
    print(DAO.getCodins())
    for c in DAO.getAllCorsi():
        print(c)
