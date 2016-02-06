#RasPi + DS18D20 + IFTTT-Maker
https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/temperature/

Make sure you got the requests library for Python:
```
sudo apt-get install python-pip
pip install requests
```
Add "dtoverlay=w1-gpio" to the end of config.txt, save and reboot
```
sudo nano /boot/config.txt
sudo reboot
```
Unique address of the DS18B20 can be found by
```
cd /sys/bus/w1/devices/
ls
```
Change it in the python-temp-alert.py
```
git clone https://github.com/mangelma/python-temp-alert.git
cd python-temp-alert/
nano python-temp-alert.py
```
Run the script
```
python python-temp-alert.py
```
