import numpy as np
import sympy as sym
from math import *
from cmath import *
import matplotlib.pyplot as plt

x, y, z = sym.symbols('x y z')
f, g = sym.symbols('f g', cls=sym.Function)

ans = None
history = []

def calculate(input):
    input = input.strip()

    input = input.replace("^", "**")
    input = input.replace("=", ",")
    input = input.replace("𝜋", "pi")
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
    input = input.replace("Log", "sym.log")

    if input.startswith("sym.solveset(sym.Eq"):
        input += ")"

    if input.startswith("plot("):
        parameters = input.split(",",4)
        function = parameters[0].split("(", 1)[1]
        xmin = int(parameters[1])
        xmax = int(parameters[2].split(")",2)[0])
        borders = (xmin, xmax)
        print(function, borders)
        plot(function, borders)
        return ("", "graph")

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

def plot(function, bounds):
    plt.clf()
    x = np.linspace(bounds[0], bounds[1], 1000)
    y = []
    for i in range(1000):
        y.append(eval(function.replace("x", "({})".format((x[i])))))
    plt.title(function)
    plt.plot(x, y)
    plt.savefig("static/plot.png")
