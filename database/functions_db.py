import sqlite3 as s

def insert_application_possible(datas):
    connection = s.connect("database\coraliotech_test_db.db")
    cursor = connection.cursor()
    query_format = "INSERT INTO Applications_possibles (nom) VALUES (\"{nom}\")"
    query = query_format.format(nom=datas["nom"])
    cursor.execute(query)
    connection.commit()
    connection.close()

def insert_organisme(datas):
    connection = s.connect("database\coraliotech_test_db.db")
    cursor = connection.cursor()
    query_format = "INSERT INTO Organisme VALUES " \
                   "(\"{espece}\", \"{genre}\", \"{famille}\", \"{ordre}\", \"{sous_classe}\", \"{classe}\", \"{embranchement}\", {statut})"
    query = query_format.format(espece=datas["espece"], genre=datas["genre"], famille=datas["famille"], ordre=datas["ordre"], sous_classe=datas["sous_classe"], classe=datas["classe"], embranchement=datas["embranchement"], statut=datas["statut"])
    cursor.execute(query)
    connection.commit()
    connection.close()

def get_applications_possibles():
    connection = s.connect("database\coraliotech_test_db.db")
    cursor = connection.cursor()
    query = "SELECT nom FROM Applications_possibles"
    cursor.execute(query)
    resultat = cursor.fetchall()
    connection.close()
    return resultat

