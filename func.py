import numpy as np
from math import *

def calculate(input):
    try:
        result = eval(input)
    except Exception as e:
        return(e)
    return(result)
