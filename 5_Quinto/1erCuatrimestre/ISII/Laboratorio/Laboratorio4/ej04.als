sig Vertice {}

sig Grafo {
	vertices: set Vertice,
	aristas: vertices -> vertices
}

pred aciclico [g:Grafo]{
	no (iden & (^(g.aristas)))
}

pred noDirigido [g:Grafo]{
	g.aristas = ~(g.aristas)
}

pred fuertementeConexo [g:Grafo]{
	(^(g.aristas)) = (g.vertices -> g.vertices)
}

pred conexo [g:Grafo]{
	(g.vertices -> g.vertices) in ^(g.aristas + ~(g.aristas))
}

/*
pred conexo [g:Grafo]{
	*(g.aristas + ~(g.aristas)) & (g.vertices -> g.vertices) = (g.vertices -> g.vertices)
}
*/

pred compFuerteConexa [g:Grafo]{
	some g_1:Grafo | g_1.vertices in g.vertices and g_1.aristas in g.aristas 
	and fuertementeConexo[g_1] 
	//and g_1.vertices != g.vertices
}

pred compConexa [g:Grafo]{
	some g_1:Grafo | g_1.vertices in g.vertices and g_1.aristas in g.aristas 
	and conexo[g_1] 
	//and g_1.vertices != g.vertices
}

// run aciclico for 5 but 1 Grafo
// run noDirigido for 5 but 1 Grafo
// run fuertementeConexo for 5 but 1 Grafo
run conexo for 3 but 1 Grafo
//run compFuerteConexa for 5 but 2 Grafo
// run compConexa for 5 but 2 Grafo
