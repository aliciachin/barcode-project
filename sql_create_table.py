# Create test database

import sqlite3

conn = sqlite3.connect('barcode.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE sample(
        id INTEGER,
        item VARCHAR,
        category VARCHAR,
        quantity REAL,
        unit VARCHAR,
        expiry_date DATE,
        date_added DATETIME,
        last_updated DATETIME
        );''')

c.execute('''
    INSERT INTO sample VALUES
        ('12345678','item1','category1','100','ml','2000-01-01','2000-01-01 10:00:00','2000-01-01 10:00:05'),
        ('87654321','item2','category2','300','g','2000-01-20','2000-01-05 10:00:00','2000-01-07 10:00:00'),
        ('19273618','item3','category3','250','ml','2000-01-10','2000-01-02 10:00:00','2000-01-02 10:00:00')
        ;''')

conn.commit()



conn.close()
