CREATE TABLE IF NOT EXISTS Fakes(
    ID INT PRIMARY KEY,
    Info TEXT,
    Proof TEXT
);

INSERT INTO Fakes
(ID, Info, Proof)
VALUES
(1, '',''),
(2, '',''),
(3, '',''),
(4, '','');


CREATE TABLE IF NOT EXISTS NoFakes(
    ID INT PRIMARY KEY,
    Info TEXT,
    Proof1 TEXT,
    Proof2 TEXT,
    Proof3 TEXT
    FOREIGN KEY (ID)
);

INSERT INTO NoFakes
(ID, Info, Proof1, Proof2, Proof3)
VALUES
(1, '','','',''),
(2, '','','',''),
(3, '','','',''),
(4, '','','','');