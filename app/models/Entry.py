from . import model

class Entry(model):
    table = "entries"
    
    @staticmethod
    def create_entry(created_at, humidity, celsius):
        entry = Entry()

        created_hour = created_at.strftime("%Y-%m-%d %H:00:00")
        created_day = created_at.strftime("%Y-%m-%d 00:00:00")
        created_month = created_at.strftime("%Y-%m-01 00:00:00")
        created_year = created_at.strftime("%Y-01-01 00:00:00")

        entry.created_at = created_at
        entry.create_hour = created_hour
        entry.create_day = created_day
        entry.create_month = created_month
        entry.create_year = created_year
        entry.humidity = float(humidity)
        entry.celsius = float(celsius)

        return entry