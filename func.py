import numpy as np
#from math import *
from cmath import *

def calculate(input):
    input = input.replace("^", "**")
    try:
        result = eval(input)
        print(type(result))
        if isinstance(result,complex):
            print("here")
            print(result.real(), result.imag())
            if result.imag() == 0.0:
                result = result.real()
            if result.real() == 0.0:
                result = result.imag()*1j
    except Exception as e:
        return(e)
    return(result)
