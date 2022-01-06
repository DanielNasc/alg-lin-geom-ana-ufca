from sys import path, exit
path.insert(1, '../')
from vectors import *
from beauty_prints import equacao_reta, equacao_plano

from simple_term_menu import TerminalMenu

def main():

    # Usuario escolhe se quer a equação de uma reta ou de um plano.
    menu = TerminalMenu(['Reta', 'Plano'], title='O que deseja calcular?')
    escolha = menu.show()
    qtd_coordenadas = escolha + 2

    # Pedir ao usuario um ponto A
    A = get_ponto('A', qtd_coordenadas)

    """
    A forma de se calcular a equação da reta/do plano é diferente dependendo das informações que o usuário tem
    Podendo ser a partir de um ponto A e um vetor normal a ela ou a partir de um ponto A e um ponto B, no caso da equação da reta,
    ou pontos A, B e C não colineares, no caso da equação do plano.
    """
    print("\nQue informações você tem?")
    menu = TerminalMenu(['A e n', 'A e B' if qtd_coordenadas == 2 else 'A, B e C' , 'Sair'])
    opcao = menu.show()

    if opcao == 0:
        com_A_e_n(A, qtd_coordenadas)
    elif opcao == 1:
        com_A_e_B(A, qtd_coordenadas)
    else:
        print("\nSaindo...")

    return 0
    
# A forma mais fácil de se encontrar a equação, apenas substituindo as icógnitas pelas coordenadas do vetor normal
# (e com um pouco de calculo a mais)
def com_A_e_n(A, qtd_c):
    pv("normal à reta" if qtd_c == 2 else "normal ao plano")
    n = get_vector(qtd_c)

    print("\n> {}".format(equacao_reta(n, A) if qtd_c == 2 else equacao_plano(n, A)))

def com_A_e_B(A, qtd_c):
    B = get_ponto('B', qtd_c)

    pv("AB")
    v = []
    for i in range(qtd_c):
        v.append(B[i] - A[i])
    print(v, "\n")

    # Se o usuario estiver procurando a equação de um plano, precisamos apenas de um ponto B
    if qtd_c == 2:
        pv("normal à reta")
        # O vetor normal pode ser obtido apenas trocando a posição dos pares ordenados e invertendo o sinal de um deles.
        n = simplificar_vetor([v[1] * -1, v[0]])
        print(n, "\n")
        
        print("> A equação da reta é dada por: r: ax + by + c = 0")
        print("> Com isso, temos: {}".format(equacao_reta(n, A)))
    # Já se o usuario estiver procurando a equação de um plano, precisamos de um ponto B e um ponto C não colineares
    else:
        C = get_ponto('C', qtd_c)
        
        pv("AC")
        w = []
        for i in range(qtd_c):
            w.append(C[i] - A[i])
        print(w, "\n")

        if (checar_se_sao_colineares(v, w)):
            print("Digite vetores não colineares")
            exit(1)

        pv("normal ao plano")
        # O vetor normal pode ser obtido a partir do produto vetorial entre os vetores AB e AC
        # Já que o produto vetorial entre dois vetores é sempre um vetor perpendicular a ambos
        n = simplificar_vetor(cross_product(v, w))
        print(n, "\n")

        print("> A equação do plano é dada por: p: ax + by + cz = 0")
        print("> Com isso, temos: {}".format(equacao_plano(n, A)))

if __name__ == '__main__':
    main()
