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
        titulo="Back to Black"
        aName="Amy Winehouse"
        cur.execute( "SELECT * FROM album WHERE album.title=%s AND album.artistid IN (SELECT artist.artistid FROM artist WHERE artist.name = %s)",(titulo, aName,))
        for a,b,c in cur.fetchall() :
            print(a,b,c)

        print("--------------------------------------------------")
        cur.execute( "SELECT * FROM artist WHERE artist.name = %s",(aName,))
        for a,b in cur.fetchall() :
            print(a,b)

        print("--------------------------------------------------")
        """print("Artista")
        cur.execute("SELECT * FROM artist LIMIT 10")
        # Recorremos los resultados y los mostramos
        for a,b in cur.fetchall() :
            print(a,b)
        print("--------------------------------------------------")

        print("Album")
        cur.execute("SELECT * FROM album LIMIT 15")
        # Recorremos los resultados y los mostramos
        for a,b,c in cur.fetchall() :
            print(a,b,c)
        print("--------------------------------------------------")

        print("Track")
        cur.execute("SELECT * FROM track WHERE track.albumid > 9 AND track.albumid < 14")
        # Recorremos los resultados y los mostramos
        for a,b,c,d,e,f,g,h,i in cur.fetchall() :
            print(a,b,c,d,e,f,g,h,i)
        print("--------------------------------------------------")

        print("!!!!!  SE ELIMINA   !!!!!")

        #Eliminar artista
        nombreArtist = "Audioslave"
        #Si quiere borrar un artista antes se borran todas las canciones y albums relacionados al artista
        cur.execute("SELECT artist.artistid FROM artist WHERE artist.name = '{0}'".format(nombreArtist))
        IDArtist=cur.fetchall()
        print(IDArtist)
        IDoficial=(IDArtist[0][0])
        print(IDoficial)
        cur.execute("DELETE FROM playlisttrack WHERE playlisttrack.trackid IN (SELECT track.trackid FROM track WHERE track.albumid IN (SELECT album.albumid FROM album WHERE album.artistid = %s))",(IDoficial,))
        cur.execute("DELETE FROM invoiceline WHERE invoiceline.trackid IN (SELECT track.trackid FROM track WHERE track.albumid IN (SELECT album.albumid FROM album WHERE album.artistid = %s))",(IDoficial,))
        cur.execute("DELETE FROM actividad_track WHERE actividad_track.trackid = %s",(IDoficial,))
        cur.execute("DELETE FROM track WHERE track.albumid IN (SELECT album.albumid FROM album WHERE album.artistid = %s)",(IDoficial,))
        cur.execute("DELETE FROM album WHERE album.artistid = '{0}'".format(IDoficial))
        cur.execute("DELETE FROM artist WHERE artist.artistid = '{0}'".format(IDoficial))

        print("Album")
        cur.execute("SELECT * FROM album LIMIT 15")
        # Recorremos los resultados y los mostramos
        for a,b,c in cur.fetchall() :
            print(a,b,c)
        print("--------------------------------------------------")

        print("Track")
        cur.execute("SELECT * FROM track WHERE track.albumid > 9 AND track.albumid < 14")
        # Recorremos los resultados y los mostramos
        for a,b,c,d,e,f,g,h,i in cur.fetchall() :
            print(a,b,c,d,e,f,g,h,i)
        print("--------------------------------------------------")

        print("Artista")
        cur.execute("SELECT * FROM artist LIMIT 10")
        # Recorremos los resultados y los mostramos
        for a,b in cur.fetchall() :
            print(a,b)
        print("--------------------------------------------------")"""


        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conexion is not None:
            conexion.close()
            print('Conexión finalizada.')


if __name__ == '__main__':
    conectar()
