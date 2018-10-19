import sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def show(conn,clase):
	cur=conn.cursor()
	if clase=='ubicacion':
		at_ubicacion() 
		cur.execute("SELECT * FROM ubicacion   ")
		rows=cur.fetchall()
		for row in rows:
			print(row)
	elif clase=='contacto':
		at_contacto()
		cur.execute("SELECT * FROM contacto    ")
		rows=cur.fetchall()
		for row in rows:
			print(row)
	elif clase=='empresa':
		at_empresa()
		cur.execute("SELECT * FROM empresa    ")
		rows=cur.fetchall()
		for row in rows:
			print(row)
	elif clase=='finanzas':
		at_finanzas()
		cur.execute("SELECT * FROM finanzas    ")
		rows=cur.fetchall()
		for row in rows:
			print(row)
	elif clase=='documentos':
		at_documentos()
		cur.execute("SELECT * FROM documentos  ")
		rows=cur.fetchall()
		for row in rows:
			print(row)
	elif clase=='producto':
		at_producto()
		cur.execute("SELECT * FROM producto")
		rows=cur.fetchall()
		for row in rows:
			print(row)
	elif clase=='provedores':
		at_provedores()
		cur.execute("SELECT * FROM provedores")
		rows=cur.fetchall()
		for row in rows:
			print(row)
	elif clase=='importaciones':
		at_importaciones()
		cur.execute("SELECT * FROM importaciones")
		rows=cur.fetchall()
		for row in rows:
			print(row)

	elif clase=='empleados':
		at_empleados()
		cur.execute("SELECT * FROM  empleados")
		rows=cur.fetchall()
		for row in rows:
			print(row)


	else:

		print('\nla clase no es valida\n')
 
 
def select_ubicacion(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM ubicacion	")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)

def at_ubicacion():
	print('ID NOMBRE CALLE NUMERO CP MUNICIPIO CIUDAD LATITUD LONGITUD')
	
def at_contacto():
	print ('ID NOMBRE TELFONO CORREO WEB FACEBOOK TWITTER INSTAGRAM LINKEDIN WHATSAPP')

def at_empresa():
	print('ID NOMBRE RSOCIAL TIPO TAMANO GIRO')

def at_finanzas():
	print('ID NOMBRE VENTAS GANANCIAS PERDIDAS INVERSIONES IMPUESTOS')

def at_documentos():
	print('ID NOMBRE CERTIFICACIONES PERMISOS SEGURO')

def at_producto():
	print ('ID NOMBRE TIPO PRECIO SECTOR DEMANANDA')

def at_provedores():
	print('ID NOMBRE CANTIDAD MATERIALES PRECIO FRECUENCIA')

def at_importaciones():
	print('ID NOMBRE ORIGEN DESTINO TRASLADO TIEMPO LOTE')

def at_empleados():
	print('ID NOMBRE NUMERO SUELDO SEGURO PRESTACIONES')

def select_contacto(conn):
	at_contacto()
	cur = conn.cursor()
	cur.execute("SELECT * FROM contacto  ")
	rows=cur.fetchall()
	for row in rows:
		print(row)
    
"""def select_task_by_priority(conn, priority):
    
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM ubicacion WHERE priority=?", (priority,))
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)"""
def mostrar(conn):
	cur=conn.cursor()
	cur.execute("SELECT * FROM sqlite_master WHERE type = 'table' ")
def seleccionar(conn,actual):
	if actual=="ubicacion":
		select_ubicacion(conn)
	elif actual=="contacto":
		select_contacto(conn)
	else:
		print 'NO EXISTE'

def insert_ubicacion(conn,datos):
    cur=conn.cursor()
    cur.execute("Insert INTO ubicacion values(?,?,?,?,?,?,?,?,?)",datos)

def insert_contacto(conn,datos):
	cur=conn.cursor()
	cur.execute("Insert INTO contacto values(?,?,?,?,?,?,?,?,?,?)".datos)


def cambiar(conn,actual):
	cur=conn.cursor()
	if actual=='ubicacion':
		
		show(conn,actual)
		emp=raw_input('Ingresa ID  a modificar')
		nombre=raw_input('Ingresa nuevo nombre: ')
		calle=raw_input('Ingresa nuevo calle: ')
		numero=raw_input('Ingresa nuevo numero: ')
		cp=raw_input('Ingresa nuevo cp: ')
		municipio=raw_input('Ingresa nuevo municipio: ')
		ciudad=raw_input('Ingresa nueva ciudad : ')
		latitud=raw_input('Ingresa nueva latitud : ')
		longitud=raw_input('Ingresa nueva longitud : ')

		"""
		cur.execute("UPDATE 'ubicacion'")
		cur.execute("SET raw_input('Atributo a modificar:  ')=raw_input('nuevo valor:  ')")
		cur.execute("WHERE id=emp")"""
		sql='''UPDATE ubicacion
		   SET nombre=?,
		       calle=?,
		       numero=?,
		       cp=?,
		       municipio=?,
		       ciudad=?,
		       latitud=?,
		       longitud=?
		   WHERE id=?'''
		cur=conn.cursor()
		cur.execute(sql,(nombre,calle,numero,cp,municipio,ciudad,latitud,longitud,emp))

		show(conn,actual)

	elif actual=='contacto':

		show(conn,actual)
		emp=input('Ingresa ID a modificar')
		nombre=raw_input('Ingresa nuevo nombre: ')
		telefono=raw_input('Ingresa nuevo telefono: ')
		correo =raw_input('Ingresa nuevo correo: ')
		web =raw_input('Ingresa nuevo web: ')
		facebook =raw_input('Ingresa nuevo facebook: ')
		twitter =raw_input('Ingresa nuevo twitter: ')
		instagram =raw_input('Ingresa nuevo instagram: ')
		linkedin =raw_input('Ingresa nuevo linkedin: ')
		whatsapp =raw_input('Ingresa nuevo whatsapp: ')

		sql='''UPDATE contacto
		   SET nombre=?,
		       telefono=?,
		       correo=?,
		       web=?,
		       facebook=?,
		       twitter=?,
		       instagram=?,
		       linkedin=?,
		       whatsapp=?
		   WHERE id=?'''
		cur=conn.cursor()
		cur.execute(sql,(nombre,telefono,correo,web,facebook,twitter,instagram,linkedin,whatsapp,emp))

		show(conn,actual)


		"""emp=raw_input('Ingresa la empresa a modificar')
    	UPDATE contacto
       	SET raw_input('Atributo a modificar: ')=raw_input('nuevo valor: ')
       	WHERE nombre=emp"""

	elif actual=='empresa':
		show(conn,actual)
		id=input('Ingresa ID a modificar:  ')
		nombre=raw_input('Ingresa nuevo nombre:   ')
		rsocial =raw_input('Ingresa nuevo razon social:   ')
		tipo =raw_input('Ingresa nuevo tipo:   ')
		tamano =raw_input('Ingresa nuevo tamano:   ')
		giro =raw_input('Ingresa nuevo giro:   ')

		sql='''UPDATE empresa
			   SET nombre=?,
			   	   rsocial=?,
			   	   tipo=?,
			   	   tamano=?,
			   	   giro =?
			   WHERE id =?'''


		cur=conn.cursor()
		cur.execute(sql,(nombre,rsocial,tipo,tamano,giro,id))
		show(conn,actual)


	elif actual=='finanzas':
		id=input('Introduce ID a modificar')
		nombre=raw_input('Introduce nuevo nombre:   ')
		ventas=raw_input('Introduce nuevas ventas :   ')
		ganancias =raw_input('Introduce nuevas ganancias :   ')
		perdidas =raw_input('Introduce nuevo perdidas:  ')
		inversiones =raw_input('Introduce nuevas inversiones: ')
		impuestos =raw_input('Introduce nuebvo:   ' )
		

		sql='''UPDATE finanzas
			   SET nombre=?
			       ventas=?
			       ganancias=?
			       perdidas=?
			       inversiones=?
			       impuestos=?
			   WHERE id = ?'''

		cur=conn.cursor()
		cur.execute(sql,(nombre,ventas,ganancias,perdidas,inversiones,impuestos,id))
		show(conn,actual)
	
	elif actual=='documentos':
		
		nom=input('Introducd ID a modificar: ')
		nombre=raw_input('Introduce nuevo nombre: ')
		certificaciones =raw_input('Introduce nuevas calificaciones: ')
		permisos =raw_input('Introduce nuevos permisos:  ')
		seguro =raw_input('Introduce nuova: ')

		sql='''UPDATE documentos
			   SET nombre=?
			       certificaciones=?
			       permisos=?
			       seguros=?
			   WHERE id=?'''
		cur=conn.cursor()
		cur.execute(sql,(nombre,certificaciones,permisos,seguros,nom))



	elif actual=='producto':
		id=input('Introducir ID a modificar')
		nombre=raw_input('Introduce nuevo nombre: ')
		tipo=raw_input('Introduce nuevo tipo: ')
		precio = raw_input('Introduce nuevo precio: ')
		sector = raw_input('INtroduce el nuevo sector')
		demanda = raw_input('Introduce la demanda: ')

		sql='''UPDATE producto
			   SET  nombre=?
			   		tipo=?
			   		precio=?
			   		sector=?
			   		demanda=?
			   	WHERE id=?'''

		cur=conn.cursor()
		cur.execute(sql,(nombre,tipo,precio,sector,demanda,id))


	elif actual=='provedores':
		ed=input('INgresa ID a modificar')
		nombre=raw_input('Introduce nuevo nombre:  )')
		cantidad =raw_input('Introduce nueva cantidad:  ')
		materiales =raw_input('Introduce nuevos materiales :  ')
		precio =raw_input('Introduce nuevo precio:  ')
		frecuencia =raw_input('Introduce nueva frecuencia:  ')
		sql='''UPDATE provedores
			   SET nombre=?
			   	   cantidad=?
			   	   materiales=?
			   	   precio=?
			   	   frecuencia=?
			   WHERE id=?'''


		cur=conn.cursor()
		cur.execute(sql,(nombre,cantidad,materiales,precio,frecuencia,ed))



	elif actual=='empleados':
		id=input('Ingresa ID a modificar')
		nombre=raw_input('Introduce nuevo nombre')
		numero=raw_input('Introduce nuevo numero]')
		sueldo =raw_input('Introduce nuevo sueldo')
		seguro =raw_input('Introduce nuevo suegro')
		prestaciones =raw_input('prestaciones')

		sql='''UPDATE empleados
			   SET nombre=?
			   	   numero=?
				   sueldo=?
				   seguro=?
				   prestaciones=?
			   WHERE id=?'''

		cur=conn.cursor()
		cur.execute(sql,(nombre,numero,sueldo,seguro,prestaciones,ed))





	else:

		print('\nla clase no es valida\n')
	

def delete(conn,actual):
	cur=conn.cursor()
	if actual=='ubicacion':
		id=input('Ingresa ID de elemento para eliminar')
		sql='DELETE FROM ubicacion WHERE id=?'
		cur.execute(sql,(id,))

	elif actual=='contacto':
		id=input('Ingresa ID de elemento para eliminar')
		sql='DELETE FROM contacto WHERE id=?'
		cur.execute(sql,(id,))
	elif actual=='empresa':
		id=input('Ingresa ID de elemento para eliminar')
		sql='DELETE FROM empresa WHERE id=?'
		cur.execute(sql,(id,))
	elif actual=='finanzas':
		id=input('Ingresa ID de elemento para eliminar')
		sql='DELETE FROM finanzas WHERE id=?'
		cur.execute(sql,(id,))
	elif actual=='documentos':
		id=input('Ingresa ID de elemento para eliminar')
		sql='DELETE FROM documentos WHERE id=?'
		cur.execute(sql,(id,))
	elif actual=='producto':
		id=input('Ingresa ID de elemento para eliminar')
		sql='DELETE FROM producto WHERE id=?'
		cur.execute(sql,(id,))
	elif actual=='provedores':
		id=input('Ingresa ID de elemento para eliminar')
		sql='DELETE FROM provedores WHERE id=?'
		cur.execute(sql,(id,))
	elif actual=='importaciones':
		id=input('Ingresa ID de elemento para eliminar')
		sql='DELETE FROM importaciones WHERE id=?'
		cur.execute(sql,(id,))
	elif actual=='empleados':
		id=input('Ingresa ID de elemento para eliminar')
		sql='DELETE FROM empleados WHERE id=?'
		cur.execute(sql,(id,))

	else:
		print ('Ingresa opcion valida')

def insert(conn,actual):
	cur=conn.cursor()
	if actual=='ubicacion':
		id=input('Ingresa ID: ')
		nombre=raw_input('Ingresa nombre: ')
		calle=raw_input('Ingresa calle: ')
		numero=raw_input('Ingresa numero: ')
		cp=raw_input('Ingresa cp: ')
		municipio=raw_input('Ingresa municipio: ')
		ciudad=raw_input('Ingresa ciudad: ')
		latitud=raw_input('Ingresa latitud: ')
		longitud=raw_input('Ingresa longitud: ')

		sql='''INSERT INTO ubicacion(id,nombre,calle,numero,cp,municipio,ciudad,latitud,longitud)
			   VALUES (?,?,?,?,?,?,?,?,?)'''
		cur.execute(sql,(id,nombre,calle,numero,cp,municipio,ciudad,latitud,longitud))
		return cur.lastrowid

	elif actual=='contacto':

		show(conn,actual)
		id=input('Ingresa ID: ')
		nombre=raw_input('Ingresa nuevo nombre: ')
		telefono=raw_input('Ingresa nuevo telefono: ')
		correo =raw_input('Ingresa nuevo correo: ')
		web =raw_input('Ingresa nuevo web: ')
		facebook =raw_input('Ingresa nuevo facebook: ')
		twitter =raw_input('Ingresa nuevo twitter: ')
		instagram =raw_input('Ingresa nuevo instagram: ')
		linkedin =raw_input('Ingresa nuevo linkedin: ')
		whatsapp =raw_input('Ingresa nuevo whatsapp: ')

		sql='''INSERT INTO contacto(id,nombre,telefono,correo,web,facebook,twitter,instagram,linkedin,whatsapp)
			   VALUES (?,?,?,?,?,?,?,?,?,?)'''
		cur.execute(sql,(id,nombre,telefono,correo,web,facebook,twitter,instagram,linkedin,whatsapp))
		return cur.lastrowid
		show(conn,actual)


	elif actual=='empresa':
		show(conn,actual)
		id=input('Ingresa ID a modificar:  ')
		nombre=raw_input('Ingresa nuevo nombre:   ')
		rsocial =raw_input('Ingresa nuevo razon social:   ')
		tipo =raw_input('Ingresa nuevo tipo:   ')
		tamano =raw_input('Ingresa nuevo tamano:   ')
		giro =raw_input('Ingresa nuevo giro:   ')

		sql='''INSERT INTO empresa(id,nombre,rsocial,tipo,tamano,giro)
			   VALUES (?,?,?,?,?,?,)'''
		cur.execute(sql,(id,nombre,rsocial,tipo,tamano,giro))
		return cur.lastrowid


	elif actual=='finanzas':
		id=input('Introduce ID a modificar')
		nombre=raw_input('Introduce nuevo nombre:   ')
		ventas=raw_input('Introduce nuevas ventas :   ')
		ganancias =raw_input('Introduce nuevas ganancias :   ')
		perdidas =raw_input('Introduce nuevo perdidas:  ')
		inversiones =raw_input('Introduce nuevas inversiones: ')
		impuestos =raw_input('Introduce nuebvo:   ' )
		

		sql='''INSERT INTO finanzas(id,nombre,ventas,ganancias,perdidas,inversiones,impuestos)
			   VALUES (?,?,?,?,?,?,?)'''
		cur.execute(sql,(id,nombre,ventas,ganancias,perdidas,inversiones,impuestos))
		return cur.lastrowid
	
	elif actual=='documentos':
		
		id=input('Introducd ID a modificar: ')
		nombre=raw_input('Introduce nuevo nombre: ')
		certificaciones =raw_input('Introduce nuevas calificaciones: ')
		permisos =raw_input('Introduce nuevos permisos:  ')
		seguro =raw_input('Introduce nuova: ')

		sql='''INSERT INTO documentos(id,nombre,certificaciones,permisos,seguro)
			   VALUES (?,?,?,?,?)'''
		cur.execute(sql,(id,nombre,certificaciones,permisos,seguro))
		return cur.lastrowid

	elif actual=='producto':
		id=input('Introducir ID a modificar')
		nombre=raw_input('Introduce nuevo mounstro: ')
		tipo=raw_input('Introduce nuevo tipo barco: ')
		precio = raw_input('Introduce nuevo precio: ')
		sector = raw_input('INtroduce el nuevo sector')
		demanda = raw_input('Introduce metro miguel angel: ')

		sql='''INSERT INTO producto(id,nombre,tipo,precio,sector,demanda)
			   VALUES (?,?,?,?,?,?)'''
		cur.execute(sql,(id,nombre,tipo,precio,sector,demanda))
		return cur.lastrowid

	elif actual=='provedores':
		id=input('INgresa ID a modificar')
		nombre=raw_input('Introduce nuevo nombre:  )')
		cantidad =raw_input('Introduce nueva cantidad:  ')
		materiales =raw_input('Introduce nuevos materiales :  ')
		precio =raw_input('Introduce nuevo precio:  ')
		frecuencia =raw_input('Introduce nueva frecuencia:  ')
		sql='''INSERT INTO provedores(id,nombre,cantidad,materiales,precio,frecuencia)
			   VALUES (?,?,?,?,?,?)'''
		cur.execute(sql,(id,nombre,cantidad,materiales,precio,frecuencia))
		return cur.lastrowid



	elif actual=='empleados':
		id=input('Ingresa ID a modificar')
		nombre=raw_input('Introduce nuevo nombre')
		numero=raw_input('Introduce nuevo numero]')
		sueldo =raw_input('Introduce nuevo sueldo')
		seguro =raw_input('Introduce nuevo suegro')
		prestaciones =raw_input('prestaciones')

		sql='''INSERT INTO empleados(id,nombre,numero,sueldo,seguro,prestaciones)
			   VALUES (?,?,?,?,?,?)'''
		cur.execute(sql,(id,nombre,numero,sueldo,seguro,prestaciones))
		return cur.lastrowid



	else:

		print('\nla clase no es valida\n')
	
	"""	
	elif actual=='contacto'
	elif actual=='empresa'
	elif actual=='finanzas'
	elif actual=='documentos'
	elif actual=='producto'
	elif actual=='provedores'
	elif actual=='importaciones'
	"""
def search(conn,actual):
	cur=conn.cursor()
	if actual=='ubicacion':
		at_ubicacion()
		at=raw_input('Que atributo quieres buscar: ')
		nombre=raw_input('Cual deseas buscar?: ')
		try:
			sql='''SELECT * FROM ubicacion
				   WHERE nombre=?'''

			cur.execute(sql,(nombre))
			print(cur.fetchone())
		except Exception as e:
			print ('No existe ese elemento')


def main():
    database = "pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        #print("1. Query task by priority:")
        #select_task_by_priority(conn,1)
 
        #print("2. Query all tasks")
        #select_all_tasks(conn)
        """
        print("3. insert_task")
        insert_task(conn,(5,'tarea 5','22/10/18'))
        """
        op=1
        while op!=7:

            print (" Que clase quiere entrar: ")
            print(" contacto  documentos  empleados  empresa\n finanzas  importaciones  producto  provedores\n ubicacion")
            mostrar(conn)
            op=1
            actual=raw_input()
            while op!=6 and op!=7 :
	            print ("1. Mostrar datos")
	            print ("2. Editar objeto")
	            print ("3. Eliminar objeto")
	            print ("4. Buscar objeto por atributo")
	            print ("5. Agregar objeto")
	            print ("6. Cambiar clase")
	            print ("7. Salir del programa")
        	    op=input("Que quieres: ")
        	    if op==1:
        	    	show(conn,actual)
        	    	

        	    elif op==2:
        	    	cambiar(conn,actual)

        	    elif op==3:
        	    	delete(conn,actual)

        	    elif op==4:
        	    	search(conn,actual)

        	    elif op==5:
        	    	insert(conn,actual)
        	    	

        	    elif op==6:
        	    	print ('')

        	    elif op==7:
        	    	print ('Gracias, vuelva pronto :)')

        	    else:
        	    	print("ingrese opcion valida")



            
					
 
if __name__ == '__main__':
    main()