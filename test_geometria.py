import pytest 
from geometria import classificar_triangulo


@pytest.mark.happy_path
@pytest.mark.parametrize("a, b, c, resultado_triangulo",[

# Checando se os retornos dos tipo de triangulo estão certos

    (3, 5, 3, "Isósceles"),
    (7, 5, 3, "Escaleno"),
    (5, 5, 5, "Equilatero"),

])

def test_cenarios_validos_triangulo(a, b, c, resultado_triangulo ):
    resultado = classificar_triangulo (a, b, c)
    assert resultado == resultado_triangulo


@pytest.mark.error_handling
@pytest.mark.parametrize("a, b, c, resultado_triangulo",[

# Checando se os retornos dos tipo de triangulo estão certos

    (0, 0, 0,),
    (8, -2, -3),
    (8, 5, -3),

])

def test_nao_numerico(a, b, c):
    pytest.raises(TypeError, match="Lados devem ser positivos")
    classificar_triangulo(a, b, c,)


pytest.mark.error_handling
@pytest.mark.parametrize("a, b, c, resultado_triangulo",[

# Checando se os retornos são strings

    (6, 3, "zero"),
    (5, "dois", 3),
    ("cincos", 2, 3),

])

def test_nao_numerico(a, b, c):
    pytest.raises(TypeError, match="Os valores devem ser numéricos")
    classificar_triangulo(a, b, c,)


pytest.mark.error_handling
@pytest.mark.parametrize("a, b, c, resultado_triangulo",[

# Checando se os retornos são triangulos

    (3, 5, 2),
    (1, 2, 1),
    (3, 1, 3),

])

def test_lados_nao_formam_triangulo(a, b, c):
    with pytest.raises(ValueError, match="Lados não formam um triângulo"):
        classificar_triangulo(a, b, c)