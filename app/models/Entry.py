from . import model
from datetime import datetime, timedelta
from app.helpers import floor_date

class Entry(model):
    table = "entries"
    
    @staticmethod
    def create_entry(created_at, humidity, celsius):
        entry = Entry()
        entry.created_at = created_at
        entry.create_5minute = floor_date(created_at, minutes=5)
        entry.create_hour = floor_date(created_at, hours=1)
        entry.create_day = floor_date(created_at, days=1)
        entry.create_month = floor_date(created_at, days=30)
        entry.create_year = floor_date(created_at, days=365)
        entry.humidity = float(humidity)
        entry.celsius = float(celsius)

        return entry