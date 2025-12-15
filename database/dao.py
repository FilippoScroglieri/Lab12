from database.DB_connect import DBConnect
from model.rifugio import Rifugio
from model.sentiero import Sentiero


class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO
    @staticmethod
    def read_rifugi():
        conn= DBConnect.get_connection()
        result= {}
        cursor = conn.cursor(dictionary=True)
        query= "SELECT * FROM rifugio"
        cursor.execute(query)
        for row in cursor:
            result[row["id"]] = Rifugio(**row)
        cursor.close()
        conn.close()
        return result
    @staticmethod
    def read_sentieri():
        conn= DBConnect.get_connection()
        result= []
        cursor = conn.cursor(dictionary=True)
        query= "SELECT * FROM connessione"
        cursor.execute(query)
        for row in cursor:
            result.append(Sentiero(**row))
        cursor.close()
        conn.close()
        return result
