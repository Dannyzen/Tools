#Random string generator with char limitator. (Danny Rosen 4/10/2012)
#Twitter: @dannyzen
import random
import string
from time import time
from datetime import datetime

def random_file_name():
	t = str(datetime.now()).replace(' ', '-')
	char_set = string.ascii_lowercase + string.digits
	#char_set = string.ascii_lowercase
	#char_set = string.digits
	random_string=''.join(random.sample(char_set,6))
	print random_string
	
random_file_name()