--Ampliacion 1
SELECT week_of_year, sum, count
FROM ventasdatacube
WHERE year_actual IS NULL AND 
	quarter_actual IS NULL AND month_actual IS NULL AND genero IS NULL AND artista is null and 
	week_of_year IS NOT null and week_of_year >= 2 and week_of_year <= 8;
--ORDER BY count DESC
--LIMIT 10;

--Ampliacion 2
SELECT year_actual, artista, sum, count
FROM ventasdatacube
WHERE year_actual is NOT NULL AND 
	quarter_actual IS NULL AND month_actual IS NULL AND genero IS NULL AND artista is not null and 
	week_of_year IS NULL 
ORDER BY count DESC
LIMIT 10;

--Ampliacion 3
SELECT month_actual, genero , sum, count
FROM ventasdatacube
WHERE year_actual is NULL AND 
	quarter_actual IS NULL AND month_actual is not NULL AND genero IS not NULL AND artista is null and 
	week_of_year IS NULL 
ORDER BY count desc 
LIMIT 10;

--Ampliacion 3
SELECT month_actual, genero , sum, count
FROM ventasdatacube
WHERE year_actual is NULL AND 
	quarter_actual IS NULL AND month_actual is not NULL AND genero IS not NULL AND artista is null and 
	week_of_year IS NULL 
ORDER BY count desc 
LIMIT 10;