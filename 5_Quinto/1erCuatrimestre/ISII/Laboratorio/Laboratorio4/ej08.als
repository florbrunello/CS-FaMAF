open util/ordering[State]

abstract sig Object {
	hits: set Object
 }

one sig police, criminal, girl1, girl2, boy1, boy2, mother, father, raft extends Object {}

fact hiting {
	hits = mother -> boy1 + mother -> boy2 + father -> girl1 + father -> girl2 
	      + criminal -> girl1 + criminal -> girl2 + criminal -> boy1 + criminal -> boy2
	      + criminal -> mother + criminal -> father 
 }

sig State {
	near: set Object,
	far: set Object,
 }

fact initialState {
	let s0 = first[] | s0.near = Object && no s0.far
 }

pred crossRiver [from_i,from_o,to_i,to_o: set Object ] {
	let violents = ( (police not in to_i implies to_i & criminal) + 
				(mother not in to_i implies to_i & father) + 
				(father not in to_i implies to_i & mother) ) |
	some responsable: from_i & (police + mother + father) |
		( from_o = from_i - responsable - raft && 
		   to_o = to_i - violents.hits + responsable + raft ) ||
		( some other: from_i - responsable - raft | 
		   from_o = from_i - responsable - other  - raft &&
		   to_o = to_i - violents.hits + 
			      (responsable - other.hits) + 
			      (other - responsable.hits) + raft )
}

fact stateTransition {
	all s1: State, s2: next[s1] |
	( raft in s1.near => crossRiver[s1.near,s2.near,s1.far,s2.far] ) &&
	( raft in s1.far => crossRiver[s1.far,s2.far,s1.near,s2.near ] )
}

pred solvePuzzle[] {
	some s: State | s.far = Object
}

run solvePuzzle for 20 State
