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
        nameArtista="Maluma"
        cur.execute( "SELECT MAX(artist.artistid) FROM artist" )
        IDArtist=cur.fetchall()
        IDoficial=(IDArtist[0][0])
        IDoficial += 1
        cur.execute("INSERT INTO artist (artistid, name)VALUES (%s, %s)", ( IDoficial, nameArtista))
        #conexion.commit()
        cur.execute("SELECT * FROM artist")

        # Recorremos los resultados y los mostramos
        for a,b in cur.fetchall() :
            print(a,b)

        print("--------------------------------------------------")

        #insertamos album
        #necesitamos title, artistid, albumid
        nombreArtistAlbum="Maluma"
        nombreAlbum="11 pm"
        cur.execute( "SELECT MAX(album.albumid) FROM album" )
        idAlbum=cur.fetchall()
        idAlbum=idAlbum[0][0]
        idAlbum+=1
        cur.execute( "SELECT artist.artistid FROM artist WHERE artist.name=%s",(nombreArtistAlbum,) )
        IDArtistAlbum=cur.fetchall()
        IDArtistAlbum=IDArtistAlbum[0][0]
        postgres_insert_query="""INSERT INTO album (albumid, title, artistid) VALUES (%s,%s,%s)"""
        record_to_insert=(idAlbum, nombreAlbum,IDArtistAlbum)
        ##cur.execute(postgres_insert_query, record_to_insert)
        cur.execute("INSERT INTO album (albumid, title, artistid) VALUES (%s,%s,%s)", (idAlbum, nombreAlbum,IDArtistAlbum))
        #conexion.commit()
        cur.execute("SELECT * FROM album")
        # Recorremos los resultados y los mostramos
        for a,b,c in cur.fetchall() :
            print(a,b,c)

        print("--------------------------------------------------")


        # Ejecutamos una insercion registrar cancion
        #necesitamos trackID, name, AlbumId, MediaTypeId, GenreId, Composer, Milliseconds, Bytes, UnitPrice  y artist id
        #Name y ID de track
        ##insercion cancion
        nameTrack="hp"
        cur.execute( "SELECT MAX(track.trackid) FROM track" )
        IDTrack=cur.fetchall()
        IDoficial=(IDTrack[0][0])
        IDoficial += 1
        #Album
        nombreAlbum = "11 pm"
        cur.execute( "SELECT album.albumid FROM album WHERE album.title=%s",(nombreAlbum,))
        IDAlbum=cur.fetchall()
        IDAlbumOficial=(IDAlbum[0][0])
        #MediaType
        nombreMediaType = "AAC audio file"
        cur.execute( "SELECT mediatype.mediatypeid FROM mediatype WHERE mediatype.name=%s",(nombreMediaType,))
        IDMediaType=cur.fetchall()
        IDMediaTypeOficial=(IDMediaType[0][0])
        #Genre
        nombreGenre = "Pop"
        cur.execute( "SELECT genre.genreid FROM genre WHERE genre.name=%s",(nombreGenre,))
        IDGenre=cur.fetchall()
        IDGenreOficial=(IDGenre[0][0])
        #Otras variables necesaris
        Composer = "Maluma"
        Milliseconds = "189600"
        Bytes = "5"
        Unitprice = "0.99"
        cur.execute("INSERT INTO track (trackid, name, albumid, mediatypeid, genreid, composer, milliseconds, bytes, unitprice) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", ( IDoficial, nameTrack, IDAlbumOficial, IDMediaTypeOficial, IDGenreOficial, Composer, Milliseconds, Bytes, Unitprice,))
        ##conexion.commit()
        cur.execute("SELECT * FROM track")

        # Recorremos los resultados y los mostramos
        for a,b,c,d,e,f,g,h,i in cur.fetchall() :
            print(a,b,c,d,e,f,g,h,i)

        print("--------------------------------------------------")

        ##se borra cancion
        nombreTrack = "hp"
        cur.execute("DELETE FROM track WHERE track.name = %s",(nombreTrack,))
        # Recorremos los resultados y los mostramos
        for a,b,c,d,e,f,g,h,i in cur.fetchall() :
            print(a,b,c,d,e,f,g,h,i)

        print("--------------------------------------------------")

        ##se borra album
        nombreAlbum = "11 pm"
        cur.execute("DELETE FROM album WHERE album.title = %s",(nombreAlbum,))
        # Recorremos los resultados y los mostramos
        for a,b,c in cur.fetchall() :
            print(a,b,c)

        print("--------------------------------------------------")

        ##se borra artista
        nombreArtist = "Maluma"
        cur.execute("DELETE FROM artist WHERE artist.name=%s",(nombreArtist,))
        # Recorremos los resultados y los mostramos
        for a,b in cur.fetchall() :
            print(a,b)

        print("--------------------------------------------------")

        ##modificar informacion de artista
        nombreOriginalArt="Maluma"
        cur.execute( "SELECT artist.artistid FROM artist WHERE artist.name=%s",(nombreOriginalArt,))
        IDArtO=cur.fetchall()[0][0]
        print(IDArtO)
        nombreNuevoArtista="Juan Luis Londoño"
        cur.execute('''
                UPDATE artist
                SET name = %s
                WHERE artistid = %s
                ''',(nombreNuevoArtista, IDArtO))
        cur.execute("SELECT * FROM artist")
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
