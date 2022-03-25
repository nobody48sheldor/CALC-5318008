import numpy as np
from math import *
from cmath import *
from sympy import *

x, y, z = symbols('x y z')

def calculate(input):
    input = input.replace("^", "**")
    input = input.replace("=", ",")
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
        print(type(result))
        if isinstance(result,complex):
            print(result.real, result.imag)
            if result.imag == 0:
                result = result.real
            if result.real == 0:
                result = result.imag*1j
        return(str(result))
    except Exception as e:
        return(e)
