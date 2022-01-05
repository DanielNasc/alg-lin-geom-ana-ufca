from math import sqrt

def beauty_root(squares_sum):

    i = 0
    while True:
        half_sqr_minus_i = (squares_sum // 2) - i
        sqrt_h = sqrt(half_sqr_minus_i)

        if (half_sqr_minus_i == 1): break

        if (squares_sum % half_sqr_minus_i == 0) and sqrt_h.is_integer():
            return "{}√{}".format(int(sqrt_h), squares_sum // half_sqr_minus_i)
        i += 1
    
    return "√{}".format(squares_sum)
            

def adicao_ou_subtracao(a, char):

    return f"+ {a}{char}" if a > 0 else (f"- {abs(a)}{char}" if a < 0 else "")

def equacao_reta(n, A: list):

    return "r: {} {} {} = 0".format(adicao_ou_subtracao(n[0], "x")[2:],
                               adicao_ou_subtracao(n[1], "y"),
                                adicao_ou_subtracao(-(n[0]*A[0] + n[1]*A[1]), ""))

def equacao_plano(n: list, A: list):

    ax = adicao_ou_subtracao(n[0], "x")
    ax = ax[2:] if ax[0] == "+" else ax

    return "r: {} {} {} {} = 0".format(ax,
                                 adicao_ou_subtracao(n[1], "y"),
                                    adicao_ou_subtracao(n[2], "z"),
                                        adicao_ou_subtracao(-(n[0]*A[0] + n[1]*A[1] + n[2]*A[2]), ""))
