-- Cubo para agrupar ventas por pais
select 
COUNT(invoice.billingcountry)
, SUM(invoice.total)
, invoice.billingcountry 
from invoice 
group by cube (invoice.billingcountry);

-- Cubo para agrupar costumer por pais, state y company
select 
COUNT(customer.country)
, customer.country 
, customer.state 
, customer.company
from customer
group by cube (customer.country, customer.state, customer.company);

-- Cubo para agrupar track por genero
select 
COUNT(track.genreid)
, track.genreid 
, genre.name
from track
join genre on genre.genreid = track.genreid 
group by cube (track.genreid, genre.name);

-- Cubo para agrupar albums por artistas
select 
COUNT(album.artistid)
, album.artistid 
, artist.name 
from album
join artist on album.artistid = artist.artistid 
group by cube (album.artistid, artist.name);