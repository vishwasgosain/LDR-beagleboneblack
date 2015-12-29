# LDR-beagleboneblack
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC #thermistor
import time
ADC.setup()
while(1):
        value = ADC.read_raw("P9_33")
        print value
        time.sleep(0.5)
