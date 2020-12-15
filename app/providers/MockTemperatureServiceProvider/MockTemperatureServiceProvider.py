import time
import random
from app.models.Entry import Entry
import datetime

last = None

def insert():
    print("trying insert")
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
    time.sleep(random.randint(2, 5))
    data = [random.randint(14,26), random.randint(20,36)]
    on_results(*data)
    print(data)

if __name__ == "__main__":
    while True:
        run()