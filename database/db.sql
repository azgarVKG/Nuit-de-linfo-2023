CREATE TABLE IF NOT EXISTS Game(
    ID INTEGER PRIMARY KEY,
    Correct_response TEXT,
    Monster_dialog TEXT,
    Fake1 TEXT,
    Fake2 TEXT,
    Fake3 TEXT
);

CREATE TABLE IF NOT EXISTS Fact(
    ID INTEGER PRIMARY KEY,
    Info TEXT,
    full_text TEXT,
    source TEXT,
    FOREIGN KEY (ID)
        REFERENCES Game (ID)
);
