import time
import sys

def wait(duration, type = 0, message = ""):
	speed = 4
	space = 6
	count = 0
	
	str_format = "%%s%%s %%%dd / %%d\r" % len(str(duration))

	my_range = range(duration * speed)
	if type == 1:
		my_range = reversed(range(duration * speed))

	for i in my_range:
		dot_string = ('%%-%ds' % space) % ((count + 1 ) * '.')
		print str_format % (message, dot_string , (i + 1) / speed, duration),
		sys.stdout.flush()
		time.sleep(1.0 / speed)
		count = (count + 1) % space

	print
	sys.stdout.flush()

def em(str):
	if sys.platform != 'win32' and sys.stdout.isatty():
		return "\033[4m\033[1m\x1B[3m"+str+"\x1B[23m\033[0m"
	else:
		return str

def db_decrypt(name):
	f = open(name, "rb")
	o = open(name + "_cracked", "wb")
	try:
	    byte = f.read(1)
	    while len(byte)>0:
	        re = 255 - ord(byte)
	        o.write(re.to_bytes(1, byteorder='big'))
	        byte = f.read(1)
	finally:
	    f.close()
	    o.close()

def schedule_task(t, command):
	"at \\\\localhost time command"
	pass