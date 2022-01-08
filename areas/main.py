from sys import path, exit
path.insert(1, '../')
from vectors import *
from utils import *
from simple_term_menu import TerminalMenu
from beauty_prints import beauty_root

def main():
    qtd_c = reta_ou_plano()

    print(  "A área de um paralelogramo em E^2 é dada por |det[u, v]|" if qtd_c == 2 else 
            "O volume de qualquer paralelepípedo em E^3 é dada por |det[u, v, w]|")

    menu = TerminalMenu(['Pontos ABCD', 'Vetores'], title='Que informações você tem?')
    escolha = menu.show()
    if escolha == 0:
        if qtd_c == 3:
            print('Ainda não implementado')
            exit()
        com_pontos(qtd_c)
    elif escolha == 1:
        com_vetores(qtd_c)


def com_vetores(qtd_c):
    vectors = []
    for i in range(2):
        pv(chr(i + 117))
        vectors.append(get_vector(qtd_c))

    if (qtd_c == 3):
        vol = calculate_norm(cross_product(vectors[0], vectors[1]))
        vol = vol[0] if vol[0] == int(vol[0]) else beauty_root(vol[1])
        print("\nO volume é: ", vol)
        return

    print("\nA área é: ", abs(calculate_det(vectors)))

def com_pontos(qtd_c):
    points = []
    for i in range(4):
        print()
        points.append(get_ponto(chr(i + 65), qtd_c))

    v_AB = calculate_vector(points[0], points[1])
    v_BC = calculate_vector(points[1], points[2])
    v_AD = calculate_vector(points[0], points[3])
    v_DC = calculate_vector(points[3], points[2])

    if (v_AB == v_DC and v_BC == v_AD):
        print("\nA área é: ", abs(calculate_det([v_AB, v_AD])))
        return
    
    area = (1/2 * abs(calculate_det([v_AD, v_DC]))) + (1/2 * abs(calculate_det([v_AB, v_BC])))
    print("\nA área é: ", area)

if __name__ == "__main__":
    main()
