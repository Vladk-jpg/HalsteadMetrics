import math

def compute_metrics(operators: dict, operands: dict) -> dict:
    """
      {
         'n1': кол-во уникальных операторов,
         'n2': кол-во уникальных операндов,
         'N1': общее кол-во вхождений операторов,
         'N2': общее кол-во вхождений операндов,
         'n':  n1 + n2,
         'N':  N1 + N2,
         'Volume': Halstead Volume = N * log2(n)
      }
    """
    n1 = len(operators)             
    n2 = len(operands)               
    N1 = sum(operators.values())      
    N2 = sum(operands.values())       

    n = n1 + n2                      
    N = N1 + N2                       

    if n > 0:
        volume = N * math.log2(n)
    else:
        volume = 0

    return {
        "n1": n1,
        "n2": n2,
        "N1": N1,
        "N2": N2,
        "n":  n,
        "N":  N,
        "Volume": volume
    }