-- Parte I - DDL

-- Ejercicio 2
USE world;

CREATE TABLE country (
	Code CHAR(3),
	Name VARCHAR(255),
	Continent VARCHAR(255),
	Region VARCHAR(255),
	SurfaceArea INT,
	IndepYear INT,
	Population INT, 
	LifeExpectancy INT, 
	GNP INT, 
	GNPOld INT, 
	LocalName VARCHAR(255), 
	GovernmentForm VARCHAR(255),
	HeadOfState VARCHAR(255),
	Capital INT, 
	Code2 CHAR(2), 
	
	PRIMARY KEY (Code));

CREATE TABLE city (
  ID INT,
  Name VARCHAR(255),
  CountryCode CHAR(3),
  District VARCHAR(255),
  Population INT,
  
  PRIMARY KEY (ID),
  FOREIGN KEY (CountryCode) REFERENCES country(Code));

CREATE TABLE countrylanguage ( 
	CountryCode CHAR(3),
	Language VARCHAR(255),
	IsOfficial CHAR(1),
	Percentage double precision,
	
	PRIMARY KEY (CountryCode,Language),
	FOREIGN KEY (CountryCode) REFERENCES country(Code));

-- Ejercicio 4
CREATE TABLE continent (
	ContinentName VARCHAR(255),
	Area INT, 
	Mass double precision, 
	MostPopulatedCity INT,
	
	PRIMARY KEY (ContinentName),
	FOREIGN KEY (MostPopulatedCity) REFERENCES city(ID));

/* Ejercicio 5
- De esta manera obtuve los ID de las ciudades que se piden en el ejercicio 5
select ID from city where Name = 'Cairo';
select ID from city where Name = 'McMurdo Station';
select ID from city where Name = 'Mumbai (Bombay)';
select ID from city where Name = 'Istanbul';
select ID from city where Name = 'Ciudad de México';
select ID from city where Name = 'Sydney';
select ID from city where Name = 'São Paulo';

- Añadir las siguientes lineas a wold-data.sql
INSERT INTO `city` VALUES (4080,'McMurdo Station','AUS','New South Wales',3276207);

INSERT INTO `continent` VALUES ('Africa','30370000','20.4', 608);
INSERT INTO `continent` VALUES ('Antarctica','14000000','9.2', 4080);
INSERT INTO `continent` VALUES ('Asia','44579000','29.5', 1024);
INSERT INTO `continent` VALUES ('Europe','10180000','6.8', 3357);
INSERT INTO `continent` VALUES ('North America','24709000','16.5', 2515);
INSERT INTO `continent` VALUES ('Oceania','8600000','5.9', 130);
INSERT INTO `continent` VALUES ('South America','17840000','12.0', 206); */

-- Ejercicio 6
ALTER TABLE country ADD CONSTRAINT fk_continent_of_country FOREIGN KEY (Continent) REFERENCES continent(ContinentName);

-- Parte II - Consultas

-- Ejercicio 1
SELECT Name, Region 
FROM country 
ORDER BY name ASC;

-- Ejercicio 2
SELECT Name, Population 
FROM city 
ORDER BY Population 
DESC LIMIT 10;

-- Ejercicio 3
SELECT Name, Region, SurfaceArea, GovernmentForm 
FROM country 
ORDER BY surfaceArea ASC LIMIT 10;  

-- Ejercicio 4
SELECT Name 
FROM country 
WHERE IndepYear IS NULL;

-- Ejercicio 5
SELECT country.Name, countrylanguage.Percentage 
FROM country, countrylanguage 
WHERE countrylanguage.IsOfficial LIKE 'T';

SELECT country.Name, countrylanguage.Percentage 
FROM country, countrylanguage 
WHERE countrylanguage.IsOfficial = 'T';

-- Ejercicio 6
UPDATE
	countrylanguage
SET
	Percentage = 100.0
WHERE
	countryCode = 'AIA'
	AND `Language` = 'English'

-- Ejercicio 7
SELECT
	Name
FROM
	city
WHERE
	CountryCode = 'ARG'
	AND District = 'Córdoba';
    
-- Ejercicio 8
delete
from
	city
where
	District = 'Cordoba'
	and CountryCode != 'ARG';
    
-- Ejercicio 9
SELECT Name 
FROM country 
WHERE HeadOfState LIKE 'John%'

-- Ejercicio 10
SELECT
	name
FROM
	country
WHERE
	Population BETWEEN 35000000 AND 45000000
ORDER BY
	population DESC
