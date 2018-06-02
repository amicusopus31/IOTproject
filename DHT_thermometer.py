#!/usr/bin/python
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import sys

import Adafruit_DHT

#seven segment display part
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

f_botton_right=23
f_botton_left=7
f_bottom=8
f_middle=10
f_top=11
f_top_right=5
f_top_left=22

s_botton_right=26
s_botton_left=13
s_bottom=6
s_middle=19
s_top=20
s_top_right=21
s_top_left=16
 
GPIO.setup(f_botton_right, GPIO.OUT)
GPIO.setup(f_botton_left, GPIO.OUT)
GPIO.setup(f_bottom, GPIO.OUT)
GPIO.setup(f_middle, GPIO.OUT)
GPIO.setup(f_top, GPIO.OUT)
GPIO.setup(f_top_right, GPIO.OUT)
GPIO.setup(f_top_left, GPIO.OUT)

GPIO.setup(s_botton_right, GPIO.OUT)
GPIO.setup(s_botton_left, GPIO.OUT)
GPIO.setup(s_bottom, GPIO.OUT)
GPIO.setup(s_middle, GPIO.OUT)
GPIO.setup(s_top, GPIO.OUT)
GPIO.setup(s_top_right, GPIO.OUT)
GPIO.setup(s_top_left, GPIO.OUT)
 
def fzero(): 
	GPIO.output(f_top_left, 1)
	GPIO.output(f_botton_right, 1)
	GPIO.output(f_bottom, 1)
	GPIO.output(f_botton_left, 1)
	GPIO.output(f_top, 1)
	GPIO.output(f_top_right, 1)
	
def szero(): 
	GPIO.output(s_top_left, 1)
	GPIO.output(s_botton_right, 1)
	GPIO.output(s_bottom, 1)
	GPIO.output(s_botton_left, 1)
	GPIO.output(s_top, 1)
	GPIO.output(s_top_right, 1)
	
def fone(): 
	GPIO.output(f_top_right, 1)
	GPIO.output(f_botton_right, 1)
	
def sone(): 
	GPIO.output(s_top_right, 1)
	GPIO.output(s_botton_right, 1)
	
def ftwo(): 
	GPIO.output(f_bottom, 1)
	GPIO.output(f_botton_left, 1)
	GPIO.output(f_top, 1)
	GPIO.output(f_top_right, 1)
	GPIO.output(f_middle, 1)

def stwo(): 
	GPIO.output(s_bottom, 1)
	GPIO.output(s_botton_left, 1)
	GPIO.output(s_top, 1)
	GPIO.output(s_top_right, 1)
	GPIO.output(s_middle, 1)
	
def fthree(): 
	GPIO.output(f_botton_right, 1)
	GPIO.output(f_bottom, 1)
	GPIO.output(f_middle, 1)
	GPIO.output(f_top, 1)
	GPIO.output(f_top_right, 1)
	
def sthree(): 
	GPIO.output(s_botton_right, 1)
	GPIO.output(s_bottom, 1)
	GPIO.output(s_middle, 1)
	GPIO.output(s_top, 1)
	GPIO.output(s_top_right, 1)

def ffour(): 
	GPIO.output(f_top_left, 1)
	GPIO.output(f_botton_right, 1)
	GPIO.output(f_middle, 1)
	GPIO.output(f_top_right, 1)

def sfour(): 
	GPIO.output(s_top_left, 1)
	GPIO.output(s_botton_right, 1)
	GPIO.output(s_middle, 1)
	GPIO.output(s_top_right, 1)

def ffive(): 
	GPIO.output(f_top_left, 1)
	GPIO.output(f_botton_right, 1)
	GPIO.output(f_bottom, 1)
	GPIO.output(f_top, 1)
	GPIO.output(f_middle, 1)
	
def sfive(): 
	GPIO.output(s_top_left, 1)
	GPIO.output(s_botton_right, 1)
	GPIO.output(s_bottom, 1)
	GPIO.output(s_top, 1)
	GPIO.output(s_middle, 1)

def fsix(): 
	GPIO.output(f_middle, 1)
	GPIO.output(f_top_left, 1)
	GPIO.output(f_botton_right, 1)
	GPIO.output(f_bottom, 1)
	GPIO.output(f_botton_left, 1)
	GPIO.output(f_top, 1)
	
def ssix(): 
	GPIO.output(s_middle, 1)
	GPIO.output(s_top_left, 1)
	GPIO.output(s_botton_right, 1)
	GPIO.output(s_bottom, 1)
	GPIO.output(s_botton_left, 1)
	GPIO.output(s_top, 1)

def fseven(): 
	GPIO.output(f_botton_right, 1)
	GPIO.output(f_top, 1)
	GPIO.output(f_top_right, 1)
	
def sseven(): 
	GPIO.output(s_botton_right, 1)
	GPIO.output(s_top, 1)
	GPIO.output(s_top_right, 1)

def feight(): 
	GPIO.output(f_middle, 1)
	GPIO.output(f_top_left, 1)
	GPIO.output(f_botton_right, 1)
	GPIO.output(f_bottom, 1)
	GPIO.output(f_botton_left, 1)
	GPIO.output(f_top, 1)
	GPIO.output(f_top_right, 1)
	
def seight(): 
	GPIO.output(s_middle, 1)
	GPIO.output(s_top_left, 1)
	GPIO.output(s_botton_right, 1)
	GPIO.output(s_bottom, 1)
	GPIO.output(s_botton_left, 1)
	GPIO.output(s_top, 1)
	GPIO.output(s_top_right, 1)

def fnine(): 
	GPIO.output(f_top_left, 1)
	GPIO.output(f_botton_right, 1)
	GPIO.output(f_bottom, 1)
	GPIO.output(f_middle, 1)
	GPIO.output(f_top, 1)
	GPIO.output(f_top_right, 1)
	
def snine(): 
	GPIO.output(s_top_left, 1)
	GPIO.output(s_botton_right, 1)
	GPIO.output(s_bottom, 1)
	GPIO.output(s_middle, 1)
	GPIO.output(s_top, 1)
	GPIO.output(s_top_right, 1)
	
def foff(): 
	GPIO.output(f_top_left, 0)
	GPIO.output(f_botton_right, 0)
	GPIO.output(f_bottom, 0)
	GPIO.output(f_botton_left, 0)
	GPIO.output(f_top, 0)
	GPIO.output(f_top_right, 0)
	GPIO.output(f_middle, 0)
	
def soff(): 
	GPIO.output(s_top_left, 0)
	GPIO.output(s_botton_right, 0)
	GPIO.output(s_bottom, 0)
	GPIO.output(s_botton_left, 0)
	GPIO.output(s_top, 0)
	GPIO.output(s_top_right, 0)
	GPIO.output(s_middle, 0)

# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    print('usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#')
    print('example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4')
    sys.exit(1)

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Un-comment the line below to convert the temperature to Fahrenheit.
# temperature = temperature * 9/5.0 + 32

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
if humidity is not None and temperature is not None:
    #print('Temp={0:0.0f}*  Humidity={1:0.0f}%'.format(temperature, humidity))
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    if int(temperature) == 20:
        ftwo()
        szero()
        time.sleep(5)
        time.sleep(5)
        foff()
        soff()
    elif int(temperature) == 21:
        ftwo()
        sone()
        time.sleep(5)
        time.sleep(5)
        foff()
        soff()
    elif int(temperature) == 22:
        ftwo()
        stwo()
        time.sleep(5)
        time.sleep(5)
        foff()
        soff()
    elif int(temperature) == 23:
        ftwo()
        sthree()
        time.sleep(5)
        time.sleep(5)
        foff()
        soff()
    elif int(temperature) == 24:
        ftwo()
        sfour()
        time.sleep(5)
        time.sleep(5)
        foff()
        soff()
    elif int(temperature) == 25:
        ftwo()
        sfive()
        time.sleep(5)
        time.sleep(5)
        foff()
        soff()
    elif int(temperature) == 26:
        ftwo()
        ssix()
        time.sleep(5)
        time.sleep(5)
        foff()
        soff()
    elif int(temperature) == 27:
        ftwo()
        sseven()
        time.sleep(5)
        time.sleep(5)
        foff()
        soff()
    elif int(temperature) == 28:
        ftwo()
        seight()
        time.sleep(5)
        time.sleep(5)
        foff()
        soff()
    elif int(temperature) == 29:
        ftwo()
        snine()
        time.sleep(5)
        time.sleep(5)
        foff()
        soff()
    elif int(temperature) == 30:
        fthree()
        szero()
        time.sleep(5)
        time.sleep(5)
        foff()
        soff()
    elif int(temperature) == 31:
        fthree()
        sone()
        time.sleep(5)
        time.sleep(5)
        foff()
        soff()
    elif int(temperature) == 32:
        fthree()
        stwo()
        time.sleep(5)
        time.sleep(5)
        foff()
        soff()
    elif int(temperature) == 33:
        fthree()
        sthree()
        time.sleep(5)
        time.sleep(5)
        foff()
        soff()
    elif int(temperature) == 34:
        fthree()
        sfour()
        time.sleep(5)
        time.sleep(5)
        foff()
        soff()

else:
    print('Failed to get reading. Try again!')
    sys.exit(1)
