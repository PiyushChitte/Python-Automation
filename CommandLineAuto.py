# Automation using Command Line Argument

import sys

print("----------- Automations by Piyush Chitte ------------")
print("Demonstration for command line argument")
print("Application name : "+sys.argv[0])

X = int(sys.argv[1])
Y = int(sys.argv[2])
Z = X + Y
print(Z)

