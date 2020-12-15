from .DH11 import get_weather
from app.models.Entry import Entry
import datetime

last = None

def insert():
    print("trying to insert")
    if last:
        [celsius, humidity] = last
        entry = Entry()
        now = datetime.datetime.now()
        entry = Entry.create_entry(now, humidity, celsius)
        res = entry.insert()
        print("inserted")
        return res

def on_results(celsius, humidity):
    global last
    last = (celsius, humidity)
    
def run():
    get_weather(on_results)
    return last

if __name__ == "__main__":
    get_weather(on_results, True)