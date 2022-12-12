import sys
if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    fname = 'test.txt'
with open(fname,'r') as fi:
    lines = fi.readlines()

class Directory:
    def __init__(self, parent, name):
        self.name = name
        self.parent = parent
        self.files = []
        self.children = []

    def compute_size(self):
        total = 0
        for c in self.children:
            total += c.compute_size()
        return total + sum([x.size for x in self.files])

    def find_dir(self, subdirname):
        for sd in self.children:
            if sd.name == subdirname:
                return sd

        return None

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

cwd = None
rd = Directory(None, '/')
for l in lines:
    if l.startswith('$ cd'):
        if l[5:7] == '..':
            # up one level
            cwd = cwd.parent
        elif l[5:6] == '/':
            cwd = rd
        else:
            # named dir
            subdir = l[5:].strip()
            cwd = cwd.find_dir(subdir)
            if cwd == None:
                exit(1)
    elif l.startswith('$ ls'):
        # don't care about this command
        continue
    else:
        # output for a directory listing, create dir lists and files 
        if l.startswith('dir '):
            # new directory
            nd = Directory(cwd, l[4:].strip())
            cwd.children.append(nd)
        else:
            # new file
            splt = l.strip().split(' ')
            nf = File(splt[1], int(splt[0]))
            cwd.files.append(nf)

def print_dir(pd, indentation):
    ident = " "
    for x in pd.children:
        print(f"{ident*indentation}dir {x.name}")
        print_dir(x, indentation+1)
    for x in pd.files:
        print(f"{ident*indentation}{x.size} {x.name}")

print_dir(rd, 0)

def compute_sizes(pd):
    total = 0
    for x in pd.children:
        total += compute_sizes(x)
    total += sum([x.size for x in pd.files])
    return total

# 70000000 --> disk space available
# unused space of at least 30000000 for the update

# need to find the smallest directory that if deleted would free up enough space
# on fs to run the update 

# compute unused space
used_space = compute_sizes(rd)
update_size = 30000000
unused = 70000000 - used_space
dir_needed = update_size - unused
# find dirs that are at least dir_needed size
candidates = []

def deletions(pd):
    total = 0
    for x in pd.children:
        total += deletions(x)
    total += sum([x.size for x in pd.files])
    if total >= dir_needed:
        candidates.append(total)
    return total

deletions(rd)
print('answer:', min(candidates))
