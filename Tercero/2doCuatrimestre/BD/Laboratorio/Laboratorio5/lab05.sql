-- Consultas

-- Ejercicio 1
CREATE TABLE directors (
	director_id INT NOT NULL AUTO_INCREMENT,
	first_name varchar(255),
	last_name varchar(255),
	number_movies INT, 
	
	PRIMARY KEY (director_id)
)

-- Ejercicio 2
INSERT
	INTO
	directors (first_name,
	last_name,
	number_movies)
SELECT
	actor.first_name,
	actor.last_name,
	top5.cf
FROM
	actor
INNER JOIN 
(
	SELECT
		actor_id,
		count(film_id) as cf
	FROM
		film_actor
	GROUP BY
		actor_id
	ORDER BY
		cf DESC
	LIMIT 5) as top5
ON
	actor.actor_id = top5.actor_id;


-- Ejercicio 3
ALTER TABLE customer 
ADD COLUMN premium_customer char(1) DEFAULT 'F';

-- Ejercicio 4
SELECT
	customer_id
FROM
(
	SELECT
		customer_id
	FROM
		payment
	GROUP BY
		customer_id
	ORDER BY
		sum(amount) DESC
	LIMIT 10) as top10


UPDATE
	customer
SET
	premium_customer = 'T'
WHERE
	customer_id IN (
	SELECT
		customer_id
	FROM
		(
		SELECT
			customer_id
		FROM
			payment
		GROUP BY
			customer_id
		ORDER BY
			sum(amount) DESC
		LIMIT 10) as top10)

-- Ejercicio 5
SELECT rating, count(*) AS count
FROM film
GROUP BY rating
ORDER BY count DESC; 

-- Ejercicio 6
SELECT
	min(payment_date),
	max(payment_date)
FROM
	payment;

-- Ejercicio 7
SELECT
	month(payment_date) AS mes ,
	COUNT(payment_id) AS Cantidad_pagos
FROM
	payment
GROUP BY
	mes;

SELECT
	month(payment_date) as month,
	avg(amount) as promedio
FROM
	payment
GROUP BY
	month
ORDER BY
	month

-- Ejercicio 8
WITH district_by_customer AS
(
select
	district,
	c.customer_id
from
	(address as a
inner join customer as c on
	a.address_id = c.address_id))
SELECT
	district,
	count(*) as rentals
FROM
	(district_by_customer as dc
inner join rental as r on
	dc.customer_id = r.customer_id)
group by
	district
order by 
	rentals 
DESC 
limit 10;

-- Ejercicio 9
ALTER TABLE inventory
ADD stock INT DEFAULT 5;

-- Ejercicio 10
CREATE TRIGGER update_stock AFTER
INSERT
	ON
	rental FOR EACH ROW 
BEGIN 
	UPDATE
	inventory i
SET
	i.stock = i.stock -1
WHERE
	i.inventory_id = NEW.inventory_id;
END

-- Ejercicio 11
CREATE TABLE fines (
	fines_id INT NOT NULL AUTO_INCREMENT, 	
	rental_id INT,
	amount numeric(10,2),

	PRIMARY KEY (fines_id),
	FOREIGN KEY (rental_id) REFERENCES rental(rental_id) 
)

-- Ejercicio 12
CREATE PROCEDURE check_date_and_fine ()
BEGIN 	
	INSERT
	INTO
	fines (rental_id,
	amount)
	(
	SELECT
		rental_id,
		DATEDIFF(return_date, rental_date)* 1.5
	FROM
		rental
	WHERE
		DATEDIFF(return_date, rental_date) > 3);
END

CALL check_date_and_fine();

-- Ejercicio 13
CREATE ROLE employee;
GRANT INSERT, UPDATE, DELETE
ON rental
TO employee;
SHOW GRANTS FOR employee

revoke DELETE 
ON rental 
FROM employee;

-- Ejercicio 14
CREATE ROLE administrator;
GRANT ALL ON sakila.* TO administrator;

show grants for employee;
show grants for administrator;

-- Ejercicio 15
CREATE ROLE type1employee;
CREATE ROLE type2employee;

grant employee to type1employee;
grant administrator to type2employee;

show grants for type1employee;
show grants for type2employee;
