import angr
import claripy

#TJS CTF
#Challenge:Validate
#Made by:Oyvind Brusethaug

AVOID_ADDRESSES=[0x80485fd,0x80485eb,0x80485d9] #These addresses we waint to avoid
FIND_ADDRESS=0x80485c7 #At this address we have a valid flag

def main():
    print "Solving the validator challenge with angr!"
    proj=angr.Project("./flagcheck")
    argv1=claripy.BVS("argv1", 43*8) #Flag size should be 43 bytes according
    initial_state=proj.factory.entry_state(args=["./flagcheck",argv1])
    sm=proj.factory.simulation_manager(initial_state)

    #Symbolically execute until out instruction pointer finds the address we want
    sm.explore(find=FIND_ADDRESS,avoid=AVOID_ADDRESSES)

    if len(sm.found) > 0:
        print "Got the state we are looking for, lets see if we can get the flag"
        solution=sm.found[0].solver.eval(argv1,cast_to=str)
        print "The flag is: %s" % repr(solution)
    else:
        print "Could not find the state we want, please tune your script"


if __name__=="__main__":
    main()
