import binaryninja

ADDRESS_FLAG_FUNCTION=0x614 #This function checks the user input against en flag embedded in the binary
MAX_ADDRESS_RANGE=0xcae #After this address there is no logic for resolving the flag

def main():
    print "Solving the challenge easyarm!"
    bv = binaryninja.BinaryViewType["ELF"].open("easyarm.arm")
    bv.update_analysis_and_wait()
    flag={}
    flag_func=bv.get_function_at(ADDRESS_FLAG_FUNCTION)

    for block in flag_func.low_level_il:
        for il in block:
            if il.operation==binaryninja.LowLevelILOperation.LLIL_IF and il.address <= MAX_ADDRESS_RANGE and il.operands[0].right.value.value:
                index_instr=flag_func.low_level_il[il.instr_index-2] #jumping back 2 instructions to find the right offset for the character
                char_index=index_instr.operands[1] 
                if len(char_index.operands) > 1:
                    flag[char_index.operands[1].value.value]=chr(il.operands[0].right.value.value) #instert the flag char at the correct index
                else:
                    flag[0]=chr(il.operands[0].right.value.value)

                    
    printable_flag=""
    
    for char in flag.itervalues():
        printable_flag+=char

    print "The flag is %s" % printable_flag



if __name__=="__main__":
    main()
