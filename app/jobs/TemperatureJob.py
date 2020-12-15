import time
import threading

try:
    import app.providers.TemperatureServiceProvider as Service
except ModuleNotFoundError:
    import app.providers.MockTemperatureServiceProvider as Service

stop_threads = False


def thread_func():
    """ Count half seconds"""
    while True:
        global stop_threads
        
        Service.run()
        time.sleep(0.5)
        
        if stop_threads: 
            break

thread = threading.Thread(target = thread_func)

def job():
    Service.insert()

def make(schedule):
    schedule.every(30).seconds.do(job)
    thread.start()

def destroy():
    global stop_threads
    stop_threads = True
    thread.join()