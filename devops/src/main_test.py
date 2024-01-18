from main import addition


def test_addition() -> None:
    nombre_1 = 1
    nombre_2 = 2

    assert addition(nombre_1, nombre_2) == 3
