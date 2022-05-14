import numpy as np
import sympy as sym
from math import *
from cmath import *
import matplotlib.pyplot as plt
import os

x, y, z = sym.symbols('x y z')
f, g = sym.symbols('f g', cls=sym.Function)

a = "a"
b = "b"
c = "c"
d = "d"

ans = None
history = []

var={
    "a":float(),
    "b":float(),
    "c":float(),
    "d":float()
}

def calculate(input):
    input = input.strip()

    input = input.replace("^", "**")
    input = input.replace("=", ",")
    input = input.replace("𝜋", "pi")
    input = input.replace("√", "sqrt")
    input = input.replace("j", "(1j)")
    input = input.replace("oo", "inf")
    input = input.replace("I", "sym.integrate")
    input = input.replace("D", "sym.diff")
    input = input.replace("Lim", "sym.limit")
    input = input.replace("E", "sym.expr.series")
    input = input.replace("So", "sym.solveset(sym.Eq")
    input = input.replace("Sin", "sym.sin")
    input = input.replace("Cos", "sym.cos")
    input = input.replace("Tan", "sym.tan")
    input = input.replace("Asin", "sym.arcsin")
    input = input.replace("Acos", "sym.arccos")
    input = input.replace("Atan", "sym.arctan")
    input = input.replace("Sinh", "sym.sinh")
    input = input.replace("Cosh", "sym.cosh")
    input = input.replace("Tanh", "sym.tanh")
    input = input.replace("arcsin", "np.arcsin")
    input = input.replace("arccos", "np.arccos")
    input = input.replace("arctan", "np.arctan")
    input = input.replace("Ln", "sym.ln")
    input = input.replace("ln", "log")
    input = input.replace("Log", "sym.log")
    input = input.replace("gcd", "np.gcd")
    input = input.replace("matrix", "np.matrix")
    input = input.replace("var_a", "var['a']")
    input = input.replace("var_b", "var['b']")
    input = input.replace("var_c", "var['c']")
    input = input.replace("var_d", "var['d']")

    if input.startswith("sym.solveset(sym.Eq"):
        input += ")"

    if input == "clear":
        return ("", "clear")

    try:
        print()
        print("     -- input --     ")
        print()
        print(input)
        print()
        print("     -- input --     ")
        print()
        result = eval(str(input))

        if input.startswith("plot("):
            return ("", "graph")

        if isinstance(result,complex):
            if result.imag == 0:
                result = result.real
            if result.real == 0:
                result = result.imag*1j
        result = str(result).replace("I", " i ")
        result = str(result).replace("j", " i ")
        return (result, "string")
    except Exception as e:
        return (e, "string")

def clear():
    return "clear"

def plot(function, bound1, bound2):
    function = str(function)
    print(function, bound1, bound2)
    print(type(function), type(bound1), bound2)
    plt.clf()
    x = np.linspace(bound1, bound2, 1000)
    y = []
    for i in range(1000):
        y.append(eval(function.replace("x", f"({x[i]})")))
    plt.title(function)
    plt.plot(x, y)
    print(os.listdir("static/graphs"))
    filesNumber = len(os.listdir("static/graphs")) + 1
    fileName = f"static/graphs/plot{filesNumber}.png"
    plt.savefig(fileName)

def set(variable, val):
    var[variable] = val
    return(f"set {variable} to {val}")
