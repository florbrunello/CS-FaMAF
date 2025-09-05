sig Elem {}

sig Rel {
	rel: Elem -> Elem
}

fun idenElem[] : Elem -> Elem {
	 iden & (Elem -> Elem)
}

pred reflexiva[r:Rel] {
	idenElem in r.rel
}

pred simetrica[r:Rel]{
	(r.rel in ~(r.rel))
}

pred antisimetrica[r:Rel]{
	(r.rel & ~(r.rel)) in idenElem
}


pred transitiva[r:Rel]{
	(r.rel).(r.rel) in r.rel
}

pred preorden[r:Rel]{
	reflexiva[r] and transitiva[r]
}

pred ordenParcial[r:Rel] {
	preorden[r] and antisimetrica[r]
}

fun univElem[]: Elem -> Elem {
	Elem -> Elem
}

pred total[r:Rel]{
	univElem = r.rel + ~(r.rel)
}

pred ordenTotal[r:Rel]{
	ordenParcial[r]
	total[r]
}

// versión Santiago
pred asimetrica[r:Rel]{
	no r.rel & ~(r.rel)
}

pred irreflexiva[r:Rel]{
	no idenElem & r.rel
}

pred ordenEstrictoS[r:Rel]{
  irreflexiva[r]
  asimetrica[r]
  transitiva[r]
}

// versión Marcos

pred ordenEstrictoM[r:Rel]{
	antisimetrica[r]
	transitiva[r]
	irreflexiva[r]
}

pred show[r:Rel]{
	ordenEstrictoM[r]
	some r.rel
}

run show for exactly 5 Elem, 1 Rel

assert mismaDef {
	all r:Rel |
	  ordenEstrictoS[r] iff ordenEstrictoM[r]
}

check mismaDef for 25


assert parcialEsTotal {
	all r:Rel |
	  ordenParcial[r] implies ordenTotal[r]
}

check parcialEsTotal for 5 but 1 Rel
