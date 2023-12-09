import os, sys
os.system("git pull")
try:
    __import__("Don").Menu().menu()
except Exception as e:
    exit(str(e))
 
