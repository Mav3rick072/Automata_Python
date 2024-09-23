#Automata Python v2.1

# Definicion del autómata con sus estados y transiciones
automata = {
    'q0': {'a': 'q1', 'b': 'q2'},
    'q1': {'a': 'q1', 'b': 'q1'},  # q1 es un estado de bucle sobre sí mismo para 'a' y 'b'
    'q2': {'a': 'q2', 'b': 'q2'}   # q2 también tiene bucles
}

# Estado inicial y estados de aceptación
estado_inicial = 'q0'
estados_aceptacion = ['q1']  # El estado q1 es el único estado de aceptación (círculo doble)

# Función para procesar la cadena en el autómata
def procesar_automata(cadena):
    estado_actual = estado_inicial  # Comenzamos en el estado inicial
    print(f"Estado inicial: {estado_actual}")
    
    # Procesamos cada símbolo de la cadena
    for simbolo in cadena:
        if simbolo in automata[estado_actual]:
            estado_actual = automata[estado_actual][simbolo]
            print(f"Símbolo: '{simbolo}' -> Nuevo estado: {estado_actual}")
        else:
            print(f"Símbolo no reconocido: '{simbolo}' en el estado {estado_actual}")
            return False  # Si hay un símbolo no reconocido, rechazamos la cadena
    
    # Verificacion si en el estado final es un estado de aceptación
    if estado_actual in estados_aceptacion:
        print(f"Cadena !Aceptada¡ en el estado: {estado_actual}")
        return True
    else:
        print(f"Cadena NO aceptada, terminó en el estado: {estado_actual}")
        return False

# Ejemplo de uso
cadena = input("Introduce la cadena de entrada (compuesta de 'a' y 'b'): ")
if procesar_automata(cadena):
    print("Resultado: Cadena aceptada.")
else:
    print("Resultado: Cadena no aceptada.")
