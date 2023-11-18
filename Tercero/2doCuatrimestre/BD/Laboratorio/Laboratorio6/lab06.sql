-- Consultas 

-- Ejercicio 1
SELECT
	officeCode,
	city,
	employees
FROM (
	SELECT
		o.*,
		COUNT(1) as employees
	FROM
		(offices o
	JOIN employees e
		ON
		o.officeCode = e.officeCode)
	GROUP BY
		o.officeCode
) as employeesPerOffice
ORDER BY
	employees DESC
LIMIT 1;

-- Ejercicio 2
SELECT
	off.officeCode,
	AVG(amount) AS average
FROM
	(((payments p
JOIN customers c ON
	p.customerNumber = c.customerNumber)
JOIN employees e ON
	c.salesRepEmployeeNumber = e.employeeNumber)
JOIN offices off ON
	e.officeCode = off.officeCode)
GROUP BY
	off.officeCode;

SELECT
	off.officeCode,
	off.city,
	COUNT(*) amountSales
FROM
	((((orderdetails o2
JOIN orders o ON
	o2.orderNumber = o.orderNumber)
JOIN customers c ON
	c.customerNumber = o.customerNumber)
JOIN employees e ON
	e.employeeNumber = c.salesRepEmployeeNumber)
JOIN offices off ON
	off.officeCode = e.officeCode)
GROUP BY
	off.officeCode
ORDER BY
	amountSales DESC
LIMIT 1;

-- Ejercicio 3
SELECT
	YEAR(paymentDate) AS pyear,
	MONTH(paymentDate) AS pmonth,
	AVG(amount),
	MIN(amount),
	MAX(amount)
FROM
	payments p
GROUP BY
	pmonth,
	pyear
ORDER BY
	pyear,
	pmonth;

-- Ejercicio 4
CREATE PROCEDURE update_credit(IN clientNumber INT, IN newLimit INT)
BEGIN
	UPDATE
	customers
SET
	creditLimit = newLimit
WHERE
	customerNumber = clientNumber;
END;

-- Ejercicio 5
CREATE OR REPLACE VIEW classicmodels.premium_customers
SELECT c.customerName, c.city, tc.amount
FROM (customers c
	JOIN (
		SELECT p.customerNumber, SUM(amount) AS amount
		FROM (customers c2
			JOIN payments p 
			ON c2.customerNumber = p.customerNumber)
		GROUP BY customerNumber) AS tc
	ON c.customerNumber = tc.customerNumber)
ORDER BY amount DESC
LIMIT 10;

-- Ejercicio 6
CREATE FUNCTION employee_of_the_month(chosenMonth INT, chosenYear INT)
RETURNS VARCHAR(255)
BEGIN
	DECLARE employeeName VARCHAR(100);
	DECLARE maxOrderCount INT;
	
    SELECT CONCAT(e.firstName, " ", e.lastName) AS name, COUNT(*) orderCount
    INTO employeeName, maxOrderCount
	FROM ((orders o
		JOIN customers c ON o.customerNumber = c.customerNumber)
		JOIN employees e ON c.salesRepEmployeeNumber = e.employeeNumber)
	WHERE MONTH(o.orderDate) = chosenMonth AND YEAR(o.orderDate) = chosenYear
	GROUP BY name
	ORDER BY orderCount DESC LIMIT 1;

	RETURN employeeName;
END;

-- Ejercicio 7
CREATE TABLE refillment (
	refillmentID INT PRIMARY KEY AUTO_INCREMENT,
	productCode VARCHAR(15),
	orderDate DATE,
	quantity INT,
	FOREIGN KEY (productCode) REFERENCES products(productCode)
);

-- Ejercicio 8
CREATE TRIGGER restock_product
AFTER INSERT ON orderdetails
FOR EACH ROW
BEGIN
	DECLARE amountStock INT;

	SELECT quantityInStock 
	INTO amountStock
	FROM products p
	WHERE p.productCode = NEW.productCode;
	
	IF (amountStock - NEW.quantityOrdered < 10) THEN
		INSERT INTO refillment (productCode, orderDate, quantity)
		VALUES (NEW.productCode, CURDATE(), 10);
	END IF;
END;

-- Ejercicio 9
CREATE ROLE IF NOT EXISTS employee;
GRANT SELECT ON classicmodels.* TO employee;
GRANT CREATE VIEW ON classicmodels.* TO employee;

