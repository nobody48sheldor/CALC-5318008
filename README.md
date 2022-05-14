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

### System
- `clear` to cleanup
- `ans` for the latest result
- `history[]` for the history

### Numbers:
- `ans` previous result (initialised with `None`) 
- `var_[]` variabe (exist for a, b, c, d), use set([], value)
- `inf` or `oo` for infinity
- `pi` or  `𝜋` for pi
- `e` for Euler's number
- `j` for i (the imaginary unit)
- tau, Nan...

### Functions
- `I(f(x))` for integral [`I(f(x), (x, lower_bound, upper_bound))`]
- `D(f(x))` for derivatives
- `Lim(f(x))` for limit
- `So(equation)` for equations
- `DE(differential equation)` for ODE [not yet]
- `plot(function, x-lower-bound, x-upper-bound)` for 2D plots
-  `sin(x)`, `cos(x)`... to get the output of the function at x
- BUT, `Sin(x)`, `Cos(x)`... to get the function, in order to integrate or take the derivative for example
- matrix for numpy's matrix
- set(variable name (a, b, c or d), value)

## Controls
<kbd>F9</kbd> : open menu

## Installation

## Clean install for raspberry (or any debian-based distro)

**In terminal :**
```
wget https://raw.githubusercontent.com/nobody48sheldor/CALC-5318008/main/install-script.sh; chmod +x install-script.sh; ./install-script.sh; rm install-script.sh
```

## Install from github

### General requirements :
- [NodeJS](https://nodejs.org/en/)
- [NPM](https://www.npmjs.com/)
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [Wget](https://www.gnu.org/software/wget/)

### GNU/LINUX and FreeBSD :
```
> git clone https://github.com/nobody48sheldor/CALC-5318008/tree/main
> ./install.sh
```
**To start :**
` > ./start.sh `

### WINDOWS [not fully functional] :
```
> git clone https://github.com/nobody48sheldor/CALC-5318008/tree/main
```
- Double click on `"install.bat"`

**To start :**
- Double click on `"start.bat"`


## Contributors

* [**n0b0dy48sheldor**](https://github.com/nobody48sheldor)
* [**Darkempire**](https://github.com/Darkempire78)
* [**GaetanAff**](https://github.com/GaetanAff)

