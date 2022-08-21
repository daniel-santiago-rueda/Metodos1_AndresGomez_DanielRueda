#!/bin/bash
pass=0

function checkvalue()
{
    if [ $1 -eq 1 ] || [ $1 -eq 0 ]
    then
        pass=1

    else
        echo "Intente de nuevo"

    fi
}

while [ $pass -eq 0 ]
do
    echo -n "Ingrese un número entero: "
    read n

    checkvalue $n

done