-- Parte I - Consultas

-- Ejercicio 1
SELECT
	city.name,
	country.Name
FROM
	city
INNER JOIN country ON
	city.CountryCode = country.Code
WHERE
	country.Population < 10000


-- Ejercicio 2
SELECT
	city.Name
FROM
	city
WHERE
	city.Population > (
	SELECT
		avg(Population)
	FROM
		city)

-- Ejercicio 3
SELECT
	city.Name
FROM
	city
WHERE
	(city.CountryCode NOT IN 
	(
	SELECT
		Code
	FROM
		country
	WHERE
		Continent = 'Asia'))
	AND 
	(city.Population >= SOME 
	(
	SELECT
		population
	FROM
		country
	WHERE
		country.continent = 'Asia'))

-- Ejercicio 4
SELECT
	c.Name,
	cl1.Language
FROM
	country c
INNER JOIN countrylanguage cl1 ON
	c.Code = cl1.CountryCode
WHERE
	cl1.IsOfficial = 'F'
	AND
	cl1.Percentage >= ALL
					(
	SELECT
		cl2.Percentage
	FROM
		countrylanguage AS cl2
	WHERE
					cl2.IsOfficial = 'T'
		AND c.Code = cl2.CountryCode)

-- Ejercicio 5
SELECT
	DISTINCT c.Region
FROM
	country AS c
INNER JOIN city AS c2 ON
	c2.CountryCode = c.Code
WHERE
	c.SurfaceArea < 1000
	AND c2.Population > 10000

-- Ejercicio 6
SELECT
	country.Name,
	max(city.Population)
FROM
	country
INNER JOIN city ON
	country.Code = city.CountryCode
GROUP BY
	country.Code

-- Ejercicio 7
SELECT
	country.Name,
	countrylanguage.Language
FROM country INNER JOIN countrylanguage ON country.Code = countrylanguage.CountryCode 
WHERE
	countrylanguage.IsOfficial = 'F'
	AND countrylanguage.Percentage > (
	SELECT
		AVG(countrylanguage.Percentage)
	FROM
		country
	INNER JOIN 
countrylanguage ON
		countrylanguage.CountryCode = country.Code
		WHERE countrylanguage.IsOfficial = 'T')

-- Ejercicio 8
SELECT
	c.continent,
	sum(c.Population) AS habitantes
FROM
	country c
GROUP BY
	continent
ORDER BY
	habitantes DESC;

-- Ejercicio 9
SELECT country.continent, avg(country.LifeExpectancy) as EdV
FROM country
GROUP BY continent 
HAVING (EdV > 40 AND EdV < 70)

-- Ejercicio 10
SELECT
	c.continent,
	max(c.Population) AS max, 
	min(c.Population) AS min,
	avg(c.Population) AS avg, 
	sum(c.Population) AS sum
FROM
	country c
GROUP BY
	continent

-- Parte II - Preguntas

SELECT  c.name AS Pais , 
		(SELECT max(ci.Population) FROM city ci WHERE ci.CountryCode = c.Code) AS maxPop,
		(SELECT ci.Name FROM city ci WHERE ci.Population=maxPop AND ci.CountryCode=c.Code) AS Nombre
FROM country c ORDER BY maxPop DESC;