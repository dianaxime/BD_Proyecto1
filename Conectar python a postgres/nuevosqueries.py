import psycopg2
from config import config

def conectar():
    """ Conexión al servidor de pases de datos PostgreSQL """
    conexion = None
    try:
        # Lectura de los parámetros de conexion
        params = config()
        # Conexion al servidor de PostgreSQL
        conexion = psycopg2.connect(**params)
        # creación del cursor
        cur = conexion.cursor()
        # Ejecución la consulta para obtener la conexión
        cur.execute('SELECT version()')
        # Se obtienen los resultados
        db_version = cur.fetchone()
        # Ejecutamos una consulta
        cur.execute( "SELECT DISTINCT playlist.name, SUM(track.milliseconds) FROM playlisttrack JOIN track ON track.trackid=playlisttrack.trackid JOIN playlist ON playlist.playlistid=playlisttrack.playlistid GROUP BY playlist.playlistid ORDER BY SUM(track.milliseconds) DESC" )
        #Insertamos los datos devueltos por la consulta en la tabla
        for a,b in cur.fetchall():
            print(a,b)
            # Cerremos el cursor
        print("----------------------------------------------")

        cur.execute('''SELECT playlist.name, COUNT(DISTINCT artist.name)
        FROM playlist 
        JOIN playlisttrack ON playlist.playlistid = playlisttrack.playlistid
        JOIN track ON playlisttrack.trackid = track.trackid 
        JOIN album ON track.albumid = album.albumid 
        JOIN artist ON album .artistid  = artist.artistid
        GROUP BY playlist.name
        ORDER BY COUNT(DISTINCT artist.name) DESC ''')

        # Recorremos los resultados y los mostramos
        for a,b in cur.fetchall() :
            print(a,b)

        print("--------------------------------------------------")

        cur.execute('''SELECT artist.name, COUNT(DISTINCT track.genreid)
        FROM artist 
        JOIN album ON album.artistid = artist.artistid
        JOIN track ON track.albumid = album.albumid 
        GROUP BY artist.name 
        ORDER BY COUNT(DISTINCT track.genreid) DESC 
        LIMIT 5''')

        #Recorremos los resultados y los mostramos
        for a,b in cur.fetchall() :
            print(a,b)

        print("--------------------------------------------------")

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conexion is not None:
            conexion.close()

if __name__ == '__main__':
    conectar()
