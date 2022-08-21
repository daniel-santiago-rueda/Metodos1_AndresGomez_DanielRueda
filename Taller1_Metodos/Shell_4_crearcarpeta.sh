#!/bin/bash

if [ -d "data" ]
then
    echo "La carpeta data existe"

else
    echo "La carpeta data no existe"
    mkdir data
    echo "La carpeta data ha sido creada"

fi