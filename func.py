import numpy as np
import sympy as sym
from math import *
from cmath import *

x, y, z = sym.symbols('x y z')
f, g = sym.symbols('f g', cls=sym.Function)

ans = None
history = []

def calculate(input):
    input = input.replace("^", "**")
    input = input.replace("=", ",")
    input = input.replace("𝜋", "pi")
    input = input.replace("j", "1j")
    input = input.replace("oo", "inf")
    input = input.replace("I", "sym.integrate")
    input = input.replace("D", "sym.diff")
    input = input.replace("Lim", "sym.limit")
    input = input.replace("E", "sym.expr.series")
    input = input.replace("So", "sym.solveset(sym.Eq")
    input = input.replace("Sin", "sym.sin")
    input = input.replace("Cos", "sym.cos")
    input = input.replace("Tan", "sym.tan")
    input = input.replace("arcSin", "sym.arcsin")
    input = input.replace("arcCos", "sym.arccos")
    input = input.replace("arcTan", "sym.arctan")
    input = input.replace("Sinh", "sym.sinh")
    input = input.replace("Cosh", "sym.cosh")
    input = input.replace("Tanh", "sym.tanh")
    input = input.replace("Ln", "sym.ln")
    input = input.replace("Log", "sym.log")
    if input.startswith("sym.solveset(sym.Eq"):
        input += ")"
    try:
        print()
        print("     -- input --     ")
        print()
        print(input)
        print()
        print("     -- input --     ")
        print()
        result = eval(str(input))
        if isinstance(result,complex):
            if result.imag == 0:
                result = result.real
            if result.real == 0:
                result = result.imag*1j
        result = str(result).replace("I", " i ")
        result = str(result).replace("j", " i ")
        return(result)
    except Exception as e:
        return(e)
