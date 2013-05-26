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
