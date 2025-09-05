sig Label {}

one sig Tau extends Label {}

sig State {}

sig LTS {
	labels: set Label,
	states: set State,
	init: one states,
	step: labels -> states -> states
} {
	states = init.(*(step[labels]))
}

sig R {
	bin: State -> State
}

//Simulación
pred simulacion [r: State -> State, sys: LTS] {
	all a: sys.labels | ((~r).(sys.step[a])) in ((sys.step[a]).(~r))
}

//Bisimulación
pred bisimulacion [r: State -> State, sys: LTS] {
	simulacion [r, sys]
	simulacion [(~r), sys]
}

//Bisimulación débil
fun wstep [sys: LTS, a: Label]: State -> State {
	(*(sys.step[Tau])).(sys.step[a]).(*(sys.step[Tau])) + *(sys.step[Tau&a])
}

pred wsimulacion [r: State -> State, sys: LTS] {
	all a: sys.labels | ((~r).(sys.step[a])) in ((wstep[sys,a]).(~r))
}

pred wbisimulacion [r: State -> State, sys: LTS] {
	wsimulacion [r, sys]
	wsimulacion [(~r), sys]
}

pred wsimulacionLTS [r: State -> State, sys1, sys2: LTS] {
	some sys: LTS |
		sys.states = sys1.states + sys2.states and
		sys.step = sys1.step + sys2.step and 
		(sys1.init -> sys2.init) in r and 
		wsimulacion[r, sys]
}
