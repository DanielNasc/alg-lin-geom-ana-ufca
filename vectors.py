def get_int(description):
    try:
        return int(input(description))
    except ValueError:
        print("Valor inválido.")
        return get_int(description)

def get_float(description):
    try:
        return float(input(description))
    except ValueError:
        print("Valor inválido.")
        return get_float(description)

def get_ponto(letra, qtd_elementos):
    print("=== Preencha os valores do ponto {} ===\n".format(letra))
    ponto = []

    for i in range(qtd_elementos):
        ponto.append(get_float("Digite o valor da coordenada {}: ".format(
            i+1 if i >= 3 else chr(i + 120))))
    return ponto

def get_vector(size=0):
    if not size:
        size = 0
        while True:
            size = get_int("Digite o número de coordenadas do vetor: ")
            if size > 0:
                break
    vector = []
    print()
    for i in range(size):
        vector.append(get_int("Digite a coordenada {}: ".format(i+1)))
    return vector

def calculate_norm(vector):
    """
    Calcula a norma de um vetor
    """
    sum = 0
    for i in range(len(vector)):
        sum += vector[i]**2
    return [sum**(1/2), sum]

def inner_product(vector1, vector2):
    """
    Calcula o produto interno de dois vetores
    """
    if len(vector1) != len(vector2):
        raise ValueError("Vetores de tamanhos diferentes")
    sum = 0
    for i in range(len(vector1)):
        sum += vector1[i] * vector2[i]
    return sum

def cross_product(v, w):
    """
    Calcula o produto vetorial de dois vetores
    """
    if len(v) != len(w):
        raise ValueError("Vetores de tamanhos diferentes")
    if len(v) != 3:
        raise ValueError("Vetores de tamanho diferente de 3")
    return [v[1]*w[2] - v[2]*w[1], v[2]*w[0] - v[0]*w[2], v[0]*w[1] - v[1]*w[0]]

def pv(n):
    print("\n=== Vetor {} ===".format(n))

def checar_se_sao_colineares(v, w):
    """
    Checa se dois vetores são colineares
    """
    if len(v) != len(w):
        raise ValueError("Vetores de tamanhos diferentes")
    if inner_product(v, w) == 0:
        return True
    
    return False

def simplificar_vetor(v):
    vetor_s = []

    menor = v[0]
    for i in range(len(v)):
        if v[i] < menor:
            menor = v[i]

    metade_i_menor = abs(menor // 2)
    for i in range(int(metade_i_menor) - 1):

        for j in range(len(v)):
            vetor_s.append(v[j] / (metade_i_menor - i))
            if (v[j] % (metade_i_menor - i) != 0):
                vetor_s = []
                continue
            if j == len(v) - 1 and len(vetor_s) == len(v):
                return vetor_s
    return v