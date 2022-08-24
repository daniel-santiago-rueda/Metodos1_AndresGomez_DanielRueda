#!/bin/bash
function factorial()
{
	dif=$(( $2 - $3 ))
	END=$3

	local producto=1
	for i in $(seq 1 $END)
	do
		coeficiente=$(( $dif + $i ))
		producto=$(($producto*$coeficiente))
	done
	let $1=$producto
}

fact=0
dfact=0

factorial fact 20 3

echo $(($fact))

#TODO
#Punto 6
#Como en el ejercicio anterior se puede simplificar la fórmula V20_3 = 20!/(20-3)! a V20_3 = 20*19*18*17!/(17!) y,
#posteriormente, a V20_3 = 20*19*18, la complejidad corresponde a dos multiplicaciones, es decir, la complejidad es
#O(n^0 (r-1)^1) = O(r-1) puesto que, en el caso del punto 6, r-1 = 3-1 = 2 que es igual a la cantidad de operaciones necesarias
#para resolver la variación.
