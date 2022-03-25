import numpy as np
from math import *
from cmath import *

def calculate(input):
    input = input.replace("^", "**")
    try:
        result = eval(input)
    except Exception as e:
        return(e)
    return(result)
