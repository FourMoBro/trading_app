"""
Creates Database
"""

import psycopg2
import config

connection = psycopg2.connect(config.DB_FILE)

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS stock (
        id INTEGER PRIMARY KEY, 
        symbol TEXT NOT NULL UNIQUE, 
        name TEXT NOT NULL,
        exchange TEXT NOT NULL,
        shortable BOOLEAN NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS stock_price (
        id INTEGER PRIMARY KEY, 
        stock_id INTEGER,
        date DATE NOT NULL,
        open NUMERIC NOT NULL, 
        high NUMERIC NOT NULL, 
        low NUMERIC NOT NULL, 
        close NUMERIC NOT NULL, 
        volume NUMERIC NOT NULL,
        sma_20 NUMERIC,
        sma_50 NUMERIC,
        rsi_14 NUMERIC,
        FOREIGN KEY (stock_id) REFERENCES stock (id)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS strategy (
        id INTEGER PRIMARY KEY, 
        name TEXT NOT NULL UNIQUE
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS stock_strategy (
        stock_id INTEGER NOT NULL,
        strategy_id INTEGER NOT NULL,
        FOREIGN KEY (stock_id) REFERENCES stock (id),
        FOREIGN KEY (strategy_id) REFERENCES strategy (id)
    )
""")

strategies = ['opening_range_breakout', 'opening_range_breakdown', 'bollinger_bands']

# # TODO - Make sure duplicates are not added into strategy Table
# for strategy in strategies:
#     cursor.execute("""
#         INSERT INTO strategy (name) VALUES (?)
#     """, (strategy, ))

connection.commit()