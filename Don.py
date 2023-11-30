import os, sys
os.system("git pull")
try:
    __import__("Don").Don_Xyz()
except Exception as e:
    exit(str(e))
 
