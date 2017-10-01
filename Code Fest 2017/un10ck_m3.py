import angr
#Made by Oyvind Brusethaug
#Contest: Code Fest CTF

def main():
	print "Code Fest CTF challenge un10ck_m3 Solver"
	print "Category: Reverse Engineering"
	print "Challenge: un10ck_m3"
	print "Made by: Oyvind"
	print ""
	find_address=0x400cca #At this point in the program the flag should be decoded into memory
	flag_address=0x6020f0 #Flag is decoded into this memory address

	project = angr.Project("un10ck_m3", load_options={"auto_load_libs":False})
	entry_state = project.factory.entry_state()
	sim = project.factory.simgr(entry_state)

	#Perfom symbolic execution until we find the address we are looking for
	sim.explore(find=find_address)

	if len(sim.found) > 0:
		found = sim.found[0]
		flag = found.se.eval(found.memory.load(flag_address, 20), cast_to=str).strip("\0")
		return flag

if __name__ == '__main__':
	print "The flag is: %s" % main()