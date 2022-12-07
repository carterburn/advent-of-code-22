import sys
if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    fname = 'test.txt'
with open(fname,'r') as fi:
    lines = fi.readlines()

buf = lines[0]

# implement sliding window of size 14 until one is a unique string. using the set
# function in python to check if the length is 14 (really bad with large input,
# but should always be 14, making it constant time)
def start_of_msg(b):
    for i in range(len(b)-13):
        if len(set(b[i:i+14])) == 14:
            return i+14


print('answer:',start_of_msg(buf))
