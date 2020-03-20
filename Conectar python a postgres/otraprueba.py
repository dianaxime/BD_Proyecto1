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
        # Ejecutamos una consulta
        cur.execute( "SELECT genre.name, COUNT(*) FROM track JOIN genre ON genre.genreid=track.genreid GROUP BY genre.genreid ORDER BY COUNT(*) DESC LIMIT 10" )


        # Recorremos los resultados y los mostramos
        for a,b in cur.fetchall() :
            print(a,b)

        print("--------------------------------------------------")


        # Ejecutamos una consulta
        cur.execute( "SELECT artist.name, COUNT(*) FROM album JOIN artist ON artist.artistid=album.artistid GROUP BY artist.artistid ORDER BY COUNT(*) DESC LIMIT 10" )

        for a,b in cur.fetchall() :
            print(a,b)

        print("--------------------------------------------------")

       # Ejecutamos una consulta
        cur.execute( "SELECT artist.name, track.name, track.milliseconds FROM album JOIN track ON track.albumid=album.albumid JOIN artist ON album.artistid=artist.artistid ORDER BY track.milliseconds DESC LIMIT 10 ")

        # Recorremos los resultados y los mostramos
        for a,b,c in cur.fetchall() :
            print(a,b,c)

        print("--------------------------------------------------")


        # Ejecutamos una consulta
        cur.execute( "SELECT genre.name, AVG(track.milliseconds) FROM track JOIN genre ON genre.genreid=track.genreid GROUP BY genre.genreid ORDER BY AVG(track.milliseconds) DESC" )


        # Recorremos los resultados y los mostramos
        for a,b in cur.fetchall() :
            print(a,b)

        print("--------------------------------------------------")

        #insercion de datos
        # Ejecutamos una insercion registrar artista
        #necesitamos name y artist id

        """INSERT INTO cliente VALUES
            (4614488, 'Juan Carlos', 'Vasquez'),
            (8962157 ,'Ivan', 'Porras'),
            (4526358, 'Camila', 'Gonzales'),
            (1252689, 'Juan Diego', 'Salazar'),
            (7826951, 'Sara', 'Figueroa');"""
        nameArtista="Maluma"
        cur.execute( "SELECT MAX(artist.artistid) FROM artist" )
        IDArtist=cur.fetchall()
        print(IDArtist)
        #IDArtist += 1
        cur.execute("INSERT INTO artist VALUES ( IDArtist, nameArtista)")
        cur.execute("SELECT * FROM artist")

        # Recorremos los resultados y los mostramos
        for a,b in cur.fetchall() :
            print(a,b)

        print("--------------------------------------------------")

        # Ejecutamos una insercion registrar cancion
        cur.execute( "SELECT genre.name, AVG(track.milliseconds) FROM track JOIN genre ON genre.genreid=track.genreid GROUP BY genre.genreid ORDER BY AVG(track.milliseconds) DESC" )


        # Recorremos los resultados y los mostramos
        for a,b in cur.fetchall() :
            print(a,b)

        print("--------------------------------------------------")

        # Ejecutamos una insercion
        cur.execute( "SELECT genre.name, AVG(track.milliseconds) FROM track JOIN genre ON genre.genreid=track.genreid GROUP BY genre.genreid ORDER BY AVG(track.milliseconds) DESC" )


        # Recorremos los resultados y los mostramos
        for a,b in cur.fetchall() :
            print(a,b)

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
