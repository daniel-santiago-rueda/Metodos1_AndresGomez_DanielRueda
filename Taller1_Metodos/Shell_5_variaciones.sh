#!/bin/bash
function factorial()
{
	local producto=1
	for i in $(seq 1 1 $2)
	do
		producto=$(($producto*$i))
	done
	let $1=$producto
}

nfact=0
dfact=0

factorial nfact 20
factorial dfact 17

echo $(($nfact/$dfact))
#TODO
#Punto 6
#La complejidad es