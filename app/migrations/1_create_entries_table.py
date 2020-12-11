def up():
    return ("""
        CREATE TABLE entries (
            created_at DATETIME UNIQUE,
            humidity FLOAT,
            celsius FLOAT
        )
    """)

def down():
    return ("""
    DROP TABLE IF EXISTS entries
    """)
