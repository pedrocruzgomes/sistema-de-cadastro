import sqlite3

class DataBase:
    def __init__(self, name = "system.db") -> None:
        self.name = name

    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def closeConnection(self):
        try:
            self.connection.close()
        except:
            pass

    def create_table_pessoas(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Pessoas(

            NOME TEXT,
            CPF TEXT,
            NASC TEXT,
            TELEFONE TEXT,
            EMAIL TEXT,
            CIDADE TEXT,
            RUA TEXT,
            BAIRRO TEXT,
            NUMERO TEXT,
            
            PRIMARY KEY(CPF)
        );""")

    def registrar_pessoa(self, fullDataSet):
        campos_tabela = ("NOME", "CPF", "NASC", "TELEFONE", "EMAIL", "CIDADE", "RUA", "BAIRRO", "NUMERO")
        qntd = ("?,?,?,?,?,?,?,?,?")
        cursor = self.connection.cursor()

        try:
            cursor.execute(f"""INSERT INTO Pessoas {campos_tabela}
            VALUES({qntd})""", fullDataSet)
            self.connection.commit()
            return("OK")

        except:
            return "Erro"

    def select_all_pessoas(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Pessoas ORDER BY NOME")
            pessoas = cursor.fetchall()
            return pessoas

        except:
            pass

    def delete_pessoa(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Pessoas WHERE CPF = '{id}' ")
            self.connection.commit()
            return "Cadastro de pessoa excluido com sucesso!"

        except:
            return "Erro ao excluir registo!"

    def update_pessoa(self, fullDataSet):
            cursor = self.connection.cursor()
            cursor.execute(f""" UPDATE Pessoas set
                
                NOME = "{fullDataSet[0]}",
                CPF = "{fullDataSet[1]}",
                NASC = "{fullDataSet[2]}",
                TELEFONE = "{fullDataSet[3]}",
                EMAIL = "{fullDataSet[4]}",
                CIDADE = "{fullDataSet[5]}",
                RUA = "{fullDataSet[6]}",
                BAIRRO = "{fullDataSet[7]}",
                NUMERO = "{fullDataSet[8]}"
                
                WHERE CPF = "{fullDataSet[1]}" """)

            self.connection.commit()