# CALC-5318008

CALC-5318008 is an app made for turning your raspberry-pi into a fully functional and powerful scientific calculator for cheap !

![logo](https://cdn.discordapp.com/attachments/954359083799023617/957369179240026112/Idee_Logo_Calculette_V2.png)

## Raspberry-pi supported

In theory it should be from the **raspberry-pi 3**

## What can it do ?

 ### Formal calculation (give the formula) and numerical answers
 
- the usual `+, -, /, *, ^`
- calculus `∂/∂x (y and z also), ∫, lim, ODE`
- equations
- complex numbers
- common functions (such as `sin, cos, ln ...`)
- plot functions in 2D (3D in comming)
- miscellaneous functions

## Syntax

### Numbers:
- `ans` previous result (initialised with `None`) 
- `inf` or `oo` for infinity
- `pi` or  `𝜋` for pi
- `e` for Euler's number
- `j` for i (the imaginary unit)
tau, Nan...

### Functions
- `I(f(x))` for integral [`I(f(x), (x, lower_bound, upper_bound))`]
- `D(f(x))` for derivatives
- `Lim(f(x))` for limit
- `So(equation)` for equations
- `DE(differential equation)` for ODE [not yet]
- `plot(function, x-lower-bound, x-upper-bound)` for 2D plots
-  `sin(x)`, `cos(x)`... to get the output of the function at x
- BUT, `Sin(x)`, `Cos(x)`... to get the function, in order to integrate or take the derivative for example

## Installation

###  general requirement :

- python and pip
- node js and npm

### GNU/LINUX and FreeBSD :
```
> git clone https://github.com/nobody48sheldor/CALC-5318008
> ./install.sh
```
to start : 

` > ./start.sh `

### WINDOWS :
```
> git clone https://github.com/nobody48sheldor/CALC-5318008
```
- double click on `"install.bat"`

to start :

- double click on `"start.bat"`


## Contributors

* [**n0b0dy48sheldor**](https://github.com/nobody48sheldor)
* [**Darkempire**](https://github.com/Darkempire78)
* [**GaetanAff**](https://github.com/GaetanAff)

