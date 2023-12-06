import json


def getData() -> dict:

    """
    Récupérer les données dans la base de données

    -- Returns --
    - data `dict` : Le dictionnaire des données
    """

    with open("database/data.json", "r", encoding="utf-8-sig") as file: data = json.load(file)
    return data

def saveData(data: dict):

    """
    Sauvegarder les données dans la base de données

    -- Parameters --
    - data `dict` : Le dictionnaire des données
    """

    with open("database/data.json", "w", encoding="utf-8") as file: json.dump(data, file, indent=4, ensure_ascii=False)