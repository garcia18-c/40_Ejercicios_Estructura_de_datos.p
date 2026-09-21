#Ejercicio 1 VALIDADOR DE NOTAS


#Entrada:
#Una o varias notas.

#Proceso:
#Validar que cada nota esté entre 0 y 100,
#guardar únicamente las notas válidas en una lista
#y calcular el promedio.

#Salida:
#Lista de notas válidas y promedio.

#BOSQUEJO A MANO

#Notas recibidas:
#85, 92, 110, 78, -5, 88

#Lista inicial:
#[]

#¿85 es válida? 0<=85<=100 → Sí → guardar
#Lista: [85]

#¿92 es válida? 0<=92<=100 → Sí → guardar
#Lista: [85,92]

#¿110 es válida? 0<=110<=100 → No → no guardar
#Lista: [85,92]

#¿78 es válida? 0<=78<=100 → Sí → guardar
#Lista: [85,92,78]

#¿-5 es válida? 0<=-5<=100 → No → no guardar
#Lista: [85,92,78]

#¿88 es válida? 0<=88<=100 → Sí → guardar
#Lista: [85,92,78,88]

#Promedio:
#85+92+78+88 = 343
#343/4 = 85.75

#DESCUBRIR EL PATRÓN

#1. validar_nota(nota): comprueba si la nota está entre 0 y 100.
#2. cargar_notas(*args): recorre las notas y reutiliza validar_nota()
#   para guardar solo las válidas.
#3. notas: lista que almacena únicamente las notas válidas.
#4. promedio(): usa sum() y len() sobre la lista de notas.
#5. __init__: inicializa la lista vacía.

#CÓDIGO

class Calificador:

    def __init__(self):
        self.notas = []

    def validar_nota(self, nota):
        if 0 <= nota <= 100:
            return True
        else:
            return False

    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)

        return self.notas

    def promedio(self):
        return sum(self.notas) / len(self.notas)


c = Calificador()
print(c.cargar_notas(85, 92, 110, 78, -5, 88))
print(c.promedio())

#PRUEBA DE ESCRITORIO

#| Nota | ¿Válida? | Lista |
#| 85 | Sí | [85] |
#| 92 | Sí | [85,92] |
#| 110 | No | [85,92] |
#| 78 | Sí | [85,92,78] |
#| -5 | No | [85,92,78] |
#| 88 | Sí | [85,92,78,88] |

#Salida:
#[85, 92, 78, 88]
#85.75


#Ejercicio 2 CONTADOR DE PALABRAS ÚNICAS


#Entrada:
#Una o varias palabras, individualmente o en lotes.

#Proceso:
#Guardar las palabras en un conjunto para evitar duplicados y en
#una lista para conservar el orden. Luego contar las palabras únicas.

#Salida:
#Cantidad de palabras únicas.

#BOSQUEJO A MANO

#Palabras recibidas:
#"hola", "mundo", "hola"

#Conjunto inicial:
#{}
#Lista inicial:
#[]

#¿"hola" ya está en el conjunto? No → es nueva
#Conjunto: {"hola"}
#Lista: ["hola"]

#¿"mundo" ya está en el conjunto? No → es nueva
#Conjunto: {"hola","mundo"}
#Lista: ["hola","mundo"]

#¿"hola" ya está en el conjunto? Sí → no se duplica en el conjunto
#Conjunto: {"hola","mundo"}
#Lista: ["hola","mundo","hola"]

#DESCUBRIR EL PATRÓN

#1. agregar_palabra(palabra): agrega la palabra al conjunto y a la lista.
#2. agregar_multiples(*args): recorre varias palabras y reutiliza
#   agregar_palabra().
#3. palabras_unicas: conjunto sin duplicados.
#4. orden: lista que conserva el orden, con repeticiones.
#5. contar_palabras(): usa len() sobre el conjunto.
#6. __init__: inicializa el conjunto y la lista vacíos.

#CÓDIGO

class AnalizadorTexto:

    def __init__(self):
        self.palabras_unicas = set()
        self.orden = []

    def agregar_palabra(self, palabra):
        self.palabras_unicas.add(palabra)
        self.orden.append(palabra)

    def contar_palabras(self):
        return len(self.palabras_unicas)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)


at = AnalizadorTexto()
at.agregar_multiples("hola", "mundo", "hola")

print("Conjunto:", at.palabras_unicas)
print("Lista:", at.orden)
print("Cantidad de palabras unicas:", at.contar_palabras())

#PRUEBA DE ESCRITORIO

#| Palabra | ¿Nueva? | Conjunto | Lista |
#| hola | Sí | {hola} | [hola] |
#| mundo | Sí | {hola,mundo} | [hola,mundo] |
#| hola | No | {hola,mundo} | [hola,mundo,hola] |

#Salida:
#Cantidad de palabras unicas: 2


#Ejercicio 3 CARRO DE COMPRAS


#Entrada:
#Nombres de artículos y sus precios.

#Proceso:
#Guardar cada artículo en un diccionario usando el nombre como clave
#y el precio como valor. Sumar todos los precios para obtener el total.
#Filtrar los artículos cuyo precio esté dentro de un rango.

#Salida:
#Total del carrito y artículos dentro del rango de precios indicado.

#BOSQUEJO A MANO

#Artículos:
#"pan" → 2.50
#"leche" → 3.00
#"arroz" → 5.00
#"queso" → 8.00

#Diccionario:
#{"pan":2.50, "leche":3.00, "arroz":5.00, "queso":8.00}

#Total:
#2.50+3.00+5.00+8.00 = 18.50

#Rango $3 a $5:
#"pan" → 2.50 → No
#"leche" → 3.00 → Sí
#"arroz" → 5.00 → Sí
#"queso" → 8.00 → No

#Resultado:
#["leche", "arroz"]

#DESCUBRIR EL PATRÓN

#1. agregar_articulo(nombre, precio): guarda el artículo en el diccionario.
#2. total_carrito(): recorre los valores del diccionario y los suma.
#3. articulos_por_rango(precio_min, precio_max): filtra los artículos
#   cuyo precio esté dentro del rango.
#4. articulos: diccionario nombre → precio.
#5. __init__: inicializa el diccionario vacío.

#CÓDIGO

class CarroCompras:

    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        return sum(self.articulos.values())

    def articulos_por_rango(self, precio_min, precio_max):
        resultado = []

        for nombre, precio in self.articulos.items():
            if precio_min <= precio <= precio_max:
                resultado.append(nombre)

        return resultado


c = CarroCompras()
c.agregar_articulo("pan", 2.50)
c.agregar_articulo("leche", 3.00)
c.agregar_articulo("arroz", 5.00)
c.agregar_articulo("queso", 8.00)

print("Artículos:", c.articulos)
print("Total:", c.total_carrito())
print("Artículos en el rango:", c.articulos_por_rango(3, 5))

#PRUEBA DE ESCRITORIO

#| Artículo | Precio | ¿En rango 3-5? |
#| pan | 2.50 | No |
#| leche | 3.00 | Sí |
#| arroz | 5.00 | Sí |
#| queso | 8.00 | No |

#Salida:
#Total: 18.5
#Artículos en el rango: ['leche', 'arroz']


#Ejercicio 4 INVERSOR DE SECUENCIAS


#Entrada:
#Una lista o varias listas.

#Proceso:
#Invertir manualmente la lista utilizando bucles, sin usar reversed().
#Si se reciben varias listas, reutilizar invertir_lista() y guardar
#cada resultado en un diccionario.

#Salida:
#Una lista invertida o un diccionario con la lista original
#y su lista invertida.

#BOSQUEJO A MANO

#Lista:
#[1,2,3]

#Resultado inicial:
#[]

#Empezar desde el último elemento:
#3 → [3]
#2 → [3,2]
#1 → [3,2,1]

#Resultado:
#[3,2,1]

#Varias listas:
#[1,2,3] y [4,5,6]

#Diccionario inicial:
#{}

#Invertir [1,2,3] → [3,2,1]
#Guardar: {(1,2,3): [3,2,1]}

#Invertir [4,5,6] → [6,5,4]
#Guardar: {(1,2,3):[3,2,1], (4,5,6):[6,5,4]}

#DESCUBRIR EL PATRÓN

#1. invertir_lista(lista): recorre la lista desde el último elemento
#   hasta el primero y arma una nueva lista.
#2. invertir_multiples(*listas): recorre varias listas y reutiliza
#   invertir_lista().
#3. resultados: diccionario que guarda la lista original (como tupla,
#   porque las listas no pueden ser clave) y su versión invertida.
#4. __init__: no necesita atributos.

#CÓDIGO

class InversorSecuencia:

    def __init__(self):
        pass

    def invertir_lista(self, lista):
        resultado = []

        for i in range(len(lista) - 1, -1, -1):
            resultado.append(lista[i])

        return resultado

    def invertir_multiples(self, *listas):
        resultados = {}

        for lista in listas:
            original = tuple(lista)
            invertida = self.invertir_lista(lista)
            resultados[original] = invertida

        return resultados


inv = InversorSecuencia()
print(inv.invertir_lista([1, 2, 3]))
print(inv.invertir_multiples([1, 2, 3], [4, 5, 6]))

#PRUEBA DE ESCRITORIO

#| i | lista[i] | resultado |
#| 2 | 3 | [3] |
#| 1 | 2 | [3,2] |
#| 0 | 1 | [3,2,1] |

#Salida:
#[3, 2, 1]
#{(1, 2, 3): [3, 2, 1], (4, 5, 6): [6, 5, 4]}


#Ejercicio 5 DETECTOR DE PARES E IMPARES


#Entrada:
#Números en lote.

#Proceso:
#Usar % para clasificar cada número. Si numero % 2 == 0 es par;
#de lo contrario es impar. Guardar ambas categorías y contarlas.

#Salida:
#Diccionario {'pares': [...], 'impares': [...]} y tupla (cant_pares, cant_impares).

#BOSQUEJO A MANO

#Números:
#1, 2, 3, 4, 5

#Inicial:
#{"pares": [], "impares": []}

#1 % 2 = 1 → impar → [1]
#2 % 2 = 0 → par → [2]
#3 % 2 = 1 → impar → [1,3]
#4 % 2 = 0 → par → [2,4]
#5 % 2 = 1 → impar → [1,3,5]

#Resultado:
#{"pares":[2,4], "impares":[1,3,5]}
#Cantidad:
#(2,3)

#DESCUBRIR EL PATRÓN

#1. es_par(numero): retorna True si numero % 2 == 0.
#2. separar(*numeros): recorre números y reutiliza es_par().
#3. resultado: diccionario con listas para pares e impares.
#4. cantidad_pares_impares(): usa len() y retorna una tupla.
#5. __init__: inicializa el diccionario.

#CÓDIGO

class AnalizadorNumeros:

    def __init__(self):
        self.resultado = {
            "pares": [],
            "impares": []
        }

    def es_par(self, numero):
        if numero % 2 == 0:
            return True
        else:
            return False

    def separar(self, *numeros):
        for numero in numeros:
            if self.es_par(numero):
                self.resultado["pares"].append(numero)
            else:
                self.resultado["impares"].append(numero)

        return self.resultado

    def cantidad_pares_impares(self):
        cant_pares = len(self.resultado["pares"])
        cant_impares = len(self.resultado["impares"])
        return (cant_pares, cant_impares)


an = AnalizadorNumeros()
print(an.separar(1, 2, 3, 4, 5))
print(an.cantidad_pares_impares())

#PRUEBA DE ESCRITORIO

#| Número | es_par() | Pares | Impares |
#| 1 | False | [] | [1] |
#| 2 | True | [2] | [1] |
#| 3 | False | [2] | [1,3] |
#| 4 | True | [2,4] | [1,3] |
#| 5 | False | [2,4] | [1,3,5] |

#Cantidad:
#len(pares)=2
#len(impares)=3
#Salida: (2,3)

#Ejercicio 6 ESTADÍSTICAS DE TEMPERATURA


#Entrada:
#Temperaturas individuales o en lote.

#Proceso:
#Guardar las temperaturas en una lista y calcular mínima,
#máxima y promedio. Para varias temperaturas, reutilizar
#registrar_temperatura().

#Salida:
#Valores mínimo, máximo y promedio.

#BOSQUEJO A MANO

#Temperaturas:
#20, 25, 18, 30

#Lista inicial:
#[]

#20 → [20]
#25 → [20,25]
#18 → [20,25,18]
#30 → [20,25,18,30]

#Mínima = 18
#Máxima = 30
#Promedio = (20+25+18+30)/4 = 23.25

#DESCUBRIR EL PATRÓN

#1. registrar_temperatura(temp): agrega una temperatura a la lista.
#2. registrar_multiples(*temps): recorre las temperaturas y reutiliza
#   registrar_temperatura().
#3. minima(): usa min().
#4. maxima(): usa max().
#5. promedio(): suma y divide entre len().
#6. temperaturas: lista interna.

#CÓDIGO

class GestorTemperatura:

    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def registrar_multiples(self, *temps):
        for temp in temps:
            self.registrar_temperatura(temp)

    def minima(self):
        return min(self.temperaturas)

    def maxima(self):
        return max(self.temperaturas)

    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)


gt = GestorTemperatura()
gt.registrar_multiples(20, 25, 18, 30)

print(gt.minima())
print(gt.maxima())
print(gt.promedio())

#PRUEBA DE ESCRITORIO

#| Acción | Temperaturas | Salida |
#| registrar 20 | [20] | — |
#| registrar 25 | [20,25] | — |
#| registrar 18 | [20,25,18] | — |
#| registrar 30 | [20,25,18,30] | — |
#| minima() | misma | 18 |
#| maxima() | misma | 30 |
#| promedio() | misma | 23.25 |


#Ejercicio 7 MAPEADOR DE EDADES


#Entrada:
#Nombres y edades.

#Proceso:
#Guardar nombre → edad en un diccionario, filtrar personas con
#edad mayor o igual al mínimo y calcular promedio de edades.

#Salida:
#Lista de personas filtradas y promedio.

#BOSQUEJO A MANO

#Ana → 28
#Bob → 17
#Carlos → 22

#Diccionario:
#{"Ana":28, "Bob":17, "Carlos":22}

#Mayores o iguales a 18:
#Ana → sí
#Bob → no
#Carlos → sí

#Lista:
#["Ana", "Carlos"]

#Promedio:
#(28+17+22)/3 = 22.33

#DESCUBRIR EL PATRÓN

#1. agregar_persona(): guarda nombre → edad.
#2. personas_mayores(edad_minima): recorre items() y filtra.
#3. edad_promedio(): suma valores y divide por cantidad.
#4. personas: diccionario interno.
#5. __init__: inicializa el diccionario.

#CÓDIGO

class GestorPersonas:

    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        resultado = []

        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                resultado.append(nombre)

        return resultado

    def edad_promedio(self):
        return sum(self.personas.values()) / len(self.personas)


gp = GestorPersonas()
gp.agregar_persona("Ana", 28)
gp.agregar_persona("Bob", 17)
gp.agregar_persona("Carlos", 22)

print(gp.personas_mayores(18))
print(gp.edad_promedio())

#PRUEBA DE ESCRITORIO

#| Persona | Edad | ¿>=18? | Resultado |
#| Ana | 28 | Sí | ["Ana"] |
#| Bob | 17 | No | ["Ana"] |
#| Carlos | 22 | Sí | ["Ana","Carlos"] |

#Promedio = 22.33 aproximadamente.


#Ejercicio 8 ASIGNADOR DE EQUIPOS


#Entrada:
#Nombres de equipos y jugadores.

#Proceso:
#Crear cada equipo como una lista vacía dentro de un diccionario,
#agregar jugadores y comparar la cantidad de jugadores.

#Salida:
#Nombre del equipo con más integrantes.

#BOSQUEJO A MANO

#Equipos iniciales:
#{"A": [], "B": []}

#Agregar Juan a A:
#{"A":["Juan"], "B":[]}

#Agregar Pedro a A:
#{"A":["Juan","Pedro"], "B":[]}

#Agregar Luis a B:
#{"A":["Juan","Pedro"], "B":["Luis"]}

#A tiene 2 jugadores.
#B tiene 1.
#Mayor: A.

#DESCUBRIR EL PATRÓN

#1. crear_equipo(): crea clave con lista vacía.
#2. agregar_jugador(): usa append() sobre la lista del equipo.
#3. equipo_mayor_integrantes(): recorre el diccionario y compara len().
#4. equipos: diccionario de listas.
#5. __init__: inicializa el diccionario.

#CÓDIGO

class Equipos:

    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        mayor = None
        cantidad_mayor = 0

        for equipo, jugadores in self.equipos.items():
            if len(jugadores) > cantidad_mayor:
                cantidad_mayor = len(jugadores)
                mayor = equipo

        return mayor


eq = Equipos()
eq.crear_equipo("A")
eq.crear_equipo("B")
eq.agregar_jugador("A", "Juan")
eq.agregar_jugador("A", "Pedro")
eq.agregar_jugador("B", "Luis")

print(eq.equipo_mayor_integrantes())

#PRUEBA DE ESCRITORIO

#| Acción | A | B | Mayor |
#| crear equipos | [] | [] | — |
#| Juan → A | [Juan] | [] | A |
#| Pedro → A | [Juan,Pedro] | [] | A |
#| Luis → B | [Juan,Pedro] | [Luis] | A |

#Salida: A.


#Ejercicio 9 VALIDADOR DE CARACTERES


#Entrada:
#Textos para analizar.

#Proceso:
#Recorrer cada carácter y clasificarlo como vocal, consonante o dígito.
#Guardar además el texto más largo analizado.

#Salida:
#Diccionario con los conteos.

#BOSQUEJO A MANO

#Texto:
#"Hola123"

#H → consonante
#o → vocal
#l → consonante
#a → vocal
#1 → dígito
#2 → dígito
#3 → dígito

#Conteos:
#vocales = 2
#consonantes = 2
#digitos = 3

#Texto más largo:
#"Hola123"

#DESCUBRIR EL PATRÓN

#1. solo_vocales(letra): comprueba si la letra está en "aeiouAEIOU".
#2. contar_por_tipo(texto): recorre carácter a carácter y clasifica.
#3. texto_mas_largo: atributo que conserva el texto más largo.
#4. conteos: diccionario con vocales, consonantes y dígitos.
#5. __init__: inicializa el historial y texto más largo.

#CÓDIGO

class AnalizadorString:

    def __init__(self):
        self.texto_mas_largo = ""
        self.conteos = {
            "vocales": 0,
            "consonantes": 0,
            "digitos": 0
        }

    def solo_vocales(self, letra):
        return letra.lower() in "aeiou"

    def contar_por_tipo(self, texto):
        conteos = {
            "vocales": 0,
            "consonantes": 0,
            "digitos": 0
        }

        for letra in texto:
            if letra.isdigit():
                conteos["digitos"] += 1
            elif letra.isalpha():
                if self.solo_vocales(letra):
                    conteos["vocales"] += 1
                else:
                    conteos["consonantes"] += 1

        self.conteos = conteos

        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        return conteos


astr = AnalizadorString()
print(astr.contar_por_tipo("Hola123"))

#PRUEBA DE ESCRITORIO

#| Carácter | Tipo | Vocales | Consonantes | Dígitos |
#| H | consonante | 0 | 1 | 0 |
#| o | vocal | 1 | 1 | 0 |
#| l | consonante | 1 | 2 | 0 |
#| a | vocal | 2 | 2 | 0 |
#| 1 | dígito | 2 | 2 | 1 |
#| 2 | dígito | 2 | 2 | 2 |
#| 3 | dígito | 2 | 2 | 3 |

#Salida:
#{'vocales': 2, 'consonantes': 2, 'digitos': 3}


#Ejercicio 10 GESTOR DE TAREAS CON PRIORIDAD


#Entrada:
#Descripciones y prioridades.

#Proceso:
#Guardar cada tarea como tupla (descripción, prioridad), filtrar
#las de prioridad "alta" y eliminar una tarea por descripción.

#Salida:
#Lista de tareas prioritarias.

#BOSQUEJO A MANO

#Tareas:
#("Estudiar","alta")
#("Leer","baja")
#("Tarea","alta")

#Lista:
#[("Estudiar","alta"), ("Leer","baja"), ("Tarea","alta")]

#Prioritarias:
#[("Estudiar","alta"), ("Tarea","alta")]

#Eliminar "Estudiar":
#[("Leer","baja"), ("Tarea","alta")]

#DESCUBRIR EL PATRÓN

#1. agregar_tarea(): crea una tupla y la agrega a la lista.
#2. tareas_prioritarias(): filtra por prioridad "alta".
#3. eliminar_completada(): recorre y elimina la tarea cuya descripción coincide.
#4. tareas: lista de tuplas.
#5. __init__: inicializa la lista.

#CÓDIGO

class Tareas:

    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        self.tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        resultado = []

        for tarea in self.tareas:
            if tarea[1] == "alta":
                resultado.append(tarea)

        return resultado

    def eliminar_completada(self, descripcion):
        for tarea in self.tareas:
            if tarea[0] == descripcion:
                self.tareas.remove(tarea)
                return True

        return False


t = Tareas()
t.agregar_tarea("Estudiar", "alta")
t.agregar_tarea("Leer", "baja")
t.agregar_tarea("Tarea", "alta")

print(t.tareas_prioritarias())
t.eliminar_completada("Estudiar")
print(t.tareas)

#PRUEBA DE ESCRITORIO

#| Acción | Lista de tareas | Salida |
#| agregar Estudiar | [("Estudiar","alta")] | — |
#| agregar Leer | +("Leer","baja") | — |
#| agregar Tarea | +("Tarea","alta") | — |
#| tareas_prioritarias() | misma | [("Estudiar","alta"),("Tarea","alta")] |
#| eliminar Estudiar | [("Leer","baja"),("Tarea","alta")] | True |


#Ejercicio 11 CONTADOR DE FRECUENCIA


#Entrada:
#Elementos individuales o en lote.

#Proceso:
#Usar un diccionario donde cada elemento sea una clave y su valor
#sea la cantidad de veces que aparece. Encontrar el máximo.

#Salida:
#Elemento más frecuente y frecuencia de un elemento.

#BOSQUEJO A MANO

#Elementos:
#a, b, a, c, a, b

#Inicial:
#{}

#a → {"a":1}
#b → {"a":1,"b":1}
#a → {"a":2,"b":1}
#c → {"a":2,"b":1,"c":1}
#a → {"a":3,"b":1,"c":1}
#b → {"a":3,"b":2,"c":1}

#Más frecuente:
#"a" con 3.

#DESCUBRIR EL PATRÓN

#1. agregar_elemento(): aumenta el contador.
#2. elemento_mas_frecuente(): recorre items() y guarda el mayor.
#3. frecuencia_elemento(): devuelve el valor de una clave o 0 si no existe.
#4. frecuencias: diccionario contador.
#5. __init__: inicializa el diccionario.

#CÓDIGO

class ContadorFrecuencia:

    def __init__(self):
        self.frecuencias = {}

    def agregar_elemento(self, elemento):
        if elemento in self.frecuencias:
            self.frecuencias[elemento] += 1
        else:
            self.frecuencias[elemento] = 1

    def elemento_mas_frecuente(self):
        mayor = None
        frecuencia = 0

        for elemento, cantidad in self.frecuencias.items():
            if cantidad > frecuencia:
                frecuencia = cantidad
                mayor = elemento

        return mayor

    def frecuencia_elemento(self, elemento):
        return self.frecuencias.get(elemento, 0)


cf = ContadorFrecuencia()
cf.agregar_elemento("a")
cf.agregar_elemento("b")
cf.agregar_elemento("a")
cf.agregar_elemento("c")
cf.agregar_elemento("a")

print(cf.elemento_mas_frecuente())
print(cf.frecuencia_elemento("a"))

#PRUEBA DE ESCRITORIO

#| Elemento | Diccionario |
#| a | {"a":1} |
#| b | {"a":1,"b":1} |
#| a | {"a":2,"b":1} |
#| c | {"a":2,"b":1,"c":1} |
#| a | {"a":3,"b":1,"c":1} |

#Salida:
#"a"
#3


#Ejercicio 12 SELECTOR DE RANGO CON TUPLAS


#Entrada:
#Pares (inicio, fin) para varios rangos.

#Proceso:
#Crear una tupla con los números del rango y combinar varios rangos
#en un conjunto para eliminar duplicados.

#Salida:
#Lista de elementos únicos.

#BOSQUEJO A MANO

#Rango (1,3):
#[1,2,3]

#Rango (2,4):
#[2,3,4]

#Unimos:
#1,2,3,2,3,4

#Conjunto:
#{1,2,3,4}

#Lista final:
#[1,2,3,4]

#DESCUBRIR EL PATRÓN

#1. crear_rango(): genera una tupla con números de inicio a fin.
#2. elementos_en_multiples_rangos(*rangos): recorre las tuplas,
#   reutiliza crear_rango() y usa un conjunto.
#3. conjunto: elimina duplicados.
#4. __init__: no necesita estado permanente.

#CÓDIGO

class SelectorRango:

    def __init__(self):
        pass

    def crear_rango(self, inicio, fin):
        resultado = []

        for numero in range(inicio, fin + 1):
            resultado.append(numero)

        return tuple(resultado)

    def elementos_en_multiples_rangos(self, *rangos):
        unicos = set()

        for rango in rangos:
            inicio, fin = rango
            valores = self.crear_rango(inicio, fin)

            for numero in valores:
                unicos.add(numero)

        return sorted(unicos)


sr = SelectorRango()
print(sr.elementos_en_multiples_rangos((1,3), (2,4)))

#PRUEBA DE ESCRITORIO

#| Rango | Valores | Conjunto |
#| (1,3) | (1,2,3) | {1,2,3} |
#| (2,4) | (2,3,4) | {1,2,3,4} |

#Salida:
#[1,2,3,4]


#Ejercicio 13 COMBINADOR DE LISTAS


#Entrada:
#Dos o más listas.

#Proceso:
#Intercalar elementos usando índices y bucles. Para varias listas,
#reutilizar intercalar().

#Salida:
#Lista intercalada.

#BOSQUEJO A MANO

#Lista 1:
#[1,2]

#Lista 2:
#[3,4]

#Tomar 1 → [1]
#Tomar 3 → [1,3]
#Tomar 2 → [1,3,2]
#Tomar 4 → [1,3,2,4]

#Resultado:
#[1,3,2,4]

#DESCUBRIR EL PATRÓN

#1. intercalar(lista1, lista2): toma alternativamente un elemento de cada lista.
#2. intercalar_multiples(*listas): combina varias listas reutilizando intercalar().
#3. resultado: lista final.
#4. __init__: no necesita atributos.

#CÓDIGO

class CombinadorListas:

    def __init__(self):
        pass

    def intercalar(self, lista1, lista2):
        resultado = []
        limite = max(len(lista1), len(lista2))

        for i in range(limite):
            if i < len(lista1):
                resultado.append(lista1[i])

            if i < len(lista2):
                resultado.append(lista2[i])

        return resultado

    def intercalar_multiples(self, *listas):
        if len(listas) == 0:
            return []

        resultado = listas[0]

        for i in range(1, len(listas)):
            resultado = self.intercalar(resultado, listas[i])

        return resultado


cl = CombinadorListas()
print(cl.intercalar([1,2], [3,4]))
print(cl.intercalar_multiples([1,2], [3,4], [5,6]))

#PRUEBA DE ESCRITORIO

#| i | lista1[i] | lista2[i] | Resultado |
#| 0 | 1 | 3 | [1,3] |
#| 1 | 2 | 4 | [1,3,2,4] |

#Salida:
#[1,3,2,4]


#Ejercicio 14 MAPEO DE ESTUDIANTES A NOTAS


#Entrada:
#Estudiante → nota.

#Proceso:
#Guardar en diccionario, filtrar aprobados y comparar notas para
#encontrar la mayor.

#Salida:
#Lista de aprobados y tupla (nombre, nota) del mejor estudiante.

#BOSQUEJO A MANO

#Ana → 95
#Bob → 70
#Carlos → 88

#Aprobados con mínimo 70:
#Ana, Bob, Carlos

#Mayor:
#Ana → 95

#Resultado:
#("Ana",95)

#DESCUBRIR EL PATRÓN

#1. registrar(): guarda estudiante → nota.
#2. estudiantes_aprobados(): recorre items() y filtra.
#3. mejor_estudiante(): compara notas y guarda nombre y nota mayor.
#4. notas: diccionario.
#5. __init__: inicializa.

#CÓDIGO

class RegistroNotas:

    def __init__(self):
        self.notas = {}

    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        resultado = []

        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                resultado.append(estudiante)

        return resultado

    def mejor_estudiante(self):
        mejor = None
        mejor_nota = None

        for estudiante, nota in self.notas.items():
            if mejor_nota is None or nota > mejor_nota:
                mejor_nota = nota
                mejor = estudiante

        return (mejor, mejor_nota)


rn = RegistroNotas()
rn.registrar("Ana", 95)
rn.registrar("Bob", 70)
rn.registrar("Carlos", 88)

print(rn.estudiantes_aprobados(70))
print(rn.mejor_estudiante())

#PRUEBA DE ESCRITORIO

#| Estudiante | Nota | Mejor hasta ahora |
#| Ana | 95 | ("Ana",95) |
#| Bob | 70 | ("Ana",95) |
#| Carlos | 88 | ("Ana",95) |


#Ejercicio 15 DIVISORES DE UN NÚMERO


#Entrada:
#Uno o varios números.

#Proceso:
#Probar divisiones desde 1 hasta el número y guardar los divisores.
#Para saber si es perfecto, sumar sus divisores excepto él mismo.

#Salida:
#Tupla de divisores, booleano y diccionario para múltiples números.

#BOSQUEJO A MANO

#Número:
#12

#Probar:
#12 % 1 = 0 → divisor
#12 % 2 = 0 → divisor
#12 % 3 = 0 → divisor
#12 % 4 = 0 → divisor
#12 % 5 ≠ 0
#12 % 6 = 0 → divisor
#12 % 7 ≠ 0
#...
#12 % 12 = 0 → divisor

#Tupla:
#(1,2,3,4,6,12)

#Para perfecto:
#Divisores propios:
#1+2+3+4+6 = 16
#16 != 12 → no es perfecto.

#DESCUBRIR EL PATRÓN

#1. encontrar_divisores(): recorre de 1 a numero y agrega si el residuo es 0.
#2. es_perfecto(): reutiliza encontrar_divisores() y suma los divisores excepto el número.
#3. encontrar_multiples_divisores(*numeros): crea diccionario número → tupla.
#4. __init__: no necesita atributos.

#CÓDIGO

class DivisorFinder:

    def __init__(self):
        pass

    def encontrar_divisores(self, numero):
        divisores = []

        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)

        return tuple(divisores)

    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)
        suma = sum(divisores[:-1])
        return suma == numero

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}

        for numero in numeros:
            resultado[numero] = self.encontrar_divisores(numero)

        return resultado


df = DivisorFinder()
print(df.encontrar_divisores(12))
print(df.es_perfecto(12))
print(df.encontrar_multiples_divisores(6, 12))

#PRUEBA DE ESCRITORIO

#| i | 12 % i | Divisores |
#| 1 | 0 | [1] |
#| 2 | 0 | [1,2] |
#| 3 | 0 | [1,2,3] |
#| 4 | 0 | [1,2,3,4] |
#| 5 | ≠0 | [1,2,3,4] |
#| 6 | 0 | [1,2,3,4,6] |
#| 12 | 0 | [1,2,3,4,6,12] |


#Ejercicio 16 CODIFICADOR / DECODIFICADOR


#Entrada:
#Letra o palabra y desplazamiento de 1 a 25.

#Proceso:
#Convertir letras a posiciones del alfabeto, desplazar usando % y
#reconstruir el texto. Guardar cada codificación en un diccionario.

#Salida:
#Palabra codificada.

#BOSQUEJO A MANO

#Palabra:
#"hola"

#Desplazamiento:
#3

#h → k
#o → r
#l → o
#a → d

#Resultado:
#"krod"

#DESCUBRIR EL PATRÓN

#1. codificar_letra(): calcula la nueva posición usando ord(), % y chr().
#2. codificar_palabra(): recorre la palabra y reutiliza codificar_letra().
#3. historial: diccionario que guarda palabra original → codificada.
#4. __init__: inicializa historial.

#Conceptos:
#ord(), chr(), %, for, diccionario, listas, join(), lower().

#CÓDIGO

class CodificadorCesar:

    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        if not letra.isalpha():
            return letra

        base = ord('a')
        posicion = ord(letra.lower()) - base
        nueva_posicion = (posicion + desplazamiento) % 26

        return chr(base + nueva_posicion)

    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""

        for letra in palabra:
            resultado += self.codificar_letra(letra, desplazamiento)

        self.historial[palabra] = resultado

        return resultado


cc = CodificadorCesar()
print(cc.codificar_palabra("hola", 3))

#PRUEBA DE ESCRITORIO

#| Letra | Posición | +3 | Resultado |
#| h | 7 | 10 | k |
#| o | 14 | 17 | r |
#| l | 11 | 14 | o |
#| a | 0 | 3 | d |

#Salida correcta para César +3:
#"krod"


#Ejercicio 17 GRUPO DE EDADES


#Entrada:
#Edades en lote.

#Proceso:
#Clasificar cada edad con if/elif, agruparlas en listas dentro
#de un diccionario y calcular promedio de una categoría.

#Salida:
#Diccionario agrupado y promedio.

#BOSQUEJO A MANO

#5 → niño
#15 → adolescente
#30 → adulto
#70 → mayor

#Diccionario:
#{
# "niño":[5],
# "adolescente":[15],
# "adulto":[30],
# "mayor":[70]
#}

#Promedio de adulto:
#30.

#DESCUBRIR EL PATRÓN

#1. clasificar_edad(): devuelve una categoría según el rango.
#2. agrupar_por_categoria(*edades): reutiliza clasificar_edad()
#   y agrega la edad a la lista correspondiente.
#3. edad_promedio_categoria(): suma y divide por cantidad.
#4. grupos: diccionario de listas.
#5. __init__: inicializa las categorías.

#Rangos usados:
#niño: 0–11
#adolescente: 12–17
#adulto: 18–64
#mayor: 65 o más.

#CÓDIGO

class AgrupadorEdades:

    def __init__(self):
        self.grupos = {
            "niño": [],
            "adolescente": [],
            "adulto": [],
            "mayor": []
        }

    def clasificar_edad(self, edad):
        if edad <= 11:
            return "niño"
        elif edad <= 17:
            return "adolescente"
        elif edad <= 64:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        for edad in edades:
            categoria = self.clasificar_edad(edad)
            self.grupos[categoria].append(edad)

        return self.grupos

    def edad_promedio_categoria(self, categoria):
        edades = self.grupos[categoria]
        return sum(edades) / len(edades)


ae = AgrupadorEdades()
print(ae.agrupar_por_categoria(5, 15, 30, 70))
print(ae.edad_promedio_categoria("adulto"))

#PRUEBA DE ESCRITORIO

#| Edad | Categoría | Diccionario |
#| 5 | niño | niño:[5] |
#| 15 | adolescente | adolescente:[15] |
#| 30 | adulto | adulto:[30] |
#| 70 | mayor | mayor:[70] |


#Ejercicio 18 MATRIZ DE DISTANCIAS


#Entrada:
#Tuplas (x,y) como puntos.

#Proceso:
#Calcular distancia euclidiana, comparar para encontrar el punto
#más cercano y guardar todas las distancias calculadas en una lista.

#Salida:
#Distancia numérica y punto más cercano.

#BOSQUEJO A MANO

#Puntos:
#(0,0) y (3,4)

#Fórmula:
#sqrt((x2-x1)^2 + (y2-y1)^2)

#sqrt((3-0)^2 + (4-0)^2)
#= sqrt(9+16)
#= sqrt(25)
#= 5.0

#DESCUBRIR EL PATRÓN

#1. distancia_euclidiana(): aplica la fórmula y guarda la distancia.
#2. punto_mas_cercano(): calcula distancia a cada punto y conserva la menor.
#3. distancias: lista de resultados calculados.
#4. __init__: inicializa la lista.

#CÓDIGO

import math


class CalculadorDistancia:

    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]

        distancia = math.sqrt(dx ** 2 + dy ** 2)
        self.distancias.append(distancia)

        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        punto_cercano = None
        menor_distancia = None

        for punto in puntos:
            distancia = self.distancia_euclidiana(referencia, punto)

            if menor_distancia is None or distancia < menor_distancia:
                menor_distancia = distancia
                punto_cercano = punto

        return punto_cercano


cd = CalculadorDistancia()
print(cd.distancia_euclidiana((0,0), (3,4)))
print(cd.punto_mas_cercano((0,0), (3,4), (1,1), (5,5)))

#PRUEBA DE ESCRITORIO

#Para (0,0) → (3,4):
#dx=3, dy=4
#distancia=5.0

#Para puntos:
#(3,4) → 5.0
#(1,1) → 1.41 aprox.
#(5,5) → 7.07 aprox.

#Punto más cercano:
#(1,1)


#Ejercicio 19 INVENTARIO DE PRODUCTOS


#Entrada:
#Productos y cantidades.

#Proceso:
#Guardar o actualizar cantidades en un diccionario. Al restar,
#comprobar si existe suficiente stock. Filtrar productos bajo el mínimo.

#Salida:
#True/False y lista de productos bajo stock.

#BOSQUEJO A MANO

#Stock inicial:
#{}

#pan +50:
#{"pan":50}

#Restar 30:
#{"pan":20}
#Hay suficiente → True

#Buscar bajo 15:
#20 < 15 → No

#Si luego restamos 10:
#{"pan":10}
#10 < 15 → Sí

#Resultado:
#["pan"]

#DESCUBRIR EL PATRÓN

#1. agregar_stock(): suma cantidad al stock existente.
#2. restar_stock(): comprueba suficiencia, resta y retorna True/False.
#3. productos_bajo_stock(): recorre items() y filtra cantidades menores al mínimo.
#4. stock: diccionario producto → cantidad.
#5. __init__: inicializa el diccionario.

#CÓDIGO

class Inventario:

    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        if producto in self.stock:
            self.stock[producto] += cantidad
        else:
            self.stock[producto] = cantidad

    def restar_stock(self, producto, cantidad):
        if producto in self.stock and self.stock[producto] >= cantidad:
            self.stock[producto] -= cantidad
            return True

        return False

    def productos_bajo_stock(self, minimo):
        resultado = []

        for producto, cantidad in self.stock.items():
            if cantidad < minimo:
                resultado.append(producto)

        return resultado


inv = Inventario()
inv.agregar_stock("pan", 50)
print(inv.restar_stock("pan", 30))
print(inv.productos_bajo_stock(15))

#PRUEBA DE ESCRITORIO

#| Acción | Stock | Salida |
#| agregar pan 50 | {"pan":50} | — |
#| restar pan 30 | {"pan":20} | True |
#| bajo stock <15 | {"pan":20} | [] |

#NOTA:
#Con exactamente el ejemplo del enunciado, la salida de productos_bajo_stock(15)
#es [] porque quedan 20 unidades. Para obtener ["pan"] habría que dejar menos
#de 15 unidades, por ejemplo restar 40 y quedar en 10.


#Ejercicio 20 ANALIZADOR DE PATRONES EN TEXTOS


#Entrada:
#Texto y patrón de búsqueda.

#Proceso:
#Separar el texto en palabras, buscar las que comiencen con el patrón,
#agrupar palabras por longitud y obtener palabras únicas con un conjunto.

#Salida:
#Lista de coincidencias, diccionario por longitud y conjunto de únicas.

#BOSQUEJO A MANO

#Texto:
#"el gato está aquí"

#split():
#["el", "gato", "está", "aquí"]

#Patrón "ga":
#"el" → no
#"gato" → sí

#Resultado encontrar_palabras:
#["gato"]

#Agrupar por longitud:
#"el" → 2
#"gato" → 4
#"está" → 4
#"aquí" → 4

#Resultado:
#{
#  2: ["el"],
#  4: ["gato", "está", "aquí"]
#}

#Palabras únicas:
#{"el", "gato", "está", "aquí"}

#DESCUBRIR EL PATRÓN

#1. encontrar_palabras(): usa split() y startswith() para filtrar.
#2. agrupar_por_longitud(): usa split(), len() y un diccionario de listas.
#3. palabras_unicas(): usa un conjunto para eliminar duplicados.
#4. __init__: puede mantener el último texto analizado.

#CÓDIGO

class AnalizadorPatrones:

    def __init__(self):
        self.texto = ""

    def encontrar_palabras(self, texto, patron):
        palabras = texto.split()
        resultado = []

        for palabra in palabras:
            if palabra.startswith(patron):
                resultado.append(palabra)

        self.texto = texto
        return resultado

    def agrupar_por_longitud(self, texto):
        grupos = {}

        for palabra in texto.split():
            longitud = len(palabra)

            if longitud not in grupos:
                grupos[longitud] = []

            grupos[longitud].append(palabra)

        self.texto = texto
        return grupos

    def palabras_unicas(self):
        return set(self.texto.split())


ap = AnalizadorPatrones()

print(ap.encontrar_palabras("el gato está aquí", "ga"))
print(ap.agrupar_por_longitud("el gato está aquí"))
print(ap.palabras_unicas())

#PRUEBA DE ESCRITORIO

#| Palabra | Longitud | Grupo |
#| el | 2 | {2:["el"]} |
#| gato | 4 | {2:["el"],4:["gato"]} |
#| está | 4 | {2:["el"],4:["gato","está"]} |
#| aquí | 4 | {2:["el"],4:["gato","está","aquí"]} |

#Conjunto final:
#{"el","gato","está","aquí"}