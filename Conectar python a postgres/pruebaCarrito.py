import pymongo
from datetime import datetime, timedelta
#conectar a mongo
conexion=pymongo.MongoClient() 
db=conexion.proyectoBD
coleccion=db.carrito

def add_item_to_cart(customer_id, track_id, unit_price):
    now = datetime.utcnow()

    # Asegurarse que el carrito esta activo
    result = coleccion.update(
        {'_id': customer_id, 'status': 'active' },
        { '$set': { 'last_modified': now },
          '$push': {
              'tracks': {'customer_id': customer_id, 'track_id': track_id, 'unit_price': unit_price} } },
        w=1)

def update_cart(customer_id, track_id):
    now = datetime.utcnow()
    
    # Make sure the cart is still active and add the line item
    result = coleccion.update(
        {'_id': customer_id, 'status': 'active', 'tracks.track_id': track_id },
        { '$set': { 'last_modified': now },
            '$pull': {
                'tracks': {'customer_id': customer_id, 'track_id': track_id} },
        },
        w=1)

def checkout(customer_id):
    now = datetime.utcnow()

    cart = coleccion.find_and_modify(
        {'_id': cart_id, 'status': 'active' },
        update={'$set': { 'status': 'pending', 'last_modified': now } } )
    
    try:
        #collect_payment(cart)
        coleccion.update(
            {'_id': cart_id },
            {'$set': { 'status': 'complete' } } )
    except:
        coleccion.update(
            {'_id': cart_id },
            {'$set': { 'status': 'active' } } )

def expire_carts(timeout):
    now = datetime.utcnow()
    threshold = now - timedelta(seconds=timeout)

    # Lock and find all the expiring carts
    coleccion.update(
        {'status': 'active', 'last_modified': { '$lt': threshold } },
        {'$set': { 'status': 'expiring' } },
        multi=True )

    # Actually expire each cart
    for cart in coleccion.find({'status': 'expiring'}):

        # Return all line items to inventory
        for item in cart['tracks']:
            db.inventory.update(
                { '_id': item['sku'],
                  'carted.cart_id': cart['_id'],
                  'carted.qty': item['qty']
                },
                {'$inc': { 'qty': item['qty'] },
                 '$pull': { 'carted': { 'cart_id': cart['_id'] } } })

        db.cart.update(
            {'_id': cart['_id'] },
            {'$set': { 'status': 'expired' }})



#------------------------MAIN------------------------------------

menu = "1. Agregar items a un shopping cart \n2. Modificar la cantidad de items en un shopping cart \n3. Hacer un check out de un shopping cart \n4. Retornar inventario de shopping carts expirados \n5. Salir"
opcion = 0

while (opcion != 5):
	print(menu)
	opcion=int(input("Ingrese una opcion: "))
	if (opcion == 1):
		cartID = int(input("Ingrese el ID de su carrito: "))
		sku = input("Ingrese el sku de su producto: ")
		qty = int(input("Ingrese la cantidad de articulos: "))
		details = input("Algun comentario que desee añadir: ")
		resultado = add_item_to_cart(cartID, sku, qty, details)
	if (opcion == 2):
		cartID = int(input("Ingrese el ID de su carrito: "))
		sku = input("Ingrese el sku de su producto: ")
		old_qty = int(input("Ingrese la antigua cantidad de articulos: "))
		new_qty = int(input("Ingrese la nueva cantidad de articulos: "))
		resultado = update_quantity(cartID, sku, old_qty, new_qty)
	if (opcion == 3):
		cartID = int(input("Ingrese el ID de su carrito: "))
		resultado = checkout(cartID)
	if (opcion == 4):
		timeout = int(input("Ingrese el tiempo en segundos: "))
		resultado = expire_carts(timeout)
