import binaryninja

OBFUSCATED_CODE_ADDRESS=0x40107c #Starting point of obfuscated code
XOR_KEY=0xa2
CONST_FACTOR=0x22 #This value is addded to the opcode after XOR-ing

def main():
    address_pointer=OBFUSCATED_CODE_ADDRESS
    bv=binaryninja.BinaryViewType["PE"].open("greek_to_me.exe")
    bv.update_analysis_and_wait()
    bw=binaryninja.BinaryWriter(bv)
    br=binaryninja.BinaryReader(bv)

    while address_pointer != (OBFUSCATED_CODE_ADDRESS+0x79):
        br.seek(address_pointer)
        bw.seek(address_pointer)
        bw.write8((br.read8()^XOR_KEY)+CONST_FACTOR)
        address_pointer=address_pointer+1

    #Save updated file
    bv.save("greek_to_me_mod.exe")

if __name__=="__main__":
    main()
