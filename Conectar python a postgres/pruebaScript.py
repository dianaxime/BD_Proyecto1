import pymongo
import psycopg2
from config import config
import datetime

#conectar a mongo
conexion=pymongo.MongoClient() 
db=conexion.proyectoBD
coleccion=db.recomendaciones


def conectar():
    """ Conexión al servidor de pases de datos PostgreSQL """
    conexion = None
    try:
        # Lectura de los parámetros de conexion
        params = config()

        # Conexion al servidor de PostgreSQL
        print('Conectando a la base de datos PostgreSQL...')
        conexion = psycopg2.connect(**params)
        # creación del cursor
        cur = conexion.cursor()
        # Ejecución la consulta para obtener la conexión
        print('La version de PostgreSQL es la:')
        cur.execute('SELECT version()')

        # Se obtienen los resultados
        db_version = cur.fetchone()
        # Se muestra la versión por pantalla
        print(db_version)
        #cur.execute(
        '''SELECT customer.email, genre.name
        	FROM creador_track
        	JOIN customer ON customer.customerid = creador_track.creadorid
        	JOIN track ON creador_track.trackid = track.trackid 
        	JOIN genre ON track.genreid = genre.genreid
        	WHERE customer.customerid IN (
        	SELECT creador_track.creadorid 
        	FROM creador_track
        	GROUP BY creador_track.creadorid
        	ORDER BY COUNT(creador_track.creadorid) DESC LIMIT 10)
        	GROUP BY customer.email, genre.genreid
        	ORDER BY customer.email DESC
        	'''
        #)
        fecha = '2009-01-06'
        ahora = datetime.datetime.utcnow()
        tiempo = ahora - datetime.timedelta(days=30)
        cur.execute('''
        	SELECT customer.email, track."name", 
			genre."name" as genre, invoice.invoicedate
			FROM invoice
			JOIN invoiceline ON invoiceline.invoiceid = invoice.invoiceid
			join track on invoiceline.trackid = track.trackid
			join genre on track.genreid = genre.genreid
			join customer on customer.customerid = invoice.customerid
			where invoice.invoicedate = %s
		''',(fecha,))
        # Recorremos los resultados y los mostramos
        compras = cur.fetchall()
        for email, cancion, genero, fechac in compras:
            #print(email, cancion, genero, fechac)
            cur.execute('''
            	SELECT DISTINCT(track."name"), genre."name"
            	FROM bitacora
            	JOIN track ON bitacora.nombre_object = track."name"
            	JOIN genre ON track.genreid = genre.genreid
            	WHERE bitacora.nombre_object <> %s
            	AND bitacora.email <> %s 
            	AND bitacora.date_on > %s
            	AND bitacora.date_on < %s
            	AND bitacora.accion = %s
            ''',(cancion, email, tiempo, ahora, 'add'))
            resul = cur.fetchall()
            for a, b in resul:
            	#print(a, b)
            	if (coleccion.find({'_id': email}).count() > 0):
            		if (coleccion.find({ '_id': email, 'sells.track': cancion}).count() <= 0):
            			result = coleccion.update({'_id': email }, { '$set': { 'modified': ahora },'$push': { 'sells': {'email': email, 'track': cancion, 'genre': genero, 'date': fechac}}}, w=1)
            		if (coleccion.find({ '_id': email, 'tracks.track': a}).count() <= 0):
            			result = coleccion.update({'_id': email }, { '$set': { 'modified': ahora },'$push': { 'tracks': {'track': a, 'genre': b, 'date': ahora} }}, w=1)
            	else:
	            	result = coleccion.insert({'_id': email }, { '$set': { 'modified': ahora },'$push': { 'sells': {'email': email, 'track': cancion, 'genre': genero, 'date': fechac}, 'tracks': {'track': a, 'genre': b, 'date': ahora} } }, w=1)
        
        print("--------------------------------------------------")

        # Cerremos el cursor
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conexion is not None:
            conexion.close()
            print('Conexión finalizada.')


if __name__ == '__main__':
    conectar()