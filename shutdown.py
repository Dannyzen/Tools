#Twitter: Dannyzen
#Usage: python shutdown.py number_of_minutes
#If no minutes are given, it attempts to cancel any scheduled shutdowns 

import sys
import os

def shutdown_stop():
	os.system("shutdown /a")

def shutdown_time(time):
	time = int(time) * 60
	shutdown_string = "shutdown /s /t " + str(time)
	os.system(shutdown_string)

if len(sys.argv) == 1:
	shutdown_stop()
else:
	shutdown_time(sys.argv[1])
