import sqlite3

database = sqlite3.connect("database/ndl.db")
databaseCursor = database.cursor()

def getData(table: str, column: str, parameter: str, parameterVal):
    if parameter == None:
        query = f"SELECT {column} FROM {table};"
        databaseCursor.execute(query)
        queryResult = databaseCursor.fetchall()
    else:
        query = f"SELECT {column} FROM {table} WHERE {parameter} = {parameterVal};"
        databaseCursor.execute(query)
        queryResult = databaseCursor.fetchone()
    return queryResult

def updateData(table: str, columns: str | list[str], newValues: list, parameter: str, parameterVal) -> bool:
    query = f"UPDATE {table} SET "
    for i in range(len(columns)):
        query += f"{columns[i]} = {newValues[i]}"
        if i == len(columns) - 1:
            query += " "
        else:
            query += ", "
    if parameter != None:
        query += f"WHERE {parameter} = {parameterVal};"
    databaseCursor.execute(query)
    return True

# Example
res = getData("NoFakes", "*", None, None)
print(res)