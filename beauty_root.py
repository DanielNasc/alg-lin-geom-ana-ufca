from math import sqrt

def beauty_root(squares_sum):
    """
    Function that prints the path to a file
    """

    i = 0
    while True:
        half_sqr_minus_i = (squares_sum // 2) - i
        sqrt_h = sqrt(half_sqr_minus_i)

        if (half_sqr_minus_i == 1): break

        if (squares_sum % half_sqr_minus_i == 0) and sqrt_h.is_integer():
            return "{}√{}".format(int(sqrt_h), squares_sum // half_sqr_minus_i)
        i += 1
    
    return "√{}".format(squares_sum)
            
            