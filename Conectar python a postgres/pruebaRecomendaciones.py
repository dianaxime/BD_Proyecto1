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
        cur.execute(
        '''SELECT customer.email, genre.name, COUNT(genre.genreid)
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
        )
        resul = cur.fetchall()
        for email, genre, cuenta in resul:
            if cuenta > 5:
                a = coleccion.aggregate([{ '$match': { '_id': email } },{ '$unwind': '$tracks' },{ '$match': { 'tracks.genre': genre }},{ '$project': { 'track': '$tracks.track', 'genre': '$tracks.genre' }}])
                for i in a:
                    print(i['_id'],' ',i['track'],' ',i['genre'])
        

        

        
        # Recorremos los resultados y los mostramos
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