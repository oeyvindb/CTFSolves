import binaryninja
from termcolor import colored
#Solving the Flareon 02 2017 challenge with Binary Ninja 
#Flag is:R_y0u_H0t_3n0ugH_t0_1gn1t3@flare-on.com
#Made by: Oyvind

ADDRESS_OBFUSCATED_FLAG = 0x403000
STARTING_ADDRESS_DECODE_LOOP = 0x403026     #This was found when reversing the binary, the decoding loop starts at the end of the user input
XOR_KEY = 4                                 #Based on return from func sub_401000, the initiated value of the XOR key is 4

def banner():
    banner="""
    \00
        ( ___)(  )    /__\  (  _ \( ___)(  _  )( \( )  (__ \ / _ \/  )(__ )   / _ \(__ \ 
        )__)  )(__  /(__)\  )   / )__)  )(_)(  )  (    / _/( (_) ))(  / /   ( (_) )/ _/ 
        (__)  (____)(__)(__)(_)\_)(____)(_____)(_)\_)  (____)\___/(__)(_/     \___/(____)
    \00
        """
    return banner

def main():
    print colored(banner(), "red")
    global XOR_KEY
    decode_ptr=STARTING_ADDRESS_DECODE_LOOP
    flag=[]

    # Creating a binary view with binja API
    bv=binaryninja.BinaryViewType["PE"].open("IgniteMe.exe")
    bv.update_analysis_and_wait()
    br=binaryninja.BinaryReader(bv)

    print "Starting decoding the flag!"
    while decode_ptr >= ADDRESS_OBFUSCATED_FLAG:
        br.seek(decode_ptr)
        XOR_KEY=(br.read8()^XOR_KEY)
        flag.append(chr(XOR_KEY))
        decode_ptr=decode_ptr-1

    flag=flag[::-1]
    print "The flag is:", colored("".join(flag), "green")

if __name__=="__main__":
    main()
