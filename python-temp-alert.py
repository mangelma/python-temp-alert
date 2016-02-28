import requests
import time

while True:

	localtime = time.asctime( time.localtime(time.time()) )

 	file = open("/sys/bus/w1/devices/28-000004cdad42/w1_slave")

	text = file.read() 

	file.close() 

	# Split the text with new lines (\n) and select the second line. 
	secondline = text.split("\n")[1] 

	# Split the line into words, referring to the spaces, and select the 10th word (counting from 0). 
	temperaturedata = secondline.split(" ")[9] 

	# The first two characters are "t=", so get rid of those and convert the temperature from a string to a number. 
	temperature = float(temperaturedata[2:]) 

	# Put the decimal point in the right place and display it. 
	temperature = temperature / 1000 

	temperature = round(temperature, 1)

	print temperature	

	# value1 to send is temperature + timestamp
	
	# if temperature drops, send low temp alert
	if temperature < 5:
		try:
			requests.post('https://maker.ifttt.com/trigger/lowtempalert/with/key/cykmAmqps7Wod3aGyLwNNr', data = {"value1":temperature, "value2":localtime})
		except:
			pass
	# if temperature rises, send high temp alert
	if temperature > 20:
		try:
			requests.post('https://maker.ifttt.com/trigger/hitempalert/with/key/cykmAmqps7Wod3aGyLwNNr', data = {"value1":temperature, "value2":localtime})
		except:
			pass
	# for logging
	try:
		requests.post('https://maker.ifttt.com/trigger/templog/with/key/cykmAmqps7Wod3aGyLwNNr', data = {"value1":temperature, "value2":localtime})
	except:
		pass
	# wait for ten minutes
	time.sleep(1800)

