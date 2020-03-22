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

        cur.execute( "SELECT customer.firstname, COUNT(creador_track.creadorid) FROM creador_track JOIN customer ON customer.customerid=creador_track.creadorid GROUP BY customer.customerid ORDER BY COUNT(creador_track.creadorid) DESC LIMIT 10" )

        for a in cur.fetchall() :
            print(a)

        print("---------------------------------------------------")
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

        ##modificar informacion de album
        nombreOriginalAlb="11 pm"
        cur.execute( "SELECT album.albumid FROM album WHERE album.title=%s",(nombreOriginalAlb,))
        IDAlbO=cur.fetchall()[0][0]
        print(IDAlbO)
        cur.execute( "SELECT album.artistid FROM album WHERE album.title=%s",(nombreOriginalAlb,))
        IDArtistaO=cur.fetchall()[0][0]
        print(IDArtistaO)
        newArtist="Cumbia Band"
        cur.execute( "SELECT artist.artistid FROM artist WHERE artist.name=%s",(newArtist,))
        newArtistid=cur.fetchall()#[0][0]
        if (len(newArtistid)==0):
        	print("Ese artista no esta creado")
        	nameArtista=newArtist
	        cur.execute( "SELECT MAX(artist.artistid) FROM artist" )
	        IDArtist=cur.fetchall()
	        IDoficial=(IDArtist[0][0])
	        IDoficial += 1
	        print(IDoficial)
	        print(nameArtista)
	        cur.execute("INSERT INTO artist (artistid, name)VALUES (%s, %s)", ( IDoficial, nameArtista))
	        cur.execute("SELECT * FROM artist")
	        for a,b in cur.fetchall() :
	            print(a,b)

	        print("--------------------------------------------------")
	        ##conexion.commit()
	        cur.execute("SELECT * FROM artist")
	        newArtistid=IDoficial
	        ##print(IDAlbO)
	        nombreNewAlb="11 pm"
	        cur.execute('''
	                UPDATE album
	                SET title = %s,
	                	artistid=%s
	                WHERE albumid = %s
	                ''',(nombreNewAlb, newArtistid, IDAlbO))

	        # Recorremos los resultados y los mostramos

        else:
        	newArtistid=newArtistid	[0][0]
	        print(newArtistid)
	        nombreNewAlb="11 pm"
	        cur.execute('''
	                UPDATE album
	                SET title = %s,
	                	artistid=%s
	                WHERE albumid = %s
	                ''',(nombreNewAlb, newArtistid, IDAlbO))


        cur.execute("SELECT * FROM album")
        for a,b,c in cur.fetchall() :
            print(a,b,c)

        print("--------------------------------------------------")

##modificar informacion de cancion
        nombreOriginalTrack="Crazy"
        cur.execute( "SELECT track.trackid FROM track WHERE track.name=%s",(nombreOriginalTrack,))
        IDTrackO=cur.fetchall()[0][0]
        print(IDTrackO)
        cur.execute( "SELECT track.albumid FROM track WHERE track.name=%s",(nombreOriginalTrack,))
        IDAlbumO=cur.fetchall()[0][0]
        print(IDAlbumO)
        cur.execute( "SELECT album.title FROM album WHERE album.albumid=%s",(IDAlbumO,))
        nombreAlbumO=cur.fetchall()[0][0]
        print(nombreAlbumO)
        cur.execute( "SELECT track.mediatypeid FROM track WHERE track.name=%s",(nombreOriginalTrack,))
        IDMediaTO=cur.fetchall()[0][0]
        print(IDMediaTO)
        cur.execute( "SELECT mediatype.name FROM mediatype WHERE mediatype.mediatypeid=%s",(IDMediaTO,))
        nombreMediaTO=cur.fetchall()[0][0]
        print(nombreMediaTO)
        cur.execute( "SELECT track.genreid FROM track WHERE track.name=%s",(nombreOriginalTrack,))
        IDGenreO=cur.fetchall()[0][0]
        print(IDGenreO)
        cur.execute( "SELECT genre.name FROM genre WHERE genre.genreid=%s",(IDGenreO,))
        nombreGenreO=cur.fetchall()[0][0]
        print(nombreGenreO)
        cur.execute( "SELECT track.composer FROM track WHERE track.name=%s",(nombreOriginalTrack,))
        IDComposerO=cur.fetchall()[0][0]
        print(IDComposerO)
        cur.execute( "SELECT track.milliseconds FROM track WHERE track.name=%s",(nombreOriginalTrack,))
        IDMilliO=cur.fetchall()[0][0]
        print(IDMilliO)
        cur.execute( "SELECT track.bytes FROM track WHERE track.name=%s",(nombreOriginalTrack,))
        IDbytesO=cur.fetchall()[0][0]
        print(IDbytesO)
        cur.execute( "SELECT track.unitprice FROM track WHERE track.name=%s",(nombreOriginalTrack,))
        IDUnitPriceO=cur.fetchall()[0][0]
        print(IDUnitPriceO)
        print("--------------------------------------------------------------------------------------------------")
        newgenreTrack="Rock"
        newalbumTrack="Big Ones"
        newmediatype="MPEG audio file"

        cur.execute( "SELECT mediatype.mediatypeid FROM mediatype WHERE mediatype.name=%s",(newmediatype,))
        idnewMediaT=cur.fetchall()#[0][0]
        print(idnewMediaT)

        cur.execute( "SELECT genre.genreid FROM genre WHERE genre.name=%s",(newgenreTrack,))
        idnewgenre=cur.fetchall()#[0][0]
        print(idnewgenre)

        cur.execute( "SELECT album.albumid FROM album WHERE album.title=%s",(newalbumTrack,))
        idnewalbum=cur.fetchall()#[0][0]
        print(idnewalbum)

        if (len(idnewMediaT)==0 or len(idnewgenre)==0 or len(idnewalbum)==0 ):
        	print ("No se puede modificar esta cancion. Verifica que el genero, album y tipo de medio ya exista")
        	idnewMediaT=IDMediaTO
        	idnewgenre=IDGenreO
        	idnewalbum=IDAlbumO
        else:
        	idnewMediaT=idnewMediaT[0][0]
        	idnewgenre=idnewgenre[0][0]
        	idnewalbum=idnewalbum[0][0]

        newname="Crazy"
        newComposer="Steven Tyler, Joe Perry, Desmond Child"
        newMilli=316656
        newByte=10402398
        newByte=0.99

        cur.execute('''
                UPDATE track
                SET name = %s,
                albumid=%s,
                mediatypeid=%s,
                genreid=%s,
                composer=%s,
                milliseconds=%s,
                bytes=%s,
                unitprice=%s
                WHERE trackid = %s
                ''',(newname, idnewalbum, idnewMediaT,idnewgenre, newComposer,newMilli,newByte, newByte,IDTrackO))
        cur.execute("SELECT * FROM track")
        for a,b,c,d,e,f,g,h,i in cur.fetchall() :
            print(a,b,c,d,e,f,g,h,i)

        print("--------------------------------------------------")

        #Eliminar track
        nombreTrack = "Snowballed"
        #Si quiere borrar un track antes se borra de las playlisttrack y de la invoiceline en donde este agregada
        #try:
        cur.execute("SELECT track.trackid FROM track WHERE track.name = '{0}'".format(nombreTrack))
        IDTrack=cur.fetchall()
        print(IDTrack)
        IDoficial=(IDTrack[0][0])
        print(IDoficial)
        cur.execute("DELETE FROM playlisttrack WHERE playlisttrack.trackid = %s",(IDoficial,))
        cur.execute("DELETE FROM actividad_track WHERE actividad_track.trackid = %s",(IDoficial,))
        cur.execute("DELETE FROM invoiceline WHERE invoiceline.trackid = %s",(IDoficial,))
        cur.execute("DELETE FROM track WHERE track.trackid = %s",(IDoficial,))
        cur.execute("SELECT * FROM track")

        #Eliminar album
        nombreAlbum = "Facelift"
        #Si quiere borrar un album antes se borran todas las canciones que estan relacionadas con el album
        #try:
        cur.execute("SELECT album.albumid FROM album WHERE album.title = '{0}'".format(nombreAlbum))
        IDAlbum=cur.fetchall()
        print(IDAlbum)
        IDoficial=(IDAlbum[0][0])
        print(IDoficial)
        cur.execute("DELETE FROM playlisttrack WHERE playlisttrack.trackid IN (SELECT track.trackid FROM track WHERE track.albumid = %s)",(IDoficial,))
        cur.execute("DELETE FROM invoiceline WHERE invoiceline.trackid IN (SELECT track.trackid FROM track WHERE track.albumid = %s)",(IDoficial,))
        cur.execute("DELETE FROM actividad_track WHERE actividad_track.trackid IN (SELECT track.trackid FROM track WHERE track.albumid = %s)",(IDoficial,))
        cur.execute("DELETE FROM track WHERE track.albumid = %s",(IDoficial,))
        cur.execute("DELETE FROM album WHERE album.title = '{0}'".format(nombreAlbum))

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
        cur.execute("DELETE FROM actividad_track WHERE actividad_track.trackid IN (SELECT track.trackid FROM track WHERE track.albumid IN (SELECT album.albumid FROM album WHERE album.artistid = %s))",(IDoficial,))
        cur.execute("DELETE FROM track WHERE track.albumid IN (SELECT album.albumid FROM album WHERE album.artistid = %s)",(IDoficial,))
        cur.execute("DELETE FROM album WHERE album.artistid = '{0}'".format(IDoficial))
        cur.execute("DELETE FROM artist WHERE artist.artistid = '{0}'".format(IDoficial))




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
