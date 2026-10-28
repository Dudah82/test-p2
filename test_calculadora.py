from calculadora import soma, calculadora1

def test_soma():
    result = soma(3, 4)
    assert result == 7

def test_calculadora_op_soma():
    result = calculadora1(1, 2, 3)
    assert result == 5

def test_calculadora_op_sub():
    result = calculadora1(2, 4, 2)
    assert result == 2
    
def test_calculadora_op_mult():
    result = calculadora1(3, 5, 4)
    assert result == 20