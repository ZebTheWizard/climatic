from .DH11 import get_weather

last = None

def insert():
    if last:
        [celsius, humidity] = last
        entry = Entry()
        now = datetime.datetime.now()
        entry = Entry.create_entry(now, humidity, celsius)

        return entry.insert()

def on_results(celsius, humidity):
    global last
    last = (celsius, humidity)
    
def run():
    get_weather(on_results)