import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Dokumentacja Matplotlib: matplotlib.org
# WYKONANIE WKRESU I ODZWIERCIEDLANIE na kol

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
# plt.legend(labels='liniowa', 'kwadratowa')
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

# TWORZENIE DWÓCH WYKRESÓW OBOK SIEBIE #
# x1 = np.arange(0, 2, 0.02)
# x2 = np.arange(0, 2, 0.02)
# y1 = np.sin(2 * np.pi * x1)
# y2 = np.cos(2 * np.pi * x1)
# plt.subplot(2, 1, 1)
# plt.plot(x1, y1, '-')
# plt.title('Wykres Sin(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
#
# plt.subplot(2, 1, 2)
# plt.plot(x2, y2, 'r-')
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.title('Wykres Cos(x)')
# plt.subplots_adjust(hspace=0.5)  # hspace,wspace,left,right,top,bottom - Odstępy
# # Wartośc right ma być wiekszy od left
# plt.show()


# Multi wykresy #

# x1 = np.arange(0.0, 2.0, 0.02)
# x2 = np.arange(0.0, 2.0, 0.02)
# y1 = np.sin(2 * np.pi * x1)
# y2 = np.cos(2 * np.pi * x1)
# fig, axs = plt.subplots(3, 2)
# axs[0, 0].plot(x1, y1, '-')
# axs[0, 0].set_title('Wykres sin(X)')
# axs[0, 0].set_xlabel('x')
# axs[0, 0].set_ylabel('Sin(x)')
# axs[1, 1].plot(x2, y2, 'r-')
# axs[1, 1].set_title('Wykres cos(X)')
# axs[1, 1].set_xlabel('x')
# axs[1, 1].set_ylabel('Cos(x)')
# axs[2, 0].plot(x2, y2, 'r-')
# axs[2, 0].set_title('Wykres cos(X)')
# axs[2, 0].set_xlabel('x')
# axs[2, 0].set_ylabel('Cos(x)')
# fig.delaxes(axs[0, 1])
# fig.delaxes(axs[1, 0])
# fig.delaxes(axs[2, 1])
# plt.subplots_adjust(hspace=0.5, wspace=0.5)
# plt.show()

# WYKRES SŁUPKOWY Z DANYMI #

# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Braslia', 'Warszawa'],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
#         'Populacja': [11190846, 1303171035, 207847528, 38675467]}
# df = pd.DataFrame(data)
# print(df)
# grupa = df.groupby('Kontynent')
# etykiety = np.array(list(grupa.groups.keys()))
# wartosci = list(grupa.agg('Populacja').sum())
# fig, ax = plt.subplots(figsize=(8, 8))
# ax.bar(x=etykiety, height=wartosci, color=['yellow', 'green', 'red'])
# ax.set_xlabel('Kontynenty')
# ax.set_ylabel('Populacja w mld')
# ax.ticklabel_format(axis='y', style='plain')
# fig.subplots_adjust(left=0.2)
# plt.show()

# WYKRES KOŁOWY #
df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
print(df)
seria = df.groupby('Imię i nazwisko')['Wartość zamówienia'].sum()
wedges, texts, autotext = plt.pie(x=seria, labels=seria.index,
                                  autopct=lambda pct: '{:.1f}%'.format(pct),
                                  textprops=dict(color='black'),
                                  colors=['red', 'green'])
plt.title('Suma zamówien dla sprzedawców')
plt.legend(loc='lower right')
plt.ylabel('Procentowy wynik wartości zamówienia')
plt.show()
