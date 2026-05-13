"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from calculator import Calculator

def test_app():
    my_calculator = Calculator()
    welcome_message = my_calculator.get_hello_message()
    assert "== Calculatrice v1.0 ==" in welcome_message

# TODO: ajoutez les tests
def test_addition():
    my_calculator = Calculator()
    assert my_calculator.addition(2, 3) == 5
    assert my_calculator.addition(0, -3) == -3
    assert my_calculator.addition(10000, 10000000000) == 10000010000
    assert my_calculator.addition(-20, -53) == -73
    assert my_calculator.addition(-20000, 25000) == 5000

def test_subtraction():
    my_calculator = Calculator()
    assert my_calculator.subtraction(5, 3) == 2
    assert my_calculator.subtraction(50, 0) == 50
    assert my_calculator.subtraction(-20, -20) == 0
    assert my_calculator.subtraction(100000, 500000) == -400000
    assert my_calculator.subtraction(0, -27) == 27

def test_multiplication():
    my_calculator = Calculator()
    assert my_calculator.multiplication(5, 3) == 15
    assert my_calculator.multiplication(50, 0) == 0
    assert my_calculator.multiplication(50, -6) == -300
    assert my_calculator.multiplication(-10000, -1) == 10000
    assert my_calculator.multiplication(10000, 0.01) == 100

def test_division():
    my_calculator = Calculator()
    assert my_calculator.division(6, 3) == 2
    assert my_calculator.division(20, -2) == -10
    assert my_calculator.division(10, 0.1) == 100
    assert my_calculator.division(0.1, 100) == 0.001
    assert my_calculator.division(6, 0) == "Erreur : division par zéro"