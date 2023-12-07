import sqlite3

database = sqlite3.connect("database/ndl.db")
databaseCursor = database.cursor()

def getData(table: str, column: str, id: int):
    if id == None:
        query = f"SELECT {column} FROM {table}"
        databaseCursor.execute(query)
        queryResult = databaseCursor.fetchall()
    else:
        query = f"SELECT {column} FROM {table} WHERE id = {id}"
        databaseCursor.execute(query)
        queryResult = databaseCursor.fetchone()
    return queryResult

res = getData("NoFakes", "Proof1", 0)
print(res)