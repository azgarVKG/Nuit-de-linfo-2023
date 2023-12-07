CREATE TABLE IF NOT EXISTS Fact(
    ID INT PRIMARY KEY,
    Ennonce TEXT,
    src TEXT
);

CREATE TABLE IF NOT EXISTS NoFakes(
    ID INT PRIMARY KEY,
    Info TEXT,
    Proof TEXT
);

CREATE TABLE IF NOT EXISTS Fakes(
    ID INT PRIMARY KEY,
    Info TEXT,
    Proof1 TEXT,
    Proof2 TEXT,
    Proof3 TEXT
    FOREIGN KEY (ID)
        REFERENCES Fakes (ID)
);
