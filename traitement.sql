CREATE TABLE IF NOT EXISTS donne(
    nom TEXT PRIMARY KEY,
    pwd TEXT  NOT NULL
);

CREATE TABLE IF NOT EXISTS coord(
    mail TEXT PRIMARY KEY, 
    nom NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS compte(
    mail TEXT NOT NULL, 
    nom TEXT NOT NULL,
    solde INTEGER NOT NULL,
    PRIMARY KEY (mail, nom)
);
