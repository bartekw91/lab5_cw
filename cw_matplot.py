import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Dokumentacja Matplotlib: matplotlib.org

# plt.plot([1, 2, 3, 4])
# plt.ylabel('Liczby')
# plt.show()

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro-')  # [Pozycja osi X[, [Poz osi Y], '<kol><punkt><styl lini>'
# plt.axis((0, 6, 0, 20))  # Ograniczenie linii ((<pocz X, kon X, pocz Y, kon Y))
# plt.show()
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r')
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'o')
# # plt.axis((0, 6, 0, 20))
# # Alternatywy do plt.axis():
# plt.xlim(0, 6)
# plt.ylim(0, 20)
# # Koniec alternatywy do plt.axis():
# plt.show()

# TWORZENIE PROSTEGO WYKRESU Z ZAPISYWANIEM JAKO OBRAZ #
# x = np.linspace(0, 2, 100)
# plt.plot(x, x, label='liniowa')
# plt.plot(x, x**2, label='kwadratowa')
# plt.plot(x, x**3, label='sześcienna')
# plt.xlabel('Etykieta X')
# plt.ylabel('Etykieta Y')
# plt.title('Prosty wykres')
# plt.legend()
# plt.savefig('wykres_z_matplot.png')
# plt.show()
# im1 = Image.open('wykres_z_matplot.png')
# im1 = im1.convert('RGB')
# im1.save('nowy.jpg')

# PRZYKŁADOWY WYKRES Z SINUS #
# x = np.arange(0, 10.1, 0.1)
# s = np.sin(x)
# plt.plot(x, s, label='sin(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('Wykres Sinus(x)')
# plt.legend()
# plt.show()

# WYKRES Z DANYMI ZE SŁOWNIKA #

# dane = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# dane['b'] = dane['a'] + 10 * np.random.randn(50)
# dane['d'] = np.abs(dane['d']) * 100
# print(f'a={dane['a'][0]}, b={dane['b'][0]}, c={dane['c'][0]}, d={dane['d'][0]}')
# plt.scatter('a', 'b', c='c', cmap='magma', s='d', data=dane)
# plt.xlabel('Wartość A')
# plt.ylabel('Wartość B')
# plt.show()


x1 = np.arange(0, 2, 0.02)
x2 = np.arange(0, 2, 0.02)
