sig Interprete {}

sig Cancion {}

sig Catalogo {
	canciones: set Cancion,
	interpretes: set Interprete,
	interpretaciones: canciones some -> some interpretes
}

pred add [c_i, c_o:Catalogo, c:Cancion, i:Interprete] {
	c_o.interpretaciones = c_i.interpretaciones + (c->i)
}

pred delete [c_i, c_o:Catalogo, c:Cancion, i:Interprete] {
	c_o.interpretaciones = c_i.interpretaciones - (c->i)
}

fun par_int [c:Catalogo]: (Interprete -> Interprete) {
	(~(c.interpretaciones)) . (c.interpretaciones)
}

/*
fun par_int2 [c:Catalogo]: (Interprete -> Interprete) {
	{ a,b : Interprete |
		a != b and (a->b) in (~(c.interpretaciones)) . (c.interpretaciones) }
}
*/

pred show [c_i, c_o:Catalogo, c:Cancion, i:Interprete] {
	add [c_i, c_o, c, i]
	c_o.interpretaciones != c_i.interpretaciones
}

//run add for 3 but 2 Catalogo
run par_int for 7 but 2 Catalogo
