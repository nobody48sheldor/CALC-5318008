# CALC-5318008

CALC-5318008 is an app made for turning your raspberry-pi into a fully functional and powerful scientific calculator for cheap !

![logo](https://cdn.discordapp.com/attachments/954359083799023617/957369179240026112/Idee_Logo_Calculette_V2.png)

## Raspberry-pi supported

In theory it should be from the **raspberry-pi 3**

## What can it do ?

 ### Formal calculation (give the formula) and numeral answers
 
- the usual `+, -, /, *, ^`
- calculus `∂/∂x (y and z also), ∫, lim, ODE`
- equations
- complex numbers
- common functions
- plot functions (2D and 3D) [not yet]
- miscellaneous functions

## Syntax

### Numbers:
- `ans` previous result (initialised with `None`) 
- `inf` or `oo` for infinity
- `pi` or  `𝜋` for pi
- `e` for Euler's number
- `1j` for i (the imaginary unit)
tau, Nan...

### Functions
- `I(f(x))` for integral [`I(f(x), (x, lower_bound, upper_bound))`]
- `D(f(x))` for derivatives
- `L(f(x))` for limit
- `S(equation)` for equations
- `DE(differential equation)` for ODE [not yet]

## Installation

```
> git clone https://github.com/nobody48sheldor/CALC-5318008
> ./install.sh
> ./start.sh
```

## Contributors

* [**n0b0dy48sheldor**](https://github.com/nobody48sheldor)
* [**Darkempire**](https://github.com/Darkempire78)
* [**GaetanAff**](https://github.com/GaetanAff)
