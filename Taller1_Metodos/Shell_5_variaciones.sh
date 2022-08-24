#!/bin/bash
echo $(( 20*19*18 ))

#TODO
#Punto 6

#Como en el ejercicio anterior se puede simplificar la fórmula V20_3 = 20!/(20-3)! a V20_3 = 20*19*18*17!/(17!) y,
#posteriormente, a V20_3 = 20*19*18, la complejidad corresponde a dos multiplicaciones, es decir, la complejidad es
#O(n^0 (r-1)^1) = O(r-1) puesto que, en el caso del punto 6, r-1 = 3-1 = 2 que es igual a la cantidad de operaciones necesarias
#para resolver la variación.
