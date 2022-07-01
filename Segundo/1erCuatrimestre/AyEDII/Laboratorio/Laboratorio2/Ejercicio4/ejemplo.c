 /* 
./sorter ../input/empty.in
0

statistics for selection_sort
time elapsed=0.049,    comparisons:          0,    swaps:          0
statistics for insertion_sort
time elapsed=0.02,    comparisons:          0,    swaps:          0
statistics for quick_sort
time elapsed=0.017,    comparisons:          0,    swaps:          0


./sorter ../input/all-negative-100.in
100
-89 -66 -4 -19 -47 -30 -33 -12 -59 -77 -6 -38 -46 -40 -97 -41 -79 -69 -31 -67 -11 -72 -86 -5 -50 -92 -27 -22 -15 -71 -32 -34 -56 -49 -62 -91 -39 -63 -61 -21 -95 -84 -14 -53 -36 -90 -88 -10 -68 -100 -54 -70 -99 -98 -75 -51 -96 -58 -9 -52 -64 -57 -76 -73 -44 -26 -65 -8 -1 -82 -18 -28 -2 -42 -81 -37 -20 -60 -13 -3 -55 -85 -23 -29 -78 -74 -35 -43 -17 -24 -45 -48 -80 -93 -87 -94 -16 -7 -25 -83

statistics for selection_sort
time elapsed=0.298,    comparisons:       4950,    swaps:        100
statistics for insertion_sort
time elapsed=0.208,    comparisons:       2554,    swaps:       2458
statistics for quick_sort
time elapsed=0.088,    comparisons:       1066,    swaps:        157


./sorter ../input/all-positive-100.in
100
47 19 52 4 71 62 92 7 23 77 91 70 78 36 60 61 98 87 86 40 81 89 93 13 45 80 66 17 88 48 95 27 56 55 49 82 3 94 39 41 85 68 12 20 26 69 11 28 54 6 74 21 42 2 63 97 38 53 8 32 50 34 73 67 79 51 43 22 57 83 37 24 5 33 35 65 1 16 72 31 0 29 44 76 75 64 58 30 46 9 10 18 14 96 84 90 99 15 25 59

statistics for selection_sort
time elapsed=0.338,    comparisons:       4950,    swaps:        100
statistics for insertion_sort
time elapsed=0.249,    comparisons:       2863,    swaps:       2770
statistics for quick_sort
time elapsed=0.069,    comparisons:       1009,    swaps:        171

selection_sort: en all-positive y all-negative hace la misma cantidad de comparaciones porque 
hay la misma cantidad de numeros en el arreglo. En cambio los otros dos dependen de los valores 
del arreglo. 

./sorter ../input/example-sorted.in
5
0 -1 2 3 8

statistics for selection_sort
time elapsed=0.046,    comparisons:         10,    swaps:          5
statistics for insertion_sort
time elapsed=0.028,    comparisons:          4,    swaps:          0
statistics for quick_sort
time elapsed=0.034,    comparisons:         20,    swaps:          4

En este caso que el arreglo venga ordenado según goes before y tenga pocos elementos, 
el que menos tarda es insertion_sort puesto que no es necesario hacer swaps. 

./sorter ../input/example-unsorted.in
5
2 -1 3 8 0

statistics for selection_sort
time elapsed=0.042,    comparisons:         10,    swaps:          5
statistics for insertion_sort
time elapsed=0.021,    comparisons:          7,    swaps:          5
statistics for quick_sort
time elapsed=0.022,    comparisons:         10,    swaps:          4

// Conclusion: En este caso que el arreglo venga ordenado según goes before y tenga pocos elementos, 
el que menos tarda es insertion_sort puesto que no es necesario hacer swaps. 

./sorter ../input/sorted-asc-100.in
100
7 1657 1722 -3738 3753 3886 -4091 4908 -4959 5066 5823 6805 -7463 8365 -9207 9356 -9362 10557 10758 -11184 11338 -12320 12921 -13193 -14571 -15305 -15852 -16728 -17335 18019 -18302 19764 -20455 -21566 -22611 -22696 -24895 24901 -25595 -25667 -25680 -25951 -26130 -27130 -28072 28633 28669 -28857 28991 -29178 -29331 -29900 -29960 -30480 -32171 32935 32980 -33372 -35659 35765 -36896 -37112 37252 37881 -37997 39374 -39788 -40802 41553 41582 -42177 -42203 -45419 -45424 46328 -49923 -50385 -51819 -52145 52890 53224 53828 54379 -56195 57042 57799 58349 58642 59148 59317 -59413 60264 -60663 -61039 61084 61254 -62258 -63643 -63838 -63951

statistics for selection_sort
time elapsed=0.214,    comparisons:       4950,    swaps:        100
statistics for insertion_sort
time elapsed=0.03,    comparisons:         99,    swaps:          0
statistics for quick_sort
time elapsed=0.518,    comparisons:       9900,    swaps:         99

Nuevamente, el arreglo esta ordenado y el que menos demora es insertion_sort. 

./sorter ../input/sorted-asc-1000.in
statistics for selection_sort
time elapsed=10.759,    comparisons:     499500,    swaps:       1000
statistics for insertion_sort
time elapsed=0.029,    comparisons:       1001,    swaps:          2
statistics for quick_sort
time elapsed=9.422,    comparisons:     998134,    swaps:        997

Nuevamente, el arreglo esta ordenado y el que menos demora es insertion_sort. 

./sorter ../input/sorted-asc-10000.in
statistics for selection_sort
time elapsed=446.162,    comparisons:   49995000,    swaps:      10000
statistics for insertion_sort
time elapsed=0.188,    comparisons:      10398,    swaps:        399
statistics for quick_sort
time elapsed=888.459,    comparisons:   96110645,    swaps:       9626

Nuevamente, el arreglo esta ordenado y el que menos demora es insertion_sort. 

// Concluimos de example-sorted.in, sorted-asc-100.in, sorted-asc-1000.in, sorted-asc-10000.in
que para los casos en que el arreglo esté ordenado según goes_before (en modulo), el algoritmo 
de ordenacion que menos demora es insertion_sort puesto que hace menos swaps y comparaciones. 

./sorter ../input/sorted-desc-100.in
100
64776 64263 64142 -63523 63203 -62597 -62255 -59402 -58886 57241 56509 55043 54480 54062 53524 -52992 -52532 -51667 51342 51192 47800 47627 46500 45806 45805 -45131 44056 -44047 -43238 -42641 -42119 -39679 38812 -37912 37840 -36685 36613 -35645 -34324 33935 33856 33496 -33438 -31978 -31113 28687 -28342 28153 27347 27214 26506 24709 24524 24508 -24094 -23356 23188 22768 22381 21558 -21401 -20693 20245 -20220 -20095 19585 -19096 -18671 18579 -18328 -18159 -17914 -17457 -16658 16147 15699 14958 14830 -13943 -13363 11883 11491 9205 -9075 7896 -7372 7063 -6172 5820 5013 4371 -4037 3974 3788 -3218 2816 -2617 -1165 -950 399

statistics for selection_sort
time elapsed=0.235,    comparisons:       4950,    swaps:        100
statistics for insertion_sort
time elapsed=0.336,    comparisons:       4950,    swaps:       4950
statistics for quick_sort
time elapsed=0.279,    comparisons:       7400,    swaps:         99

En este caso que el arreglo viene ordenado de forma descebdebte, el que menos tarda es selection_sort, sin embargo
quick_sort lo hace 0,044 segundos después. Notar que la cantidad de swaps que 
realizan selection_sort y quick_sort es muy similar. 

./sorter ../input/sorted-desc-1000.in
statistics for selection_sort
time elapsed=9.666,    comparisons:     499500,    swaps:       1000
statistics for insertion_sort
time elapsed=9.311,    comparisons:     499500,    swaps:     499500
statistics for quick_sort
time elapsed=9.194,    comparisons:     749000,    swaps:        999

En este caso que el arreglo viene ordenado de forma descebdebte pero tenemos mayor cantidad
de elementos en el arreglo, el que menos tarda es quick_sort. Notar que la cantidad de swaps que 
realizan selection_sort y quick_sort es muy similar. 

./sorter ../input/sorted-desc-10000.in
statistics for selection_sort
time elapsed=504.659,    comparisons:   49995000,    swaps:      10000
statistics for insertion_sort
time elapsed=871.177,    comparisons:   49995000,    swaps:   49995000
statistics for quick_sort
time elapsed=690.967,    comparisons:   74990000,    swaps:       9999

En este caso que el arreglo viene ordenado de forma descendente y el que menos tarda es selection_sort. 
Notar que la cantidad de swaps que realizan selection_sort y quick_sort es muy similar  y las comparaciones
que realizan selection_sort e insertion_sort es la misma. 

// Conclusion: para el caso de arreglos ordenados de forma descendente segun goes_before, los algoritmos
mas eficientes son selecion_sort y quick_sort con una diferencia de tiempo similar considerando 
la longtud de los arreglos. Además, los swaps que realizan siempre difieren en 1. No ocurre lo mismo
con las comparaciones, lo que marca la diferencia de eficiencia segun el caso. 

./sorter ../input/unsorted-100.in
statistics for selection_sort
time elapsed=0.228,    comparisons:       4950,    swaps:        100
statistics for insertion_sort
time elapsed=0.183,    comparisons:       2555,    swaps:       2462
statistics for quick_sort
time elapsed=0.077,    comparisons:       1140,    swaps:        164

El mas eficiente es quick_sort puesto que hace menor cantidad de comparaciones. 

./sorter ../input/unsorted-1000.in
statistics for selection_sort
time elapsed=8.036,    comparisons:     499500,    swaps:       1000
statistics for insertion_sort
time elapsed=4.864,    comparisons:     252831,    swaps:     251836
statistics for quick_sort
time elapsed=0.308,    comparisons:      17761,    swaps:       2366

El mas eficiente es quick_sort puesto que hace menor cantidad de comparaciones. 

./sorter ../input/unsorted-10000.in
statistics for selection_sort
time elapsed=442.954,    comparisons:   49995000,    swaps:      10000
statistics for insertion_sort
time elapsed=426.72,    comparisons:   24839452,    swaps:   24829459
statistics for quick_sort
time elapsed=3.135,    comparisons:     248860,    swaps:      31525

El mas eficiente es quick_sort puesto que hace menor cantidad de comparaciones. 

./sorter ../input/unsorted-100000.in
statistics for selection_sort
time elapsed=44679.8,    comparisons:  704982704,    swaps:     100000
statistics for insertion_sort
time elapsed=44557.8,    comparisons: 2498635594,    swaps: 2498535610
statistics for quick_sort
time elapsed=47.04,    comparisons:    3547068,    swaps:     360595

El mas eficiente es quick_sort puesto que hace menor cantidad de comparaciones. 

// Conclusion: para el acaso de arreglos desordenados, sin importar el tamaño, el mas eficiente sera
quick_sort puesto que hace menor cantidad de comparaciones. Notar que esto ocurre para los arreglos 
all-negative-100  y all-positive-100.in, ambos arreglos desordenados segun goes_before. 
*/