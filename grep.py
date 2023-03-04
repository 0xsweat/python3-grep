import sys
from colorama import Fore
r = """
    ▗ ▌     ▄▖          
▛▌▌▌▜▘▛▌▛▌▛▌▄▌▄▖▛▌▛▘█▌▛▌
▙▌▙▌▐▖▌▌▙▌▌▌▄▌  ▙▌▌ ▙▖▙▌
▌ ▄▌            ▄▌    ▌ 
"""
usage = Fore.MAGENTA + str(r) + "coded by : 0x.sweat\nusage : python3 grep.py FILE WORD"
try:
    file = sys.argv[1]
except:
    print(usage)
    print(Fore.RED + "No file specified")
    quit()
try:
    word = sys.argv[2]
except:
    print(usage)
    print(Fore.RED + "No word specified")
    quit()
try:
    with open(file, 'r') as f:
        c = f.read()
        f.close()
except:
    print(usage)
    print(Fore.RED + "Could not open the file specified")
    quit()
cs = c.split("\n")
for i in range(0,len(cs) - 1):
    if word in cs[i]:
        print("line " + str(i + 1) + "\n" + cs[i])
