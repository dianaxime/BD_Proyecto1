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

        #Buscar track
        nameTrack = "Fast As a Shark"
        cur.execute("""
            SELECT track.name, album.title, artist.name, track.unitprice
            FROM track  
                JOIN album ON album.albumid = track.albumid
                JOIN artist ON artist.artistid = album.artistid
            WHERE track.name = %s
            """,(nameTrack,))
        for a,b,c,d in cur.fetchall() :
            print(a,"-",b,"-",c,"-",d)
        print("--------------------------------------------------")

        #Buscar album
        nameAlbum = "AM"
        cur.execute("""
            SELECT artist.name, album.title, track.name
            FROM album 
                JOIN artist ON artist.artistid = album.artistid
                JOIN track ON track.albumid = album.albumid
            WHERE album.title = %s
            """,(nameAlbum,))
        for a,b,c in cur.fetchall() :
            print(a,"-",b,"-",c)
        print("--------------------------------------------------")

        #Buscar artista
        nameAlbum = "Accept"
        cur.execute("""
            SELECT album.title, artist.name
            FROM album 
                JOIN artist ON artist.artistid = album.artistid
            WHERE artist.name = %s
            """,(nameAlbum,))
        for a,b in cur.fetchall() :
            print(a,"-",b)
        print("--------------------------------------------------")
        #cur.execute("""SELECT add_bitacora(61::numeric, 'SI FUNCIONA'::varchar, 1::numeric, 2::numeric ) FROM track WHERE track.name='Evil Dick'""")
        #conexion.commit()
        #cur.execute("SELECT track.name FROM track WHERE track.albumid = '{0}'".format(36))
        #for a in cur.fetchall() :
           # print (a[0])
           # cur.execute("""SELECT add_bitacora(61::numeric, 'for prueba'::varchar, 1::numeric, 2::numeric ) FROM track WHERE track.name='Evil Dick'""")
        #conexion.commit()
        cur.execute("SELECT track.name FROM track WHERE track.albumid = '{0}'".format(36))
        tracks=cur.fetchall()
        for a in tracks :
            print (a[0])
            cur.execute("""SELECT add_bitacora(%s::numeric, %s::varchar, 3::numeric, 1::numeric ) """, (61, str(a[0]))) 
        """nombre="Balls to the Wall"
        cur.execute("SELECT actividad_track.trackid FROM actividad_track WHERE actividad_track.trackid IN (SELECT track.trackid FROM track WHERE track.name = %s)",(nombre,))
        IDTrack=cur.fetchall()
        print(IDTrack)
        if(len(IDTrack)!=0):
            #Si si existe se obtine el ID y adquiere su estado
            IDoficial=(IDTrack[0][0])
            print(IDoficial)
            cur.execute("SELECT actividad_track.esta_activo FROM actividad_track WHERE actividad_track.trackid = %s",(IDoficial,))
            estado=cur.fetchall()
            actualState=(estado[0][0])
            print(actualState)
            if(actualState==True):
                #Si esta activada se desactiva el track
                newState = False
                print(newState)
                cur.execute("UPDATE actividad_track SET esta_activo = False WHERE actividadid = %s",(IDoficial,))
                cur.execute("SELECT * FROM actividad_track ORDER BY actividad_track.trackid ASC LIMIT 10")
                for a,b,c in cur.fetchall() :
                    print(a,b,c)
                print("--------------------------------------------------")
            else:
                #Si esta desactivda se activa el track
                newState = True
                print(newState)
                cur.execute("UPDATE actividad_track SET esta_activo = True WHERE actividadid = %s",(IDoficial,))
                cur.execute("SELECT * FROM actividad_track ORDER BY actividad_track.trackid ASC LIMIT 10")
                for a,b,c in cur.fetchall() :
                    print(a,b,c)
                print("--------------------------------------------------")
        else:
            #Sino existe se muestra error
            print("No existe")
        print("Artista")
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
