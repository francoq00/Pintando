import turtle as t # Importamos el programa de turtle.
from turtle import * # de turtle importamos * en especifico.
from freegames import vector # de Freegames importamos vector.


def line(start, end): # Definimos el proceso para hacer lineas
    "Draw line from start to end."
    up() # Se levanta la pluma para que No dibuje nada.
    goto(start.x, start.y) # Nos movemos a donde se de click en el mouse.
    down() # Bajamos la pluma para que ahora si dibuje la trayectoria.
    goto(end.x, end.y) # Nos movemos a donde se de click en el mouse (Ya con la trayectoria marcada).

def square(start, end): # Definimos el proceso para hacer un cuadrado
    "Draw square from start to end."
    up() # Se levanta la pluma para que No dibuje nada.
    goto(start.x, start.y) # Se levanta la pluma para que No dibuje nada.
    down() # Bajamos la pluma para que ahora si dibuje la trayectoria.
    begin_fill() # Se empieza a llenar el cuadrado.

    for count in range(4): # Ciclo pata los lados del cuadrado (4).
        forward(end.x - start.x) # Hacemos la distancia que seran los lados del cuadrado.
        left(90) # gira 90 grados.

    end_fill() # Se termina de llenar el cuadrado, una vez que ya esta completamente cerrado.



def circle(start,end): # definimos el proceso para hacer el ciculo con ayuda de turtle.

    "Draw circle from start to end."
    up() # Se levanta la pluma para que No dibuje nada.
    goto(start.x, start.y) # Nos movemos a donde se de click en el mouse.
    radio = end.x-start.x # Definimos la distamcia del circulo.
    down() # Bajamos la pluma para que ahora si dibuje la trayectoria.
    t.circle(radio) # turtle tiene la fucnion para hacer un circulo, nosotros solo le definimos la medida.
    


def rectangle(start, end): # definimos el proceso para crear el rectángulo
    for count in range(4): # Ciclo para los lados del RECTÁNGULO (4).
        forward(180) # Hacemos la distancia que seran los lados del RECTÁNGULO.
        left(90) # gira 90 grados.
    end_fill() # Se termina de llenar el RECTÁNGULO, una vez que ya esta completamente cerrado.
  
def triangle(start, end): # definimos el proceso para crear el TRIÁNGULO
    "Draw triangle from start to end."
    for count in range(3): # Ciclo pata los lados del TRIÁNGULO (3).
          forward(end.x - start.x) # Hacemos la distancia que seran los lados del TRIÁNGULO.
          left(90) # gira 90 grados.
    
    end_fill() # Se termina de llenar el TRIÁNGULO, una vez que ya esta completamente cerrado.
    pass  # TODO

def tap(x, y): # Se define la funcion para que el pograma, sepa de donde a donde estamos tocando el mouse.
    "Store starting point or draw shape."
    start = state['start'] # Se empieza desde el principio.

    if start is None: # cuando el inicio sea ninguno
        state['start'] = vector(x, y) # el estado sera el vector en x,y.
    else: # si no
        shape = state['shape'] # definimos el tamaño desde el principio.
        end = vector(x, y) # se acabara en la pocicion de x,y.
        shape(start, end) # definimos que el tamaño sera desde el principio hasta el fin.
        state['start'] = None # se acaba.

def store(key, value): # definimso que el valor de la flecha es en la pocicion donde se de clic.
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line} # Empezamos con la forma de una linea, 
setup(420, 420, 370, 0)
onscreenclick(tap) # definimos que funcionara con un tap del mouse en el canvas de el programa.
listen() # empezamos el listen
onkey(undo, 'u') # si se teclea la tecla u minuscula, se va a deshacer el trazo previo.
onkey(lambda: color('cyan'), 'C') # En este punto agregue el color cyan al codigo al presionar la tecla C Mayscula.
onkey(lambda: color('black'), 'K') # En este punto se declara el color negro al codigo al presionar la tecla K Mayscula.
onkey(lambda: color('white'), 'W') # En este punto se declara el color blanco al codigo al presionar la tecla W Mayscula.
onkey(lambda: color('green'), 'G') # En este punto se declara el color verde al codigo al presionar la tecla G Mayscula.
onkey(lambda: color('blue'), 'B') # En este punto se declara el color azul al codigo al presionar la tecla B Mayscula.
onkey(lambda: color('red'), 'R') # En este punto se declara el color rojo al codigo al presionar la tecla R Mayscula.
onkey(lambda: store('shape', line), 'l') # En este punto se declara que al presionar la tecla l minuscula, la froma (funcion) que haga sea la de una linea.
onkey(lambda: store('shape', square), 's') # En este punto se declara que al presionar la tecla s minuscula, la froma (funcion) que haga sea un cuadrado.
onkey(lambda: store('shape', circle), 'c') # En este punto se declara que al presionar la tecla c minuscula, la froma (funcion) que haga sea un circulo.
onkey(lambda: store('shape', rectangle), 'r') # En este punto se declara que al presionar la tecla r minuscula, la froma (funcion) que haga sea un rectangulo.
onkey(lambda: store('shape', triangle), 't') # En este punto se declara que al presionar la tecla t minuscula, la froma (funcion) que haga sea un triangulo.

done()# cerramos el listen

