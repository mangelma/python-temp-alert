# python-temp-alert
RasPi + DS18D20 + IFTTT-Maker
Based on https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/temperature/
Make sure you got the requests library for Python:
```
sudo apt-get install python-pip
pip install requests
```
Add dtoverlay=w1-gpio to config.txt:
```
sudo nano /boot/config.txt
```
Cloning
```
git clone https://github.com/mangelma/python-temp-alert.git
```
