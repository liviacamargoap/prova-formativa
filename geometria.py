def classificar_triangulo(a: int, b: int, c:int):
    if a < 0 or b < 0 or c < 0:
        raise ValueError ("Lados devem ser positivos")
    
    if (a + b > c) or (a + c > b) or (b + c > a):
        raise ValueError ("Lados não formam um triângulo")
    
    if (a==b) or (c==b):
        return "Equilátero"
    
    if (a == b) or (a == c) or (b == c):
        return "Isósceles"
    