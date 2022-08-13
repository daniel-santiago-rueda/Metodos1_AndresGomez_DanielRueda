echo -n "Ingrese un número entero positivo: "
read n
echo calculando factorial de $n
function factorial(){
	local producto=1
	for i in $(seq 1 1 $n)
	do	
		producto=$(($producto*$i))
	done
	let fact=$producto
	
}


factorial

echo El factorial de $n es $fact.

