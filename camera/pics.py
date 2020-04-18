import time
import picamera
import pysftp
import os

myHost = 'kill.cs.rutgers.edu'
myUser = 'jrb340'
myPass = 'raspberrypi'
myOpts = pysftp.CnOpts()
myOpts.hostkeys = None

'''option 1:
with picamera.PiCamera() as camera:
	while(1):
		ts = time.gmtime()
		fname = time.strftime('%m%d_%H%M%S', ts) + '.jpg'

		camera.capture('pics/'+ fname)
		print('picture saved: ' + fname)
		time.sleep(30)
'''
'''option 2:'''
with pysftp.Connection(host=myHost, username=myUser, password=myPass, cnopts=myOpts) as sftp:
	print('connection established')
	sftp.cwd('/ilab/users/jrb340/pics/')

	
	with picamera.PiCamera() as camera:
		while(1):
			ts = time.gmtime()
			fname = time.strftime('%m%d_%H%M%S',ts)+'.jpg'
			
			camera.capture(fname)
			sftp.put(fname, fname)
			os.remove(fname)
			
			print('picture saved: ' + fname)
			time.sleep(30)




