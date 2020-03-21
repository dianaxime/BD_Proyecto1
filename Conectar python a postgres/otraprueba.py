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
        """cur.execute( "SELECT genre.name, COUNT(*) FROM track JOIN genre ON genre.genreid=track.genreid GROUP BY genre.genreid ORDER BY COUNT(*) DESC LIMIT 10" )


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

        print("--------------------------------------------------")"""
        ##crear usuario
        firstName="Juan Diego"
        lastName="Vásquez"
        email="juan.diego.vf@gmail.com"
        contrasena="soyJuanDiego123"
        cur.execute( "SELECT MAX(customer.customerid) FROM customer" )
        IDUsuario=cur.fetchall()
        IDoficial=(IDUsuario[0][0])
        IDoficial += 1
        print(IDoficial)
        cur.execute("INSERT INTO customer (customerid, firstname, lastname, email)VALUES (%s, %s,%s, %s)", (IDoficial, firstName, lastName, email,))
        cur.execute("SELECT customerid,firstname, lastname,email FROM customer")
        #conexion.commit()

        # Recorremos los resultados y los mostramos
        for a,b,c,d in cur.fetchall() :
            print(a,b,c,d)

        print("--------------------------------------------------")
        cur.execute("INSERT INTO permisos_usuario (permisoid, contraseña, customerid, puede_registrar, puede_inactivar, puede_eliminar,puede_modificar)VALUES (%s, %s,%s, %s,%s,%s, %s)", (IDoficial, contrasena, IDoficial,False, False,False,False,))
        cur.execute("SELECT * FROM permisos_usuario")

        #conexion.commit()

        # Recorremos los resultados y los mostramos
        for a,b,c,d,e,f,g in cur.fetchall() :
            print(a,b,c,d,e,f,g)

        print("--------------------------------------------------")

        ##crear admin
        """firstName="Juan Carlos"
        lastName="Vásquez"
        email="juancvs@gmail.com"
        contrasena="soyJuanCarlos123"
        cur.execute( "SELECT MAX(employee.employeeid) FROM employee" )
        IDUsuario=cur.fetchall()
        IDoficial=(IDUsuario[0][0])
        IDoficial += 1
        print(IDoficial)
        cur.execute("INSERT INTO employee (employeeid, firstname, lastname, email)VALUES (%s, %s,%s, %s)", (IDoficial, firstName, lastName, email,))
        cur.execute("SELECT employeeid,firstname, lastname,email FROM employee")

        # Recorremos los resultados y los mostramos
        for a,b,c,d in cur.fetchall() :
            print(a,b,c,d)

        print("--------------------------------------------------")
        cur.execute("INSERT INTO permisos_admin (permisoid, contraseña, employeeid)VALUES (%s, %s,%s)", (IDoficial, contrasena, IDoficial,))
        cur.execute("SELECT * FROM permisos_admin")

        # Recorremos los resultados y los mostramos
        for a,b,c in cur.fetchall() :
            print(a,b,c)

        print("--------------------------------------------------")"""

        ##verificar contrasena de admin
        correoIngresado="juancvs@gmail.com"
        contrasenaIngresada="soyJuanCarlos123"
        cur.execute("SELECT contraseña FROM permisos_admin JOIN employee ON employee.employeeid=permisos_admin.employeeid  WHERE employee.email=%s",(correoIngresado,))
        contrasenaUsuario=cur.fetchall()
        if (len(contrasenaUsuario)==0):
            print("Ese correo no esta registrado de admin")
        else:
            contrasenaUsuario=contrasenaUsuario[0][0]
            if (contrasenaIngresada==contrasenaUsuario):
                print ("Acceso concebido de admin")
            else:
                print("contraseña incorrecta de admin")


        ##verificar contrasena de usuario
        correoIngresado="juan.diego.vf@gmail.com"
        contrasenaIngresada="soyJuanDiego123"
        cur.execute("SELECT contraseña FROM permisos_usuario JOIN customer ON customer.customerid=permisos_usuario.customerid  WHERE customer.email=%s",(correoIngresado,))
        contrasenaUsuario=cur.fetchall()
        if (len(contrasenaUsuario)==0):
            print("Ese correo no esta registrado")
        else:
            contrasenaUsuario=contrasenaUsuario[0][0]
            if (contrasenaIngresada==contrasenaUsuario):
                print ("Acceso concebido")
            else:
                print("contraseña incorrecta")

        """cur.execute("DELETE FROM permisos_usuario WHERE permisos_usuario.contraseña = 'soyJuanDiego123'")
        conexion.commit()
        cur.execute("DELETE FROM customer WHERE customer.firstname = 'Juan Diego'",(IDoficial,))
        conexion.commit()"""

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
