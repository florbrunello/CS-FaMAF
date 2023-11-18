/* Parcial 1 - Brunello, Florencia */

-- Ejercicio 1
ALTER TABLE `person` 
    ADD COLUMN `total_medals` INT DEFAULT 0;

-- Ejercicio 2
WITH total_medals AS (
    SELECT
        games_competitor.person_id as pid,
        count(competitor_event.medal_id) as total
    FROM
        competitor_event
    INNER JOIN games_competitor 
    ON
        competitor_event.competitor_id = games_competitor.id
    WHERE
        competitor_event.medal_id != 4
    GROUP BY
        games_competitor.person_id
)
UPDATE
	person
INNER JOIN total_medals 
ON
	person.id = total_medals.pid
SET
	person.total_medals = (
	SELECT
		total_medals.total
	FROM
		total_medals
	WHERE
		person.id = total_medals.pid);

-- Ejercicio 3
SELECT
    person.full_name,
    medal.medal_name,
    count(competitor_event.medal_id) as total
FROM
    competitor_event
INNER JOIN games_competitor
ON
    competitor_event.competitor_id = games_competitor.id
INNER JOIN person
ON
    games_competitor.person_id = person.id
INNER JOIN medal
ON
    competitor_event.medal_id = medal.id
INNER JOIN person_region 
ON 
    person_region.person_id = person.id 
INNER JOIN noc_region 
ON 
    noc_region.id = person_region.region_id 
WHERE
    noc_region.noc = 'ARG'
    AND 
    competitor_event.medal_id != 4
GROUP BY
    person.full_name,
    medal.medal_name
ORDER BY
    person.full_name,
    medal.medal_name;

-- Ejercicio 4
SELECT
    sport.sport_name,
    count(competitor_event.medal_id) as total 
FROM    
    competitor_event
INNER JOIN games_competitor
ON
    competitor_event.competitor_id = games_competitor.id
INNER JOIN person
ON
    games_competitor.person_id = person.id
INNER JOIN sport
ON
    competitor_event.event_id = sport.id
INNER JOIN person_region
ON
    person_region.person_id = person.id
INNER JOIN noc_region
ON
    noc_region.id = person_region.region_id
WHERE
    noc_region.noc = 'ARG'
GROUP BY
    sport.sport_name
ORDER BY
    sport.sport_name;

-- Ejercicio 5
SELECT
    noc_region.noc,
    medal.medal_name,
    count(competitor_event.medal_id) as total
FROM
    competitor_event
INNER JOIN games_competitor
ON
    competitor_event.competitor_id = games_competitor.id
INNER JOIN person
ON
    games_competitor.person_id = person.id
INNER JOIN person_region
ON
    person_region.person_id = person.id
INNER JOIN noc_region
ON
    noc_region.id = person_region.region_id
INNER JOIN medal
ON
    competitor_event.medal_id = medal.id
WHERE 
	competitor_event.medal_id != 4
GROUP BY
    noc_region.noc,
    medal.medal_name
ORDER BY
    noc_region.noc,
    medal.medal_name;

-- Ejercicio 6
(
SELECT
	noc_region.noc,
	count(competitor_event.medal_id) as total
FROM
	competitor_event
INNER JOIN games_competitor
ON
	competitor_event.competitor_id = games_competitor.id
INNER JOIN person
ON
	games_competitor.person_id = person.id
INNER JOIN person_region
ON
	person_region.person_id = person.id
INNER JOIN noc_region
ON
	noc_region.id = person_region.region_id
INNER JOIN medal
ON
	competitor_event.medal_id = medal.id
GROUP BY
	noc_region.noc
ORDER BY
	total DESC
LIMIT 1)
UNION 
(
SELECT
    noc_region.noc,
    count(competitor_event.medal_id) as total
FROM
    competitor_event
INNER JOIN games_competitor
ON
    competitor_event.competitor_id = games_competitor.id
INNER JOIN person
ON
    games_competitor.person_id = person.id
INNER JOIN person_region
ON
    person_region.person_id = person.id
INNER JOIN noc_region
ON
    noc_region.id = person_region.region_id
INNER JOIN medal
ON
    competitor_event.medal_id = medal.id
GROUP BY
    noc_region.noc
ORDER BY
    total
LIMIT 1);


-- Ejercicio 7
CREATE TRIGGER `increase_number_of_medals` 
    AFTER INSERT ON competitor_event
    FOR EACH ROW
BEGIN
	IF (competitor_event.medal_id != 4)
	BEGIN
		UPDATE person p
	    SET p.total_medals = p.total_medals + 1
	    WHERE p.id IN (
		   	SELECT gc.person_id
		   	FROM competitor_event ce 
		   	INNER JOIN games_competitor gc
		    ON ce.competitor_id = gc.person_id
		   	WHERE ce.competitor_id = NEW.competitor_id)
	END
 END;   

CREATE TRIGGER `decrease_number_of_medals` 
    AFTER DELETE ON competitor_event
    FOR EACH ROW
BEGIN
	IF (competitor_event.medal_id = 4)
	BEGIN
		UPDATE person p
	    SET p.total_medals = p.total_medals - 1
	    WHERE p.id IN (
		   	SELECT gc.person_id
		   	FROM competitor_event ce 
		   	INNER JOIN games_competitor gc
		    ON ce.competitor_id = gc.person_id
		   	WHERE ce.competitor_id = NEW.competitor_id)
	END
 END;

-- Ejercicio 8
CREATE OR REPLACE PROCEDURE `add_new_medalists` (IN event_id INT, 
IN g_id INT, IN s_id INT, IN b_id INT)
BEGIN 
	INSERT INTO `competitor_event` 
    (event_id, competitor_id, medal_id)
    VALUES (event_id, g_id, 1),
	       (event_id, s_id, 2),
	       (event_id, b_id, 3);
END;

-- Ejercicio 9
CREATE ROLE organizer;

GRANT DELETE ON games TO organizer;
GRANT UPDATE (games_name) ON games TO organizer;
