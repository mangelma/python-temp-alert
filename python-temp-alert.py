# apt-get install python-pip
# pip install requests
# based on https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/temperature/

import requests
import time

while True:

	# timestamp
	localtime = time.asctime( time.localtime(time.time()) )

	# Open the file that we viewed earlier so that python can see what is in it. Replace the serial number as before. 
	tfile = open("/sys/bus/w1/devices/10-000802824e58/w1_slave")

	# Read all of the text in the file. 
	text = tfile.read() 

	# Close the file now that the text has been read. 
	tfile.close() 

	# Split the text with new lines (\n) and select the second line. 
	secondline = text.split("\n")[1] 

	# Split the line into words, referring to the spaces, and select the 10th word (counting from 0). 
	temperaturedata = secondline.split(" ")[9] 

	# The first two characters are "t=", so get rid of those and convert the temperature from a string to a number. 
	temperature = float(temperaturedata[2:]) 

	# Put the decimal point in the right place and display it. 
	temperature = temperature / 1000 

	print temperature	

	# value1 to send is temperature + timestamp
	value1 = temperature + " " + localtime

	# if temperature drops, send low temp alert
	if temperature < 16:
		requests.post('https://maker.ifttt.com/trigger/lowtempalert/with/key/cykmAmqps7Wod3aGyLwNNr', data = {"value1":value1})

	# if temperature rises, send high temp alert
	if temperature > 20:
		requests.post('https://maker.ifttt.com/trigger/hitempalert/with/key/cykmAmqps7Wod3aGyLwNNr', data = {"value1":value1})

	# wait
	time.sleep(30)

