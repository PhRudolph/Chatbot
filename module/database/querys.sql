CREATE TABLE errorRequests(requestId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, requestText TEXT NOT NULL)  

INSERT INTO errorRequests (requestText)
VALUES ("Testeingabe")

SELECT * FROM errorRequests

DROP TABLE errorRequests