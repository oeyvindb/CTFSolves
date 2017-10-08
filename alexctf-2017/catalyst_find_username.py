import angr

project = angr.Project("./catalyst_patched", load_options={"auto_load_libs":False})

#This function finds the username to the catalyst log system
def find_username():
	global project
	find_address 	= 0x400d92
	avoid_address 	= (0x400d7c, 0x400c83)
	entry_state 	= project.factory.entry_state()
	sim 			= project.factory.simgr(entry_state)

	#Find the username
	sim.explore(find=find_address, avoid=avoid_address)

	if len(sim.found) > 0:
		found = sim.found[0]
		username = found.posix.dumps(0)
		return username
	else:
		print "Username coud not be found!"

def main():
 	print find_username()

if __name__ == '__main__':
 	main() 
