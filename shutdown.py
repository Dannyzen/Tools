import sys
import os

class Shutdown:
	def __init__(self):
		if len(sys.argv) == 1:
			shutdown_stop()
		else:
			shutdown_time(sys.argv[1])

def shutdown_stop():
	os.system("shutdown /a")

def shutdown_time(time):
	time = int(time) * 60
	print(type(time))
	shutdown_string = "shutdown /s /t " + str(time)
	print shutdown_string
	os.system(shutdown_string)

if __name__ == "__main__":
	Shutdown()
