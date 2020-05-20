import psycopg2
from config import config
from random import randint
from datetime import date


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

        #id de invoice e invoiceline
        cur.execute( "SELECT MAX(invoice.invoiceid) FROM invoice" )
        IDinvoice=cur.fetchall()
        invoiceoficial=IDinvoice[0][0]
        invoiceoficial += 1
        cur.execute( "SELECT MAX(invoiceline.invoicelineid) FROM invoiceline" )
        IDinvoiceline=cur.fetchall()
        invoicelineoficial=IDinvoiceline[0][0]
        invoicelineoficial += 1

        #quiero reproducir n canciones
        n=3
        cur.execute( "SELECT MAX(track.trackid) FROM track" )
        b = cur.fetchall()
        b = int(b[0][0])
        print(b)

        for i in range(n):
            existente=False
            while (existente==False):
                cur.execute( "SELECT  trackid from track where trackid=%s",  (randint(1,b),) )
                idtrack=cur.fetchall()#[0][0]
                if (len(idtrack)!=0):
                    existente=True
            idtrack=idtrack[0][0]
            print(idtrack)
            cur.execute( """INSERT into reproduccion (trackid) VALUES (%s) """,(idtrack,))
            #conexion.commit()

        print("------------------------------")
        #quiero comprar x canciones
        x=2
        #fecha introducida por el usuario
        d = date(2020, 5, 16)
        
        #cantidad de customers
        cur.execute( "SELECT MAX(customer.customerid) FROM customer" )
        c = cur.fetchall()
        c = int(c[0][0])
        print(c)

        for i in range(x):
            existente=False
            while (existente==False):
                cur.execute( "SELECT  trackid, unitprice from track where trackid=%s",  (randint(1,b),) )
                idtrack=cur.fetchall()#[0][0]
                if (len(idtrack)!=0):
                    existente=True
            idOtrack=idtrack[0][0]
            uptrack=idtrack[0][1]
            print("cancion: "+str(idOtrack))
            print("precio: "+str(uptrack))
            
            existenteC=False
            while (existenteC==False):
                cur.execute( "SELECT  customerid from customer where customerid=%s",  (randint(1,c),) )
                idCus=cur.fetchall()#[0][0]
                if (len(idCus)!=0):
                    existenteC=True
            idcustomer=idCus[0][0]
            print ("comprador: "+str(idcustomer))
            cur.execute( "INSERT INTO invoice (invoiceid, invoicedate, customerid, total) values (%s, %s, %s, %s)", (invoiceoficial, d, idcustomer, uptrack))
            cur.execute( """INSERT INTO invoiceline (invoiceid, trackid, unitprice, quantity, invoicelineid) 
                    values (%s, %s, %s, %s, %s)""", (invoiceoficial, idOtrack, uptrack, 1, invoicelineoficial))
            invoiceoficial+=1
            invoicelineoficial+=1
            print("--------------------------")

        #conexion.commit()




        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conexion is not None:
            conexion.close()
            print('Conexión finalizada.')


if __name__ == '__main__':
    conectar()