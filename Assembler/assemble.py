import sys
import getopt

instructions=['add',
	'and',
	'ber',
	'lst',
	'nor',
	'or',
	'sub',
	'lw',
	'sll',
	'srl',
	'sw',
	'lpc'',
	'spc',
	'lc',
	'addc'
	'j',
	'jal',
	'beq',
	'dply'}
op_codes={'add':'0000',
	'and':'0001',
	'ber':'0010',
	'lst':'0011',
	'nor':'0100',
	'or':'0101',
	'sub':'0110',
	'lw':'0111',
	'sll':'1001',
	'srl':'1010',
	'sw':'1011',
	'lpc':'1100',
	'spc':'1101',
	'lc':'1110',
	'addc':'1111'}
registers={'r0':'0000',
	'r1':'0001',
	'r2':'0010',
	'r3':'0011',
	'r4':'0100',
	'r5':'0101',
	'r6':'0110',
	'r7':'0111',
	'r8':'1000',
	'r9':'1001',
	'r10':'1010',
	'r11':'1011',
	'r12':'1100',
	'r13':'1101',
	'r14':'1110',
	'r15':'1111',
	'sp':'0000',
	'i0':'0001',
	'i1':'0010',
	'rv':'0011',
	'ra':'0100',
	'at':'0101',
	's0':'0110',
	's1':'0111',
	's2':'1000',
	'os0':'1001',
	'os1':'1010',
	'ex':'1011',
	't0':'1100',
	't1':'1101',
	't2':'1110',
	't3':'1111'}




def main(argv):
	try:
		opts, args =getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.Error:
		print("error")
		sys.exit(2)
	inputf='' 
	outputf=''
	for opt, arg in opts:
		if opt=="-h":
			print("test.py -i <input> -o <output>")
			sys.exit()
		elif opt in ("-i","--ifile"):
			print("input found:"+arg)
			inputf=open(arg,'r')
		elif opt in ("-o", "--ofile"):
			print("output found:"+arg)
			outputf=open(arg,'w')
	if inputf=='':
		print("pass in assembly file")
		sys.exit(1)
	if outputf=='':
		outputf=open('output.ass','w')
	line_num=0
	for l in inputf:
		outputf.write(parse(l)+'\n')
		line_num+=1

def parse(l):
	l=clean_string(l)
	l=l.lower()
	i=l.index(' ')
	c=l.index(',')
	if l[:i] in op_codes:
                if l[:i] is 'lc':
                        
                elif l[:i] is 'j':
                        return parseJ(l[(i+1):])
                elif l[:i] is 'jal':
                        return parseJAL(l[(i+1):]
                elif l[:i] is 'beq':
                        return parseBEQ(l[(i+1):]
                elif l[:i] is 'dply':
                        return parseDPLY(l[(i+1):]
                else:
                        return op_codes[l[:i]]+parse(l[(i+1):])
	if l[:c].rstrip() in registers:
		return registers[l[:c]]+parse(l[(c+1):])
	else:
		print("error in syntax
		sys.exit()

def parseLC(l):
        l=hex(int(l))
        if int(l)<=65,536:
                #running psuedo-version
                s=l[2:]
        elif int(l)<=256:
                #running hardware-version
                return '1110'+dest+l[2:]
        #throw exception here
                
def parseJ(l):
def parseJAL(l):
def parseBEQ(l):
def parseDPLY(l):
def clean_string(s):
        s=s.strip()
	if s=='':
		return ''
	return s.lower()
        
main(sys.argv[1:])
