import numpy as np
import matplotlib.pyplot as plt
import random, json, os

def Funkcja1():
    r1 = random.randrange(1, 11)
    r2 = random.randrange(1,11)
    d = random.randrange(1, 11)
    t = np.linspace(0., 2*np.pi*(np.lcm(r1, r2)/r2), num=1000)
    xt = (r2 - r1)*np.cos(t) + d*np.cos(((r2-r1)/r1)*t)
    yt = (r2 - r1)*np.sin(t) - d*np.sin(((r2-r1)/r1)*t)
    wykres = plt.figure(figsize=(10, 10))
    plt.plot(xt, yt, 'b')
    plt.grid()
    plt.title(f"r1={r1}, r2={r2}, d={d}")
    plt.show()

def Funkcja2(sciezka):
    if os.path.exists(os.path.abspath(sciezka)) == False:
        raise FileExistsError("Nie znaleziono pliku!")

    with open(sciezka) as file:
        dane = json.load(file)
        t = np.linspace(0., 1., num=100)
        wykres = plt.figure(figsize=(10, 10))

        for i in range(len(dane)):
            slownik = dane[i]
            x1 = slownik["p1"][0]
            y1 = slownik["p1"][1]
            x2 = slownik['p2'][0]
            y2 = slownik['p2'][1]
            x3 = slownik['p3'][0]
            y3 = slownik['p3'][1]
            kolor = slownik['color']

            xt = (1-t)**2*x1 + 2*t*(1-t)*x2 + t**2*x3
            yt = (1-t)**2*y1 + 2*t*(1-t)*y2 + t**2*y3

            plt.plot(xt, yt, color=kolor)
            plt.scatter([x1, x2, x3], [y1, y2, y3])
            plt.xlabel('x(t)')
            plt.ylabel('y(t)')

        plt.grid()
        plt.show()
