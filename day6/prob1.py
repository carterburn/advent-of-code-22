import sys
if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    fname = 'test.txt'
with open(fname,'r') as fi:
    lines = fi.readlines()

buf = lines[0]

# implement sliding window of size 4 until one is a unique string. using the set
# function in python to check if the length is 4 (really bad with large input,
# but should always be 4, making it constant time)
def start_of_packet(b):
    for i in range(len(b)-3):
        if len(set(b[i:i+4])) == 4:
            return i+4


print('answer:',start_of_packet(buf))
