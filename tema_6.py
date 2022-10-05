from typing import Union
from math import pow
from json_data import users

# Diccionarios
nombre: str = "Christhoval"
apellido: str = "Barba"
edad: int = 33
job: str = "Tech Lead"
salary: float = 2345.90
languages: list[str] = ["python", "ts", "js", 'rust', 'go']

usuario_christhoval: dict[str, Union[str, int, float, list[str]]] = {
    "nombre": nombre,
    "apellido": apellido,
    "edad": edad,
    "job": job,
    "salary": salary,
    "languages": languages
}
print('usuario_christhoval', nombre)

usuarios = {
    "christhoval": usuario_christhoval,
    "nombre": nombre,
    "apellido": apellido,
    "edad": edad,
    "job": job,
    "salary": salary,
    "languages": languages,
    "pow": pow,
    "users": users,
}

print('usuarios', usuarios)

# Obtener un valor
nombre = usuarios.get('nombre', 'Edgar')
print('nombre', nombre)

ciudad = usuarios.get('ciudad', 'David')
print('ciudad', ciudad)

direccion = usuarios.get('direccion', 'Panama')
print('direccion', direccion)

# Obtener valor de un diccionario anidado
nombre = usuarios.get('fernando', {}).get('nombre')
print('nombre', nombre)
# Sugerido dos niveles de profundidad(deep).

print('type', type(usuarios))

# así NO: posible crash si la llave no existe.
nombre = usuarios['nombre'] or 'Panama'
print('nombre', nombre)

tienda = {
    0: 'Galletas',
    1: 'Pan',
    2: 'Tomate'
}

print('tienda[1]', tienda[1])

# Los diccionarios son dinamicos
tienda['papa'] = '🥔'
tienda['batata'] = '🍠'
tienda['guineo'] = '🍌'
tienda['manzanas'] = '🍎'

print('tienda', tienda)

tienda['manzanas'] = {'rojas': '🍎', 'verde': '🍏'}

print('tienda', tienda)
print('manzanas->verde', tienda['manzanas']['verde'])
print('manzanas->verde', tienda.get('manzanas').get('verde'))
# si no existe
panes = {'pan': '🍞', 'croissant': '🥐', 'flauta': '🥖'}
print('panes->flauta', tienda.get('panes', panes).get('flauta'))
print('panes->bolita', tienda.get('panes', panes).get('bolita', '🥨'))

tienda['panes'] = panes
# tienda = {
#     **tienda,
#     'panes': panes
# }
print('tienda', tienda)

tienda.update(penino='🥒', cebolla='🧅')
print('tienda', tienda)

tienda.update({
    'mani': '🥜',
    'queso': '🧀',
    'filete': '🥩'
})
print('tienda', tienda)

print('tienda.items', list(tienda.items()))
print('tienda.keys', list(tienda.keys()))

print('hay cebolla?', 'cebolla' in list(tienda.keys()))
print('hay cebolla?', 'cebolla' in tienda)
print('hay camarones?', 'camarones' in list(tienda.keys()))

print('hay hongos?', 'hongos' in tienda)

print('tienda.values', list(tienda.values()))
print('hay 🧅?', '🧅' in tienda)
print('hay 🧅?', '🧅' in list(tienda.values()))

# Borrar elemento
del tienda[0]
print('tienda', tienda)

del tienda['cebolla']
print('tienda', tienda)

print('borrar -> cebolla', tienda.pop('cebolla', 'No hay cebolla!!!'))
print('tienda', tienda)

print('borrar -> mani', tienda.pop('mani', 'No hay mani!!!'))
print('tienda', tienda)

print('borrar -> ultimo', tienda.popitem())
print('tienda', tienda)
print('borrar -> ultimo', tienda.popitem())
print('tienda', tienda)

# print('borrar -> ultimo', {}.popitem())  # Crash
tienda2 = tienda.copy()
# tienda2 = {**tienda}

tienda2.update(tamales='🫔')
print('tienda', tienda)
print('tienda2', tienda2)

# Set
d = {1, 2, 3, '4', 6, 'a'}
print('type', type(d))

deudores = {'aa', 'ac', 'hy'}
prestamos = {'aa', 'ab', 'ac', 'ad'}

banco = deudores | prestamos
# banco = deudores.union(prestamos)
print('type', type(banco), list(banco))
print('ea' in banco)

print('no deudores', prestamos.difference(deudores))

print('deudores', prestamos.intersection(deudores))
print('symmetric_difference', prestamos.symmetric_difference(deudores))
print('isdisjoint', deudores.isdisjoint(prestamos))

d = banco | {5, 7, 10, 99}
print('d', d)
