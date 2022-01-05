"""
Programa que calcula a norma de um vetor v com n coordenadas.
"""

from sys import path
path.insert(1, '../')
from vectors import *
from beauty_prints import beauty_root

def main():
    vector = get_vector()
    
    norm, sum_squares = calculate_norm(vector)

    # Se a norma for um quadrado perfeito, então ela é um inteiro, então é impressa.
    if int(norm) == norm:
        print("\nA norma do vetor é: {}".format(int(norm)))
    # Se não for um quadrado perfeito, então é impressa a apenas a soma dos quadrados com o simbolo de raiz.
    else:
        print("\nA norma do vetor é: {}".format(beauty_root(sum_squares)))

if __name__ == '__main__':
    main()