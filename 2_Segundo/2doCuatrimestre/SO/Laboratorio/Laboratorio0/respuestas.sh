#Práctico 0: ShellScripting

#Ejercicio 1:
cat /proc/cpuinfo | grep "model name"

#Ejercicio 2:
cat /proc/cpuinfo | grep "model name" | wc -l

#Ejercicio 3: 
wget https://www.gutenberg.org/files/11/11-0.txt && sed 's/Alice/Florencia/g' 11-0.txt > Florencia_in_wonderland.txt && rm 11-0.txt

#Ejercicio 4a: 
sort -k 6 -n weather_cordoba.in | head -n 1 

#Ejercicio 4b:
sort -k 5 -n weather_cordoba.in | tail -n 1

#Ejercicio 5: 
sort -k 3 -n atpplayers.in

#Ejercicio 6: 
awk 'dif=$7-$8 {print $0, dif}' superliga.in | sort -k 2 -k 9 -n

#Ejercicio 7: 
ip addr | grep 'link/ether' -i

#Ejercicio 8: 
mkdir peakyblinders && for i in {1..10}; do touch peakyblinders/fma_S01E"$i"_es.srt; done
for f in *_es*; do mv $f ${f%_es.srt}.srt; done