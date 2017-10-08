import angr
import claripy

#Made by Oyvind Brusethaug

def main():
	print "Alex CTF 2017"
	print "Category: Reverse Engineering"
	print "Challenge: RE2"
	print "Made by: Oyvind"
	address_hidden_flag 	= 0x400e58 
	address_lookup_table 	= 0x6020c0
	flag 					= ""
	project = angr.Project("re2", load_options={"auto_load_libs":False})
	entry_state = project.factory.entry_state()

	for byte in range(0,128):
		pointer 		= 0x00
		char_pointer 	= 0x00

		if byte == 0:
			pointer = address_lookup_table
		else:
			pointer = address_lookup_table + (byte * 4)

		char_pointer = address_hidden_flag + entry_state.solver.eval(entry_state.memory.load(pointer,1))
		char = entry_state.se.eval(entry_state.memory.load(char_pointer,1),cast_to=str)
		flag += char

		if char == "}": # a bit dirty hack but i works :P
			break

	print "The flag is %s" % flag

if __name__ == '__main__':
	main()
