"""
Programa que calcula a norma de um vetor v com n coordenadas.
Não é um programa complexo, e as funções são muito simples.
Então não é necessário muitos comentários.
"""

def main():
    vector = get_vector()
    sum_squares = 0
    for i in range(len(vector)):
        sum_squares += vector[i]**2
    norma = sum_squares**(1/2)

    # Se a norma for um quadrado perfeito, então ela é um inteiro, então é impressa.
    if int(norma) == norma:
        print("\nA norma do vetor é: {}".format(int(norma)))
    # Se não for um quadrado perfeito, então é impressa a apenas a soma dos quadrados com o simbolo de raiz.
    else:
        print("\nA norma do vetor é: √{}".format(sum_squares))

def get_int(description):
    try:
        return int(input(description))
    except ValueError:
        print("Valor inválido.")
        return get_int(description)

def get_vector():
    n = 0
    while True:
        n = get_int("Digite o número de coordenadas do vetor: ")
        if n > 0:
            break
    vector = []
    print()
    for i in range(n):
        vector.append(get_int("Digite a coordenada {}: ".format(i+1)))
    return vector

if __name__ == '__main__':
    main()