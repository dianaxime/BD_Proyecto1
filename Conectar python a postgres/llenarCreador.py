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
        cur.execute("SELECT * FROM creador_track ORDER BY creador_track.trackid ASC LIMIT 5")
        # Recorremos los resultados y los mostramos
        for a,b,c in cur.fetchall() :
                print(a,b,c)

        print("--------------------------------------------------")
        print("Se borra...")
        nombre="Balls to the Wall"
        cur.execute("SELECT track.trackid FROM track WHERE track.name = '{0}'".format(nombre))
        IDTrack=cur.fetchall()
        IDoficial=(IDTrack[0][0])
        cur.execute("DELETE FROM creador_track WHERE creador_track.trackid = %s",(IDoficial,))
        cur.execute("SELECT * FROM creador_track ORDER BY creador_track.trackid ASC LIMIT 5")
        # Recorremos los resultados y los mostramos
        for a,b,c in cur.fetchall() :
                print(a,b,c)

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
