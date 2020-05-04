DROP TABLE IF EXISTS permisos_usuario;
CREATE TABLE permisos_usuario (
        		permisoid INT PRIMARY KEY,
        		contraseÃ±a VARCHAR(30) NOT NULL,
        		customerid INT NOT NULL,
        		puede_registrar bool not null,
        		puede_inactivar bool not null,
        		puede_eliminar bool not null,
        		puede_modificar bool not null,
        		
        		FOREIGN KEY (customerid) REFERENCES customer(customerid)
        	);
        
DROP TABLE IF EXISTS permisos_admin;
CREATE TABLE permisos_admin (
        		permisoid INT PRIMARY KEY,
        		contraseña VARCHAR(30) NOT NULL,
        		employeeid INT NOT NULL,
        		FOREIGN KEY (employeeid) REFERENCES employee(employeeid)
        	);
        
DROP TABLE IF EXISTS actividad_track;
CREATE TABLE actividad_track (
        		actividadid INT PRIMARY KEY,
        		esta_activo bool not null,
        		trackid INT NOT NULL,
        		FOREIGN KEY (trackid) REFERENCES track(trackid)
        	);

DROP TABLE IF EXISTS creador_track;
CREATE TABLE creador_track (
				relacionid INT PRIMARY KEY,
        		creadorid INT ,
        		trackid INT NOT NULL,
        		FOREIGN KEY (trackid) REFERENCES track(trackid),
        		FOREIGN KEY (creadorid) REFERENCES customer(customerid)
        	);