# Raspberry pi 3 thermometer tutorial
## equipment you will need
1. raspberry pi 3 *1
2. DHT22 *1
3. seven segment display *2
4. jumper line *20
5. bread board *1
## Wiring up DHT humidity sensors
![DHTWIRE](https://i.imgur.com/gGVOIq0.jpg)
## Test if DHT humidity sensors works
```cmd
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo apt-get update
sudo apt-get install build-essential python-dev
sudo python setup.py install
cd examples
sudo ./AdafruitDHT.py 2302 4
```
### The output would be
![DHToutput](https://i.imgur.com/3VErcqu.jpg)
## Wiring up seven segment display
![sevensegwire](https://i.imgur.com/hHWT7vn.jpg)
