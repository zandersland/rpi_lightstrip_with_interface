import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from rpi_ws281x import PixelStrip, Color
import time
from phue import Bridge

# LED strip configuration:
LED_COUNT = 300  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 50  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53

switch_1 = 23
switch_2 = 24
switch_3 = 25
switch_4 = 12
switch_5 = 4
switch_6 = 17
switch_7 = 27
switch_8 = 22

class ledFunctions():
    def theaterChase(strip, color, wait_ms=50, iterations=10):
        """Movie theater light style chaser animation."""
        for j in range(iterations):
            for q in range(3):
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i + q, color)
                strip.show()
                time.sleep(wait_ms / 1000.0)
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i + q, 0)


    class rainbowFunctions():
        def wheel(pos):
            """Generate rainbow colors across 0-255 positions."""
            if pos < 85:
                return Color(pos * 3, 255 - pos * 3, 0)
            elif pos < 170:
                pos -= 85
                return Color(255 - pos * 3, 0, pos * 3)
            else:
                pos -= 170
                return Color(0, pos * 3, 255 - pos * 3)


        def rainbowCycle(strip, wait_ms=20, iterations=5):
            """Draw rainbow that uniformly distributes itself across all pixels."""
            for j in range(256 * iterations):
                for i in range(strip.numPixels()):
                    strip.setPixelColor(i, ledFunctions.rainbowFunctions.wheel(
                        (int(i * 256 / strip.numPixels()) + j) & 255))
                strip.show()
                time.sleep(wait_ms / 1000.0)


        def theaterChaseRainbow(strip, wait_ms=50):
            """Rainbow movie theater light style chaser animation."""
            for j in range(256):
                for q in range(3):
                    for i in range(0, strip.numPixels(), 3):
                        strip.setPixelColor(i + q, ledFunctions.rainbowFunctions.wheel((i + j) % 255))
                    strip.show()
                    time.sleep(wait_ms / 1000.0)
                    for i in range(0, strip.numPixels(), 3):
                        strip.setPixelColor(i + q, 0)
    
    
    class waveFunctions():
        def set_wave_array_red(strip, _list):
            next = _list[strip.numPixels()-1]
            for pos, x in enumerate(_list):
                _list[pos] = (x[0], next[1])
                strip.setPixelColor(x[0], Color(next[1], 0, 0))
                next = x
            return _list

        def set_wave_array_green(strip, _list):
            next = _list[strip.numPixels()-1]
            for pos, x in enumerate(_list):
                _list[pos] = (x[0], next[1])
                strip.setPixelColor(x[0], Color(0, next[1], 0))
                next = x
            return _list

        def set_wave_array_blue(strip, _list):
            next = _list[strip.numPixels()-1]
            for pos, x in enumerate(_list):
                _list[pos] = (x[0], next[1])
                strip.setPixelColor(x[0], Color(0, 0,next[1]))
                next = x
            return _list

        def set_wave_array_white(strip, _list):
            next = _list[strip.numPixels()-1]
            for pos, x in enumerate(_list):
                _list[pos] = (x[0], next[1])
                strip.setPixelColor(x[0], Color(next[1], next[1], next[1]))
                next = x
            return _list


        def wave_red(strip, delay=0.01):
            # initialize array
            lights = []
            for x in range(0, strip.numPixels()):
                if x <= 150:
                    strip.setPixelColor(x, Color(x, 0, 0))
                    lights.append((x, x))
                elif x >= 151 & x <= 299:
                    z = 300 - x
                    lights.append((x, z))
                    strip.setPixelColor(x, Color(z, 0, 0))

            for _ in range(0, 2000):
                ledFunctions.waveFunctions.set_wave_array_red(strip, lights)
                # print(lights[0], lights[150], lights[151], lights[299])
                strip.show()
                # time.sleep(0.5)


        def wave_green(strip, delay=0.01):
            # initialize array
            lights = []
            for x in range(0, strip.numPixels()):
                if x <= 150:
                    strip.setPixelColor(x, Color(0, x, 0))
                    lights.append((x, x))
                elif x >= 151 & x <= 299:
                    z = 300 - x
                    lights.append((x, z))
                    strip.setPixelColor(x, Color(0, z, 0))

            for _ in range(0, 2000):
                ledFunctions.waveFunctions.set_wave_array_green(strip, lights)
                # print(lights[0], lights[150], lights[151], lights[299])
                strip.show()
                # time.sleep(0.5)


        def wave_blue(strip, delay=0.01):
            # initialize array
            lights = []
            for x in range(0, strip.numPixels()):
                if x <= 150:
                    strip.setPixelColor(x, Color(0, 0, x))
                    lights.append((x, x))
                elif x >= 151 & x <= 299:
                    z = 300 - x
                    lights.append((x, z))
                    strip.setPixelColor(x, Color(0, 0, z))

            for _ in range(0, 2000):
                ledFunctions.waveFunctions.set_wave_array_blue(strip, lights)
                # print(lights[0], lights[150], lights[151], lights[299])
                strip.show()
                # time.sleep(0.5)


        def wave_white(strip, delay=0.01):
            # initialize array
            lights = []
            for x in range(0, strip.numPixels()):
                if x <= 150:
                    strip.setPixelColor(x, Color(x, x, x))
                    lights.append((x, x))
                elif x >= 151 & x <= 299:
                    z = 300 - x
                    lights.append((x, z))
                    strip.setPixelColor(x, Color(z, z, z))

            for _ in range(0, 2000):
                ledFunctions.waveFunctions.set_wave_array_white(strip, lights)
                # print(lights[0], lights[150], lights[151], lights[299])
                strip.show()
                # time.sleep(0.5)


    def coolStartUp(strip):
        if strip.numPixels() == 60:
            timesleepdelay = 0.05
        elif strip.numPixels() == 300:
            timesleepdelay = 0.005
        else:
            timesleepdelay = 0.5
        b.set_light(['Duck1', 'Duck 2'], {'transitiontime': 8, 'on': True, 'bri': 254, 'sat': 254, 'hue': 65535})
        for x, y in zip(reversed(range(int(strip.numPixels() / 4))),
                        range(int(strip.numPixels() / 4), int(strip.numPixels() / 4) * 2)):
            strip.setPixelColor(x, Color(255, 0, 0))
            strip.setPixelColor(x + int(strip.numPixels() / 2), Color(255, 0, 0))
            strip.setPixelColor(y, Color(255, 0, 0))
            strip.setPixelColor(y + int(strip.numPixels() / 2), Color(255, 0, 0))
            strip.show()
            time.sleep(timesleepdelay)
        b.set_light(['Duck1', 'Duck 2'], {'transitiontime': 8, 'on': False, 'bri': 254, 'sat': 254, 'hue': 65535})
        for x, y in zip(reversed(range(int(strip.numPixels() / 4))),
                        range(int(strip.numPixels() / 4), int(strip.numPixels() / 4) * 2)):
            strip.setPixelColor(x, Color(0, 0, 0))
            strip.setPixelColor(x + int(strip.numPixels() / 2), Color(0, 0, 0))
            strip.setPixelColor(y, Color(0, 0, 0))
            strip.setPixelColor(y + int(strip.numPixels() / 2), Color(0, 0, 0))
            strip.show()
            time.sleep(timesleepdelay)
        time.sleep(1)
        b.set_light(['Duck1', 'Duck 2'], {'transitiontime': 0, 'on': False, 'bri': 142, 'sat': 223, 'hue': 7225})
    
    def set_strip_color(strip, color):
        for x in range(int(strip.numPixels())):
            strip.setPixelColor(x, color)
        strip.show()


def read_switches():
    binary_switch_num = 0

    if GPIO.input(switch_1) == GPIO.HIGH:
        binary_switch_num += 1
        print("switch 1 is on")
    if GPIO.input(switch_2) == GPIO.HIGH:
        binary_switch_num += 2
        print("switch 2 is on")
    if GPIO.input(switch_3) == GPIO.HIGH:
        binary_switch_num += 4
        print("switch 3 is on")
    if GPIO.input(switch_4) == GPIO.HIGH:
        binary_switch_num += 8
        print("switch 4 is on")
    if GPIO.input(switch_5) == GPIO.HIGH:
        binary_switch_num += 16
        print("switch 5 is on")
    if GPIO.input(switch_6) == GPIO.HIGH:
        binary_switch_num += 32
        print("switch 6 is on")
    if GPIO.input(switch_7) == GPIO.HIGH:
        binary_switch_num += 64
        print("switch 7 is on")
    if GPIO.input(switch_8) == GPIO.HIGH:
        binary_switch_num += 128
        print("switch 8 is on")

    print(binary_switch_num)

    return binary_switch_num


if __name__ == '__main__':
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()

    GPIO.setmode(GPIO.BCM) # Use GPIO pin numbering
    GPIO.setup(switch_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set switch_1 to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(switch_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set switch_2 to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(switch_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set switch_3 to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(switch_4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set switch_4 to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(switch_5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set switch_5 to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(switch_6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set switch_6 to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(switch_7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set switch_7 to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(switch_8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set switch_8 to be an input pin and set initial value to be pulled low (off)

    try:
        print("starting...")
        
        b = Bridge('192.168.2.74')
        
        try:
            b.connect()
        except:
            pass
        
        for x in range(15):
            strip.setPixelColor(x, Color(255, 0, 0))
        strip.show()
        for x in range(15):
            strip.setPixelColor(x, Color(0, 255, 0))
            strip.show()
            time.sleep(1)
        for x in range(strip.numPixels()):
            strip.setPixelColor(x, Color(0, 0, 0))
        strip.show()

        ledFunctions.coolStartUp(strip=strip)
        while True:
            effect_num = read_switches()
            if effect_num == 1:
                # ledFunctions.theaterChase(strip=strip, color=Color(255, 0, 255), wait_ms=50, iterations=100)
                try:
                    b.set_light(['Duck1', 'Duck 2'], {'transitiontime': 0, 'on': True, 'bri': 254, 'sat': 254, 'hue': 65535})
                except:
                    pass
                ledFunctions.waveFunctions.wave_red(strip)
                try:
                    b.set_light(['Duck1', 'Duck 2'], {'transitiontime': 0, 'on': True, 'bri': 254, 'sat': 254, 'hue': 25500})
                except:
                    pass
                ledFunctions.waveFunctions.wave_green(strip)
                try:
                    b.set_light(['Duck1', 'Duck 2'], {'transitiontime': 0, 'on': True, 'bri': 254, 'sat': 254, 'hue': 46920})
                except:
                    pass
                ledFunctions.waveFunctions.wave_blue(strip)
                try:
                    b.set_light(['Duck1', 'Duck 2'], {'transitiontime': 0, 'on': True, 'bri': 175, 'sat': 0, 'hue': 46920})
                except:
                    pass
                ledFunctions.waveFunctions.wave_white(strip)
                ledFunctions.rainbowFunctions.rainbowCycle(strip, iterations=5)
                ledFunctions.rainbowFunctions.theaterChaseRainbow(strip)
            
            elif effect_num == 2:
                ledFunctions.rainbowFunctions.rainbowCycle(strip, iterations=10)
                ledFunctions.rainbowFunctions.theaterChaseRainbow(strip)

            elif effect_num == 3:
                for x in range(5):
                    try:
                        b.set_light(['Duck1', 'Duck 2'], {'transitiontime': 0, 'on': True, 'bri': 254, 'sat': 254, 'hue': 65535})
                    except:
                        pass

                    ledFunctions.set_strip_color(strip, Color(255, 0, 0))
                    time.sleep(0.5)
                    # b.set_light(['Duck1', 'Duck 2'], {'on': False, 'transitiontime': 0})
                    # ledFunctions.set_strip_color(strip, Color(0, 0, 0))
                    # time.sleep(1)
                    try:
                        b.set_light(['Duck1', 'Duck 2'], {'transitiontime': 0, 'on': True, 'bri': 254, 'sat': 254, 'hue': 46920})
                    except:
                        pass

                    ledFunctions.set_strip_color(strip, Color(0, 0, 255))
                    time.sleep(0.5)
                    # b.set_light(['Duck1', 'Duck 2'], {'on': False, 'transitiontime': 0})
                    # ledFunctions.set_strip_color(strip, Color(0, 0, 0))
                    # time.sleep(1)

                for x in range(5):
                    try:
                        b.set_light('Duck1', {'transitiontime': 0, 'on': True, 'bri': 254, 'sat': 254, 'hue': 65535})
                        b.set_light('Duck 2', {'transitiontime': 0, 'on': True, 'bri': 254, 'sat': 254, 'hue': 46920})
                    except:
                        pass
                    for y in range(0, int(strip.numPixels()), 4):
                        strip.setPixelColor(y, Color(255, 0, 0))
                        strip.setPixelColor(y+1, Color(255, 0, 0))
                    for y in range(2, int(strip.numPixels()) - 1, 4):
                        strip.setPixelColor(y, Color(0, 0, 255))
                        strip.setPixelColor(y+1, Color(0, 0, 255))
                    strip.show()
                    time.sleep(0.5)
                    try:
                        b.set_light('Duck1', {'transitiontime': 0, 'on': True, 'bri': 254, 'sat': 254, 'hue': 46920})
                        b.set_light('Duck 2', {'transitiontime': 0, 'on': True, 'bri': 254, 'sat': 254, 'hue': 65535})
                    except:
                        pass
                    for y in range(0, int(strip.numPixels()), 4):
                        strip.setPixelColor(y, Color(0, 0, 255))
                        strip.setPixelColor(y+1, Color(0, 0, 255))
                    for y in range(2, int(strip.numPixels()) - 1, 4):
                        strip.setPixelColor(y, Color(255, 0, 0))
                        strip.setPixelColor(y+1, Color(255, 0, 0))
                    strip.show()
                    time.sleep(0.5)

            elif effect_num == 4:
                try:
                    b.set_light(['Duck1', 'Duck 2'], {'transitiontime': 0, 'on': True, 'bri': 254, 'sat': 254, 'hue': 65535})
                except:
                    pass
                ledFunctions.waveFunctions.wave_red(strip)
                try:
                    b.set_light(['Duck1', 'Duck 2'], {'transitiontime': 0, 'on': True, 'bri': 254, 'sat': 254, 'hue': 25500})
                except:
                    pass
                ledFunctions.waveFunctions.wave_green(strip)
                try:
                    b.set_light(['Duck1', 'Duck 2'], {'transitiontime': 0, 'on': True, 'bri': 254, 'sat': 254, 'hue': 46920})
                except:
                    pass
                ledFunctions.waveFunctions.wave_blue(strip)
                try:
                    b.set_light(['Duck1', 'Duck 2'], {'transitiontime': 0, 'on': True, 'bri': 175, 'sat': 0, 'hue': 65535})
                except:
                    pass
                ledFunctions.waveFunctions.wave_white(strip)

            elif effect_num == 7:
                try:
                    b.set_light(['Duck1', 'Duck 2'], {'transitiontime': 0, 'on': True, 'bri': 254, 'sat': 254, 'hue': 65535})
                except:
                    pass
                ledFunctions.set_strip_color(strip, Color(255, 0, 0))
                time.sleep(3)

            elif effect_num == 8:
                try:
                    b.set_light(['Duck1', 'Duck 2'], {'transitiontime': 0, 'on': True, 'bri': 100, 'sat': 254, 'hue': 65535})
                except:
                    pass

                ledFunctions.set_strip_color(strip, Color(100, 0, 0))
                time.sleep(3)
            
            elif effect_num == 9:
                pass

            elif effect_num == 14:
                try:
                    b.set_light(['Duck1', 'Duck 2'], {'transitiontime': 0, 'on': True, 'bri': 254, 'sat': 254, 'xy': [0.5, 0.175]})
                except:
                    pass

                ledFunctions.set_strip_color(strip, Color(255, 0, 100))
                time.sleep(3)

            elif effect_num == 26:
                ledFunctions.coolStartUp(strip)

            
            else:
                for x in range(int(strip.numPixels())):
                    strip.setPixelColor(x, Color(0, 0, 0))
                strip.show()
                time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
