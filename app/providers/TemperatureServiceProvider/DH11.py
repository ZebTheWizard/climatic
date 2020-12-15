import RPi.GPIO as GPIO
import time

def _setup(channel):
    GPIO.setmode(GPIO.BOARD)
    time.sleep(2)
    GPIO.setup(channel, GPIO.OUT)
    GPIO.output(channel, GPIO.LOW)
    time.sleep(0.02)
    GPIO.output(channel, GPIO.HIGH)
    GPIO.setup(channel, GPIO.IN)
    
def _get_buffer(channel):
    j = 0
    data = []
    while j < 40:
        k = 0
        block_while(channel, GPIO.LOW)
        while GPIO.input(channel) == GPIO.HIGH:
            k += 1
            if k > 100:
                break
        if k < 8:
            data.append(0)
        else:
            data.append(1)
        j += 1
    return data

def _parse(data):
    humidity_bit = data[0:8]
    humidity_point_bit = data[8:16]
    temp_bit = data[16:24]
    temp_point_bit = data[24:32]
    check_bit = data[32:40]
    
    humidity = 0
    humidity_point = 0
    temp = 0
    temp_point = 0
    check = 0
    
    for i in range(8):
        scalar = 2 ** (7 - i)
        humidity += humidity_bit[i] * scalar
        humidity_point += humidity_point_bit[i] * scalar
        temp += temp_bit[i] * scalar
        temp_point += temp_point_bit[i] * scalar
        check += check_bit[i] * scalar
        
    tmp = humidity + humidity_point + temp + temp_point
    return temp, humidity, tmp != check



def _collect():
    channel = 7
    _setup(channel)
    while GPIO.input(channel) == GPIO.LOW:
        continue
    while GPIO.input(channel) == GPIO.HIGH:
        continue
    
    data = _get_buffer(channel)
        
    [temp, humid, error] = _parse(data)
    
    if error:
        time.sleep(0.5)
        _collect()
    else:
        return temp, humid
        
def get_weather(cb, watch=False):
    """ Results are from raw buffers and are error prone.
    Callback is used because results return unpredicatably.
    
    Optionally, the function can rerun with the same callback.
    Just specify the time to sleep between calls. >= 0

    return Celsius, humidity%
    """   
    while True:
        results = _collect()
        if results:
            cb(*results)
        if watch:
            time.sleep(watch)
        else:
            break
        
        

