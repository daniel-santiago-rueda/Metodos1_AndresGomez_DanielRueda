#!/bin/bash

function help(){

	echo "Debe ingresar 3 parámetros: posición inicial, velocidad inicial y tiempo total"
}

if ! [ $# -eq 3 ]; then
	help
	exit 1

else
    echo "corriendo programa"

fi