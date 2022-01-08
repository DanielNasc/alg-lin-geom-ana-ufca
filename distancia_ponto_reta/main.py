from sys import path, exit
path.insert(1, '../')
from vectors import *
from utils import reta_ou_plano

"""
    A distância de um ponto P(x0, y0) a uma reta ax + by + c = 0 é dada por:
    d = |ax0 + by0 + c| / sqrt(a^2 + b^2)
    e a distância de um ponto P(x0, y0, z0) a uma reta ax + by + cz + d = 0 é dada por:
    d = |ax0 + by0 + cz0 + d| / sqrt(a^2 + b^2 + c^2)
"""

def main():
    qtd_c = reta_ou_plano()

    P = get_ponto('P', qtd_c)

    print()
    coeficientes = []
    for i in range(qtd_c + 1):
        coeficientes.append(get_float('Coeficiente {}: '.format(chr(i + 97))))
    
    distancia = distancia_ponto_reta_ou_plano(P, coeficientes)
    print("\nA distância de P {} é: {}".
                        format("à reta" if qtd_c == 2 else "ao plano", 
                                distancia[0] if distancia[0] == int(distancia[0]) else distancia[1]))

if __name__ == '__main__':
    main()