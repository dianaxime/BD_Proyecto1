--Ampliacion 1
-- MEte weekOFtheYear, imprimo first and last
SELECT week_of_year, first_day_of_week, last_day_of_week, sum, count
FROM ventasdatacube
WHERE year_actual = 2009 AND
	quarter_actual IS NULL AND month_actual IS NULL AND genero IS NULL AND artista is null and 
	week_of_year IS NOT null and week_of_year >= 2 and week_of_year <= 8
AND date_actual IS null AND first_day_of_week IS not null AND last_day_of_week is not NULL;
--ORDER BY count DESC
--LIMIT 10;

--Ampliacion 2
SELECT date_actual, artista, sum, count
FROM ventasdatacube
WHERE year_actual is NULL AND 
	quarter_actual IS NULL AND month_actual is NULL AND genero IS NULL AND artista is not null and 
	week_of_year IS NULL AND first_day_of_week IS null AND last_day_of_week is null
	and date_actual >= '2009-09-10' and date_actual <= '2009-10-12' 
ORDER BY date_actual asc;
-- LIMIt N por user

--Ampliacion 3
SELECT date_actual, genero, sum,count
FROM ventasdatacube
WHERE year_actual is NULL AND 
	quarter_actual IS NULL AND month_actual is NULL AND genero IS not NULL AND artista is null and 
	week_of_year IS NULL AND first_day_of_week IS null AND last_day_of_week is null
	and date_actual >= '2009-09-10' and date_actual <= '2009-10-12'
ORDER BY date_actual asc;
--LIMIT 25;


--Ampliacion 4
SELECT reproduccion.trackid, artist.name, track.name, COUNT(reproduccion.trackid)
from reproduccion 
join track on track.trackid = reproduccion.trackid 
join album on album.albumid = track.albumid 
join artist on artist.artistid = album.artistid 
where artist.name = 'Apocalyptica'
group by reproduccion.trackid, artist.name, track.name;