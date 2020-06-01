drop table if exists bitacora cascade;
create table bitacora(
	bitacora_id serial primary key,
	nombre_object varchar(200) not null,
	email varchar(30) not null,
	accion varchar(30) not null,
	tipo varchar(30) not null,
	date_on TIMESTAMP NOT NULL
);
--DROP FUNCTION add_bitacora(varchar,varchar, numeric, numeric);
CREATE OR REPLACE FUNCTION add_bitacora(id_usuario numeric, nombre_object varchar, tipo numeric, objeto numeric) 
returns void AS
$$
	declare 
		accion varchar;
		tipoObj varchar;
		email varchar;
begin
	if tipo=1 then 
		accion:='add';
	elseif tipo=2 then 
		accion:='update';
	elseif tipo=3 then 
		accion:='delete';
	end if;
	if objeto=1 then 
		tipoObj:='track';
	elseif objeto=2 then 
		tipoObj:='album';
	elseif objeto=3 then 
		tipoObj:='playlist';
	elseif objeto=4 then 
		tipoObj:='artist';
	end if;
	email:= (select customer.email from customer where customerid=id_usuario);
	INSERT INTO Bitacora (nombre_object, email, accion, tipo, date_on) VALUES (nombre_object, email, accion, tipoObj, now());
END;
$$
LANGUAGE 'plpgsql';

DROP INDEX IF EXISTS bitacora_index; 
CREATE INDEX bitacora_index ON bitacora(accion, tipo);

select nombre_object, email, accion, tipo, date_on from bitacora where accion='delete' order by date_on DESC;

select nombre_object, email, accion, tipo, date_on from bitacora where accion='add' order by date_on DESC;

select nombre_object, email, accion, tipo, date_on from bitacora where accion='update' order by date_on DESC;

--alteracion de tablas por bitacora
alter table track add column u_added INT references customer(customerid);
alter table track add column u_deleted INT references customer(customerid);
alter table track add column u_updated INT references customer(customerid);

alter table artist add column u_added INT references customer(customerid);
alter table artist add column u_deleted INT references customer(customerid);
alter table artist add column u_updated  INT references customer(customerid);

alter table album add column u_added INT references customer(customerid);
alter table album add column u_deleted INT references customer(customerid);
alter table album add column u_updated  INT references customer(customerid);

alter table playlist add column u_added INT references customer(customerid);
alter table playlist add column u_deleted INT references customer(customerid);
alter table playlist add column u_updated  INT references customer(customerid);


--funciones
CREATE OR REPLACE FUNCTION add_album_bitacora()
RETURNS trigger AS
$$
	declare 
		email varchar;
begin
	email:=(select customer.email from customer where customerid=new.u_added);
	INSERT INTO Bitacora (nombre_object, email, accion, tipo, date_on)
	VALUES (NEW.title, email, 'add', 'album', now());
	
RETURN NEW;
END;
$$
LANGUAGE 'plpgsql';
--
CREATE OR REPLACE FUNCTION add_playlist_bitacora()
RETURNS trigger AS
$$
	declare 
		email varchar;
begin
	email:=(select customer.email from customer where customerid=new.u_added);
	INSERT INTO Bitacora (nombre_object, email, accion, tipo, date_on)
	VALUES (NEW.name, email, 'add', 'playlist', now());
	
RETURN NEW;
END;
$$
LANGUAGE 'plpgsql';
--
CREATE OR REPLACE FUNCTION add_artist_bitacora()
RETURNS trigger AS
$$
	declare 
		email varchar;
begin
	email:=(select customer.email from customer where customerid=new.u_added);
	INSERT INTO Bitacora (nombre_object, email, accion, tipo, date_on)
	VALUES (NEW.name, email, 'add', 'artist', now());
	
RETURN NEW;
END;
$$
LANGUAGE 'plpgsql';
--
CREATE OR REPLACE FUNCTION add_track_bitacora()
RETURNS trigger AS
$$
	declare 
		email varchar;
begin
	email:=(select customer.email from customer where customerid=new.u_added);
	INSERT INTO Bitacora (nombre_object, email, accion, tipo, date_on)
	VALUES (NEW.name, email, 'add', 'track', now());
	
RETURN NEW;
END;
$$
LANGUAGE 'plpgsql';
--
CREATE OR REPLACE FUNCTION update_track_bitacora()
RETURNS trigger AS
$$
	declare 
		email varchar;
begin
	email:=(select customer.email from customer where customerid=new.u_updated);
	INSERT INTO Bitacora (nombre_object, email, accion, tipo, date_on)
	VALUES (NEW.name, email, 'update', 'track', now());
	INSERT INTO track_historial (oldname, newname, oldalbumid, newalbumid, oldmediatypeid, newmediatypeid, oldgenreid, newgenreid, oldcomposer, newcomposer, oldmilli, newmilli, oldbytes, newbytes, oldup, newup, usuario_email)
	VALUES (old.name, new.name, old.albumid, new.albumid, old.mediatypeid, new.mediatypeid, old.genreid, new.genreid, old.composer, new.composer, old.milliseconds, new.milliseconds, old.bytes, new.bytes, old.unitprice, new.unitprice, email);
	
RETURN NEW;
END;
$$
LANGUAGE 'plpgsql';
--
CREATE OR REPLACE FUNCTION update_album_bitacora()
RETURNS trigger AS
$$
	declare 
		email varchar;
begin
	email:=(select customer.email from customer where customerid=new.u_updated);
	INSERT INTO Bitacora (nombre_object, email, accion, tipo, date_on)
	VALUES (NEW.title, email, 'update', 'album', now());
	INSERT INTO album_historial (oldtitle, newtitle, oldartistid, newartistid, usuario_email )
	VALUES (old.title, new.title, old.artistid,  new.artistid, email);
	
RETURN NEW;
END;
$$
LANGUAGE 'plpgsql';
--
CREATE OR REPLACE FUNCTION update_artist_bitacora()
RETURNS trigger AS
$$
	declare 
		email varchar;
begin
	email:=(select customer.email from customer where customerid=new.u_updated);
	INSERT INTO Bitacora (nombre_object, email, accion, tipo, date_on)
	VALUES (NEW.name, email, 'update', 'artist', now());
	INSERT INTO artist_historial (oldname, newname, usuario_email )
	VALUES (old.name, new.name, email);
RETURN NEW;
END;
$$
LANGUAGE 'plpgsql';
--
CREATE OR REPLACE FUNCTION update_playlist_bitacora()
RETURNS trigger AS
$$
	declare 
		email varchar;
begin
	email:=(select customer.email from customer where customerid=new.u_updated);
	INSERT INTO Bitacora (nombre_object, email, accion, tipo, date_on)
	VALUES (NEW.name, email, 'update', 'playlist', now());
	
RETURN NEW;
END;
$$
LANGUAGE 'plpgsql';
--
CREATE OR REPLACE FUNCTION delete_track_bitacora()
RETURNS trigger AS
$$
	declare 
		email varchar;
begin
	email:=(select customer.email from customer where customerid=old.u_deleted);
	INSERT INTO Bitacora (nombre_object, email, accion, tipo, date_on)
	VALUES (OLD.name, email, 'delete', 'track', now());
	
RETURN OLD;
END;
$$
LANGUAGE 'plpgsql';
--
CREATE OR REPLACE FUNCTION delete_album_bitacora()
RETURNS trigger AS
$$
	declare 
		email varchar;
begin
	email:=(select customer.email from customer where customerid=old.u_deleted);
	INSERT INTO Bitacora (nombre_object, email, accion, tipo, date_on)
	VALUES (OLD.title, email, 'delete', 'album', now());
	
RETURN OLD;
END;
$$
LANGUAGE 'plpgsql';
--
CREATE OR REPLACE FUNCTION delete_playlist_bitacora()
RETURNS trigger AS
$$
	declare 
		email varchar;
begin
	email:=(select customer.email from customer where customerid=old.u_deleted);
	INSERT INTO Bitacora (nombre_object, email, accion, tipo, date_on)
	VALUES (OLD.name, email, 'delete', 'playlist', now());
	
RETURN OLD;
END;
$$
LANGUAGE 'plpgsql';
--
CREATE OR REPLACE FUNCTION delete_artist_bitacora()
RETURNS trigger AS
$$
	declare 
		email varchar;
begin
	email:=(select customer.email from customer where customerid=old.u_deleted);
	INSERT INTO Bitacora (nombre_object, email, accion, tipo, date_on)
	VALUES (OLD.name, email, 'delete', 'artist', now());
	
RETURN OLD;
END;
$$
LANGUAGE 'plpgsql';

--trigger insert
CREATE TRIGGER insert_track
BEFORE insert 
ON track
FOR EACH ROW
EXECUTE PROCEDURE add_track_bitacora();

CREATE TRIGGER insert_album
BEFORE insert 
ON album
FOR EACH ROW
EXECUTE PROCEDURE add_album_bitacora();

CREATE TRIGGER insert_playlist
BEFORE insert 
on playlist
FOR EACH ROW
EXECUTE PROCEDURE add_playlist_bitacora();

CREATE TRIGGER insert_artist
BEFORE insert 
ON artist
FOR EACH ROW
EXECUTE PROCEDURE add_artist_bitacora();

--triggers update
CREATE TRIGGER update_track
BEFORE update
ON track
FOR EACH ROW
EXECUTE PROCEDURE update_track_bitacora();

CREATE TRIGGER update_album
BEFORE update
ON album
FOR EACH ROW
EXECUTE PROCEDURE update_album_bitacora();

CREATE TRIGGER update_playlist
BEFORE update
on playlist
FOR EACH ROW
EXECUTE PROCEDURE update_playlist_bitacora();

CREATE TRIGGER update_artist
BEFORE update
ON artist
FOR EACH ROW
EXECUTE PROCEDURE update_artist_bitacora();

--triggers delete
CREATE TRIGGER delete_track
BEFORE delete
ON track
FOR EACH ROW
EXECUTE PROCEDURE delete_track_bitacora();

CREATE TRIGGER delete_album
BEFORE delete
ON album
FOR EACH ROW
EXECUTE PROCEDURE delete_album_bitacora();

CREATE TRIGGER delete_playlist
BEFORE delete
on playlist
FOR EACH ROW
EXECUTE PROCEDURE delete_playlist_bitacora();

CREATE TRIGGER delete_artist
BEFORE delete
ON artist
FOR EACH ROW
EXECUTE PROCEDURE delete_artist_bitacora();

--para video de las canciones
alter table track add column link_video VARCHAR(400);
create table carrito(
	carrito_id serial primary key,
	date_on TIMESTAMP NOT NULL,
	state varchar(30) not null,
	customerid INT NOT NULL,
	trackid INT NOT NULL,
    FOREIGN KEY (trackid) REFERENCES track(trackid),
    FOREIGN KEY (customerid) REFERENCES customer(customerid)
);

--tabla de reproduccion
drop table if exists reproducción cascade;
create table reproduccion(
	reproduccion_id serial primary key,
	trackid INT NOT NULL,
    FOREIGN KEY (trackid) REFERENCES track(trackid)
);

--guardar updates
drop table if exists track_historial;
create table track_historial(
	id serial primary key,
	oldname varchar(200),
	newname varchar(200),
	oldalbumid int,
	newalbumid int,
	oldmediatypeid int,
	newmediatypeid int,
	oldgenreid int,
	newgenreid int,
	oldcomposer varchar(220),
	newcomposer varchar(220),
	oldmilli int,
	newmilli int,
	oldbytes int,
	newbytes int,
	oldup float,
	newup float,
	usuario_email varchar(30));
	
drop table if exists album_historial;
create table album_historial(
	id serial primary key,
	oldtitle varchar(160),
	newtitle varchar(160),
	oldartistid int,
	newartistid int,
	usuario_email varchar(30));
	
drop table if exists artist_historial;
create table artist_historial(
	id serial primary key,
	oldname varchar(160),
	newname varchar(160),
	usuario_email varchar(30));