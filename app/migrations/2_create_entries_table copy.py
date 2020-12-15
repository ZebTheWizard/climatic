def up():
    return [
        "ALTER TABLE entries ADD COLUMN create_5minute DATETIME",
        "ALTER TABLE entries ADD COLUMN create_hour DATETIME",
        "ALTER TABLE entries ADD COLUMN create_day DATETIME",
        "ALTER TABLE entries ADD COLUMN create_month DATETIME",
        "ALTER TABLE entries ADD COLUMN create_year DATETIME",
    ]

def down():
    return None
