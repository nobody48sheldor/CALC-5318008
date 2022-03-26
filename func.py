import numpy as np
from math import *
from cmath import *
from sympy import *

x, y, z = symbols('x y z')
f, g = symbols('f g', cls=Function)

def calculate(input):
    input = input.replace("^", "**")
    input = input.replace("=", ",")
    input = input.replace("𝜋", "pi")
    input = input.replace("j", "1j")
    input = input.replace("oo", "inf")
    input = input.replace("I", "integrate")
    input = input.replace("D", "diff")
    input = input.replace("L", "limit")
    input = input.replace("E", "expr.series")
    input = input.replace("S", "solveset(Eq")
    if input.startswith("solveset(Eq"):
        input += ")"
    try:
        result = eval(input)
        if isinstance(result,complex):
            if result.imag == 0:
                result = result.real
            if result.real == 0:
                result = result.imag*1j
        return(str(result))
    except Exception as e:
        return(e)
