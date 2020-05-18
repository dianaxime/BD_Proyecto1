import psycopg2
from config import config
from random import randint



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
        
        cur.execute("SELECT COUNT(*) FROM track")
        # Recorremos los resultados y los mostramos
        link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&feature=youtu.be'
        b = cur.fetchall()
        b = int(b[0][0])
        for a in range(b):
            a=a+1
            customerID = randint(1,57)
            cur.execute('''
                        UPDATE track
                        SET link_video=%s,
                        u_updated=%s
                        WHERE trackid = %s
                        ''',(link, customerID, a))

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
