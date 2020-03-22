import psycopg2
from config import config


def conectar():
    """ Conexión al servidor de pases de datos PostgreSQL """
    conexion = None
    try:
        # Lectura de los parámetros de conexion
        params = config()

        #print(params)
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

        cur.execute("SELECT * FROM track")
        canciones=cur.fetchall()
        n=1
        for i in canciones:
        	print (i[0])
        	cur.execute("INSERT INTO creador_track (relacionid, creadorid, trackid) VALUES (%s, %s, %s)", (n, n%50+1, i[0],))
        	n+=1
        	#print("este es id de actividad_track %s",(n))
        	#cur.execute("INSERT INTO actividad_track (trackid, name, albumid, mediatypeid, genreid, composer, milliseconds, bytes, unitprice) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", ( IDoficial, nameTrack, IDAlbumOficial, IDMediaTypeOficial, IDGenreOficial, Composer, Milliseconds, Bytes, Unitprice,))

        conexion.commit()



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
