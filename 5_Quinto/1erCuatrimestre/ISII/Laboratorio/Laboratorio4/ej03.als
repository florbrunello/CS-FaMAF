sig Addr, Data {}

sig Memory{
	addrs: set Addr,
	map: addrs -> one Data
 }

sig MainMemory extends Memory {}

sig Cache extends Memory{
	dirty: set addrs
 }

sig System {
	cache: Cache,
	main: MainMemory
 }

/*
pred writeMem [m_i,m_o: Mem, a: Addr, d: Data ] {
	m_o.map = m_i.map ++ (a -> d)
}

pred writeSys [s_i,s_o: System, a: Addr, d: Data ] {
	s_o.main = s_i.main
	writeMem [s_i.cache,s_o.cache,a,d]
	s_o.cache.dirty = s_i.cache.dirty + a
}
*/

pred Load[s_i, s_o: System, a: Addr]{
	s_o.cache.map = s_i.cache.map ++ (a -> s_i.main.map[a])
	s_o.cache.dirty = s_i.cache.dirty ++ a
	s_o.main = s_i.main
}

pred Flush [s_i, s_o: System] {
	s_o.main.map = s_i.main.map ++ s_i.cache.map
	no s_o.cache.dirty
	s_o.cache.map = s_i.cache.map 
}

pred Consistent [s:System] {
	s.cache.map - (s.cache.dirty -> Data) in s.main.map
}

assert FlushConsistent {
	all s_i, s_o: System | Flush[s_i, s_o] && Consistent[s_i] implies Consistent[s_o] 
}

assert LoadConsistent {
	all s_i, s_o: System | some a: Addr | (Load[s_i, s_o, a] && Consistent[s_i]) implies Consistent[s_o] 
}

check LoadConsistent
check FlushConsistent
