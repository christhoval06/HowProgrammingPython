# Tipos de datos

# camelCase o loweCamelcase
# UpperCamelCase
# kebab-case
# snake_case OK por python

# 1. Enteros


from cmath import sqrt
from decimal import Decimal


edad: int = 32 # decimal
base_binaria: int = 0b01
base_octal: int = 0o7
base_hexadecimal: int = 0xA

suma = 0o13 + 0o34 
print('suma', suma)

print(5/2)

# Flotante

precio: float = 4.99
print(5/2.2)

valor: Decimal = Decimal(1024.99)

print('valor', valor)

# Strings - Cadenas

nombre: str = 'Christhoval'
celular: str = '+507 64325621'

# apellido: str = input('Apellido: ')
apellido: str = 'Barba R'

# print('apellido= ', apellido)

print('-' * 100 )


print(nombre + ' ' + apellido)
print('%s %s = %i' % (nombre, apellido, edad))
print('{} {} = {}'.format(nombre, apellido, edad))
print('{name} {last_name} = 0x{age:x}'.format(name=nombre, last_name=apellido, age=edad))

print(f'{nombre} {apellido} = 0x{edad:x}')

print(f'La suma de {45} + {54} es igual a {45 + 54}')


plantilla: str = '''
I am the $master of my fate,
I am the $captain of my soul.
'''

print(plantilla)

from string import Template

print(Template(plantilla).substitute(master='captain', captain='master'))

usuario = 'Pepito Perez'

print('esPerez', 'perez' in usuario.lower())
print('noEsPerez', 'perez' not in 'Juan Diaz'.lower())

print(str(34567890 + 30))

print(usuario[0], usuario[7])
print(len(usuario))
print(usuario[len(usuario) - 1])
print(usuario[-1], usuario[-12])
print(usuario[0:6], usuario[7:12])

palindromo = 'reconocer'
print(palindromo, palindromo[::-1], palindromo == palindromo[::-1])

# metodos de cadenas
s = 'FoO BaR BAZ quX'
print('capitalize', s.capitalize())
print('lower', s.lower())
print('swapcase', s.swapcase())
print('title', s.title())
print('upper', s.upper())
print('count(B)', s.count('B'))
print('find(BAZ)', s.find('BAZ'))
print('isalnum', s.isalnum())
print('isalnum', 'asd124'.isalnum())
print('isalpha', s.isalpha())
print('isalpha', nombre.isalpha())
print('isdigit', '12343'.isdigit())
print('islower', nombre.islower())
print('isspace', s.isspace())
print('isspace', '        '.isspace())

print('center', s.center(50, '-'))
print('ljust', s.ljust(50, '-'))
print('rjust', s.rjust(50, '-'))


# Booleanos

cierto: bool = True
falso: bool = False

print(0 == False)
print(1 == True)