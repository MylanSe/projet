CREATE TABLE Refuge (
   idRefuge INTEGER PRIMARY KEY AUTOINCREMENT,
   nomRefuge VARCHAR(50) NOT NULL,
   Location VARCHAR(50) NOT NULL
);
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE Animal (
   idAnimal INTEGER PRIMARY KEY AUTOINCREMENT,
   espece VARCHAR(50) NOT NULL,
   nom VARCHAR(50) NOT NULL,
   dateNaissance DATE NOT NULL,
   sexe VARCHAR(50) NOT NULL,
   tailleCm INT NOT NULL,
   disponible BOOLEAN, 
   idRefuge INT NOT NULL, idLogin INTEGER REFERENCES Login(idLogin) ON DELETE SET NULL,
   FOREIGN KEY(idRefuge) REFERENCES Refuge(idRefuge)
);
CREATE TABLE Login (
   idLogin INTEGER PRIMARY KEY AUTOINCREMENT,
   mail TEXT NOT NULL UNIQUE,
   password TEXT NOT NULL);
);

INSERT INTO Refuge VALUES(1,'A 4 pattes','Lyon');
INSERT INTO Refuge VALUES(2,'Chapristi','Talencieux');
INSERT INTO Refuge VALUES(3,'Lbo bestiau','Paris');

INSERT INTO Animal VALUES(1,'chat','Garfield','2020-01-01','male',100,0,2,NULL);
INSERT INTO Animal VALUES(2,'chien','Rantanplan','2020-01-01','male',140,1,3,NULL);
INSERT INTO Animal VALUES(3,'elephant','Dumbo','1900-10-02','male',700,1,1,NULL);
INSERT INTO Animal VALUES(4,'chat','Hello Kitty','2023-08-31','femelle',40,1,1,NULL);
INSERT INTO Animal VALUES(5,'exotique','Unicorn','2021-12-17','femelle',250,1,3,NULL);
INSERT INTO Animal VALUES(6,'exotique','Flappy','2017-05-13','male',120,1,2,NULL);


INSERT INTO Login VALUES(1,'mailTest','passwordTest');