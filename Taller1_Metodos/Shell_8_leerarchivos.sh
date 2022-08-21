#!/bin/bash

i=0
file=$1

while read -r line
do
rutas[$i]=$line
((i++))
done <$file

echo ${rutas[2]}