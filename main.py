__author__ = 'JuanMaAV92'

'''
	Detector de secuencia de sensor digital 0/1  (maquina de estado)
	El sensor es simulado solitando al usuario un valor digital [ '0', '1']
'''

def showState( state:int ):
	print ( '*' * 10)	
	print ( f'Estado {state}')
	print ( '*' * 10)	

sequence = ( 1, 0, 0, 1)

index_sequence = 0		# Indica el numero de deteccion de la secuencia.

print ( f'Inicia detector de secuencia {sequence}')
showState( 0 )


while True:

	entrada = input('Introduzca el valor digital del sensor "0" o "1", si desea cerrar el programa digite "2" : ') 

	if entrada == '2':
		break

	else:

		try:
			entrada = int(entrada)

			if index_sequence == 0 and entrada == sequence[0]:
				index_sequence += 1
				showState( index_sequence )

			elif index_sequence == 1:
				if entrada == sequence[1]:
					index_sequence += 1
					showState( index_sequence )
				else:
					index_sequence = 0
					showState( index_sequence )

			elif index_sequence == 2:
				if entrada == sequence[2]:
					index_sequence += 1
					showState( index_sequence )
				else:
					index_sequence = 0
					showState( index_sequence )		

			elif index_sequence == 3:
				if entrada == sequence[3]:
					showState( index_sequence + 1 )					
					print("\U0001F601 secuencia detectada \U0001F601")
					index_sequence = 0 
				else:
					index_sequence = 0
					showState( index_sequence )
			else:
				showState( index_sequence )
	 	

		except: 
		 	print('Esa no vale')


