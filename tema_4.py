# 3. Variables y Operadores

import math


objetos: int = 3
nuevos_objetos: int = objetos + 4

id(objetos)
id(nuevos_objetos)

# 4. Listas y Tuplas

lista: list[str] = ['Fernado', 'Edgar', 'Angel', 'Christhoval']
print('lista', lista)
print('lista[2]', lista[2])

nombres: list[str] = ['Fernado', 'Edgar', 'Angel', 'Christhoval']
nombres2: list[str] = ['Edgar', 'Angel', 'Christhoval', 'Fernado']
print('id(lista)', id(lista))
print('id(nombres)', id(nombres))
print(lista == nombres)

print(lista == nombres2)

print(['i', 'o'] == 'i o'.split(' '))
a = [False, 'Hola', 2, 4.56, [1,2,3,[1,2,3,[1,2,3,[1,2,3,4]]]]]

print('a', a)

a = [int, len, math]
print('a', a)

# range
a = range(0, 10)
print('a', a)

print('lista[-1]', lista[-1])
print('lista[1:3]', lista[1:3])
lista.reverse()
print('reverse', lista)
lista.reverse()
print('reverse', lista)

from random import choice
print('choice', choice(lista))

vocales = ['a', 'e', 'i', 'o', 'u']
print('in', 'c'.lower() not in vocales)

print(vocales + lista)
print(vocales * 2)

print('len', len(vocales))
print('min', min(vocales))
print('max', max(vocales))

print('len', len(nombres))
print('min', min(nombres))
print('max', max(nombres))
print('[::-1]', nombres[::-1])

# Nested List
a = [[1,2,3,[1,2,3,[1,2,3,[1,2,3,4]]]]]

print(a[0][3][3][2])
print((((a[0])[3])[3])[2])


print(nombres[0])
# nombres[0] += ' K.'
nombres[0] = nombres[0] + ' K.'

print(nombres[0])
nombres[3] += ' B.'
print(nombres)
nombres[1:3] = ['Edgar J.', 'Angel G.']

print(nombres)

nombres[1:3] = ['Edgar J.']

print(nombres)

nombres[1:2] = ['Edgar J.', 'Angel G.', 'Juan D.']

nombres = ['Dalila R.'] + nombres + ['Maria G.']
print(nombres)

nombres.append('Luisa K.')
print(nombres)

n = nombres
nombres.pop()
nombres.pop()
del nombres[0:2]
print('nombres', nombres)
print('n', n)

nombres.insert(2, 'Rosa F.')

print('nombres', nombres)

nombres.remove('Juan D.')
print('nombres', nombres)

(usuario1, *usuarios) = nombres
print('usuario1', usuario1)
print('usuarios', usuarios)

# Tuplas

t = (1, 2, 3)
# t[0] = 10

tt = 1, 2, 3
print('t == tt', t == tt)

print('type(t)', type(t))
print('type(tt)', type(tt))

print('type((2))', type((2)))

[valor1, *valores] = tt
(valor1, *valores) = tt
valor1, *valores = tt
print('valor1', valor1)
print('valores', valores)

(lat, lon), (lat2, lon2) = (34.908, 67.890), (90.432, 12.3243)
# Magic time!
print('lat', lat)
print('lon', lon)

d = math.sqrt( math.pow(lat2 - lat, 2) + math.pow(lon2 - lon, 2) )
print('d(A, B)', d)
