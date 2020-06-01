import pytest

def eh_bissexto(ano):
    resto = ano % 4
    resto100 = ano % 100
    resto400 = ano % 400
    return True if (not resto and resto100) or not resto400 else False


@pytest.mark.parametrize('ano', [1600, 1732, 1888, 1944, 2008])
def test_eh_bissexto(ano):
    assert eh_bissexto(ano) is True

@pytest.mark.parametrize('ano', [1742, 1889, 1951, 2011])
def test_não_eh_bissexto(ano):
    assert eh_bissexto(ano) is False