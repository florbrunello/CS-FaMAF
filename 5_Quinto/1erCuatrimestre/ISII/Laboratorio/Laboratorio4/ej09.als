open util/ordering[State]

abstract sig Object {
	time: set Object
 }

one sig IndianaJones, novia, padre, suegro extends Object {}

fact timing {
	time = IndianaJones -> 5 + novia -> 10 + padre -> 20 + suegro -> 25
 }

sig State {
	near: set Object,
	far: set Object,
 }

fact initialState {
	let s0 = first[] | s0.near = Object && no s0.far
 }
