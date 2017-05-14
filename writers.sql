DROP TABLE Writers;

CREATE TABLE IF NOT EXISTS Writers(ID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(25)) ENGINE = INNODB;

INSERT INTO Writers(Name) VALUES('Jack London');
INSERT INTO Writers(Name) VALUES('Honore de Balzac');
INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger');
INSERT INTO Writers(Name) VALUES('Emile Zola');
INSERT INTO Writers(Name) VALUES('Truman Capote');
