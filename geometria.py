def classificar_triangulo(a: int, b: int, c:int):

    if not (isinstance(a,(int,float))) or (isinstance(b,(int,float))) or (isinstance(c,(int,float))): 
        raise TypeError

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError ("Lados devem ser positivos")
    
    if not (a + b > c) or (a + c > b) or (b + c > a):
        raise ValueError ("Lados não formam um triângulo")
    
    if (a==b) and (c==b):
        return "Equilátero"
    
    if (a == b) or (a == c) or (b == c):
        return "Isósceles"
    
    if (a != b) and (b != c) and (a != c):
        return "Escaleno"