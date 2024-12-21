-- Parte 1 - Consultas

-- Ejercicio 1
SELECT city.Name, country.Name, country.Region, country.GovernmentForm
FROM city, country
ORDER BY city.Population 
DESC LIMIT 10; 

-- Ejercicio 2
SELECT country.Name, city.Name
FROM country INNER JOIN city 
ON city.ID = country.Capital
ORDER BY country.Population ASC LIMIT 10;

-- Ejercicio 3
SELECT country.Name, country.Continent, countrylanguage.Language 
FROM country 
INNER JOIN countrylanguage
ON countrylanguage.CountryCode  = country.Code
WHERE countrylanguage.IsOfficial = 'T';

-- Ejercicio 4
SELECT country.Name, city.Name
FROM country INNER JOIN city 
ON city.ID = country.Capital
ORDER BY country.SurfaceArea DESC LIMIT 20;  

-- Ejercicio 5
SELECT city.Name, countrylanguage.Language, countrylanguage.Percentage  
FROM city 
INNER JOIN countrylanguage
ON city.CountryCode = countrylanguage.CountryCode
WHERE countrylanguage.IsOfficial = 'T'
ORDER BY city.Population ASC;

-- Ejercicio 6
(SELECT Name FROM country WHERE Population > 100 ORDER BY Population ASC LIMIT 10) 
UNION 
(SELECT Name FROM country WHERE Population > 100 ORDER BY Population DESC LIMIT 10);

-- Ejercicio 7
(SELECT country.Name FROM country INNER JOIN countrylanguage ON countrylanguage.CountryCode = country.Code WHERE (countrylanguage.Language = 'English' AND countrylanguage.IsOfficial = 'T')) 
INTERSECT 
(SELECT country.Name FROM country INNER JOIN countrylanguage ON countrylanguage.CountryCode = country.Code WHERE (countrylanguage.Language = 'French' AND countrylanguage.IsOfficial = 'T'));

-- Ejercicio 8
(SELECT country.Name FROM country INNER JOIN countrylanguage ON countrylanguage.CountryCode = country.Code WHERE countrylanguage.Language = 'English') 
EXCEPT 
(SELECT country.Name FROM country INNER JOIN countrylanguage ON countrylanguage.CountryCode = country.Code WHERE countrylanguage.Language = 'Spanish');

-- Parte 2 - Preguntas

/* a) Si, devuelven lo mismo 

   b) No, no es lo mismo: 

    Caso a) SELECT city.Name, country.Name
            FROM city
            LEFT JOIN country ON city.CountryCode = country.Code AND country.Name = 'Argentina';
            En este caso, si no se cumple la condicion, agrega el pais igual con null. 

    Caso b) SELECT city.Name, country.Name
            FROM city
            LEFT JOIN country ON city.CountryCode = country.Code
            WHERE country.Name = 'Argentina';
            En este caso, primero matchea city.CountryCode = country.Code y luego 
            filtra por el where. */
