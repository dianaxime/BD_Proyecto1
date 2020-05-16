import psycopg2
from config import config
import datetime
from random import randint

import radar 


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
        #print(db_version)
        #cur.execute("SELECT * FROM creador_track ORDER BY creador_track.trackid ASC LIMIT 5")
        # Recorremos los resultados y los mostramos
        #for a,b,c in cur.fetchall() :
        #        print(a,b,c)

        #print("--------------------------------------------------")
        #print("Se borra...")
        #nombre="Balls to the Wall"
        #cur.execute("SELECT track.trackid FROM track WHERE track.name = '{0}'".format(nombre))
        #IDTrack=cur.fetchall()
        #IDoficial=(IDTrack[0][0])
        #cur.execute("DELETE FROM creador_track WHERE creador_track.trackid = %s",(IDoficial,))
        cur.execute("SELECT COUNT(*) FROM track")
        # Recorremos los resultados y los mostramos
        b = cur.fetchall()
        b = int(b[0][0])
        for a in range(b):
            a=a+1
            customerID = randint(1,57)
            cur.execute( "SELECT customer.email FROM customer WHERE customer.customerid=%s",(customerID,) )
            email = cur.fetchall()
            email = email[0][0]
            fecha = datetime.date(randint(2005,2020), randint(1,12),randint(1,28))
            cur.execute( "SELECT track.name FROM track WHERE track.trackid=%s",(a,) )
            cancion = cur.fetchall()
            cancion = cancion[0][0]
            cur.execute("INSERT INTO Bitacora (nombre_object, email, accion, tipo, date_on) VALUES (%s, %s, %s, %s, %s)", ( cancion, email, 'add', 'track', fecha))
            up = randint(1,57)
            ins = randint(1,57)
            dele = randint(1,57)
            cur.execute('''
                        UPDATE track
                        SET name = %s,
                            u_added=%s,
                            u_updated=%s,
                            u_deleted=%s
                        WHERE trackid = %s
                        ''',(cancion, ins, up, dele, a))

                #print(a)

        print("--------------------------------------------------")


        cur.execute("SELECT COUNT(*) FROM album")
        # Recorremos los resultados y los mostramos
        b = cur.fetchall()
        b = int(b[0][0])
        for a in range(b):
            a=a+1
            customerID = randint(1,57)
            cur.execute( "SELECT customer.email FROM customer WHERE customer.customerid=%s",(customerID,) )
            email = cur.fetchall()
            email = email[0][0]
            fecha = datetime.date(randint(2005,2020), randint(1,12),randint(1,28))
            cur.execute( "SELECT album.title FROM album WHERE album.albumid=%s",(a,) )
            cancion = cur.fetchall()
            cancion = cancion[0][0]
            cur.execute("INSERT INTO Bitacora (nombre_object, email, accion, tipo, date_on) VALUES (%s, %s, %s, %s, %s)", ( cancion, email, 'add', 'track', fecha))
            up = randint(1,57)
            ins = randint(1,57)
            dele = randint(1,57)
            cur.execute('''
                        UPDATE album
                        SET title = %s,
                            u_added=%s,
                            u_updated=%s,
                            u_deleted=%s
                        WHERE albumid = %s
                        ''',(cancion, ins, up, dele, a))

                #print(a)
        print("--------------------------------------------------")


        cur.execute("SELECT COUNT(*) FROM artist")
        # Recorremos los resultados y los mostramos
        b = cur.fetchall()
        b = int(b[0][0])
        for a in range(b):
            a=a+1
            customerID = randint(1,57)
            cur.execute( "SELECT customer.email FROM customer WHERE customer.customerid=%s",(customerID,) )
            email = cur.fetchall()
            email = email[0][0]
            fecha = datetime.date(randint(2005,2020), randint(1,12),randint(1,28))
            cur.execute( "SELECT artist.name FROM artist WHERE artist.artistid=%s",(a,) )
            cancion = cur.fetchall()
            cancion = cancion[0][0]
            cur.execute("INSERT INTO Bitacora (nombre_object, email, accion, tipo, date_on) VALUES (%s, %s, %s, %s, %s)", ( cancion, email, 'add', 'artist', fecha))
            up = randint(1,57)
            ins = randint(1,57)
            dele = randint(1,57)
            cur.execute('''
                        UPDATE artist
                        SET name = %s,
                            u_added=%s,
                            u_updated=%s,
                            u_deleted=%s
                        WHERE artistid = %s
                        ''',(cancion, ins, up, dele, a))
                #print(a)

        print("--------------------------------------------------")

        cur.execute("SELECT COUNT(*) FROM playlist")
        # Recorremos los resultados y los mostramos
        b = cur.fetchall()
        b = int(b[0][0])
        for a in range(b):
            a=a+1
            customerID = randint(1,57)
            cur.execute( "SELECT customer.email FROM customer WHERE customer.customerid=%s",(customerID,) )
            email = cur.fetchall()
            email = email[0][0]
            fecha = datetime.date(randint(2005,2020), randint(1,12),randint(1,28))
            cur.execute( "SELECT playlist.name FROM playlist WHERE playlist.playlistid=%s",(a,) )
            cancion = cur.fetchall()
            cancion = cancion[0][0]
            cur.execute("INSERT INTO Bitacora (nombre_object, email, accion, tipo, date_on) VALUES (%s, %s, %s, %s, %s)", ( cancion, email, 'add', 'playlist', fecha))
            up = randint(1,57)
            ins = randint(1,57)
            dele = randint(1,57)
            cur.execute('''
                        UPDATE playlist
                        SET name = %s,
                            u_added=%s,
                            u_updated=%s,
                            u_deleted=%s
                        WHERE playlistid = %s
                        ''',(cancion, ins, up, dele, a))
                #print(a)

        print("--------------------------------------------------")

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
