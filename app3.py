import sqlite3

conn = sqlite3.connect("data.yttomp3")

query = conn.execute('''
CREATE TABLE `data` (
    file_sno INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id TEXT NOT NULL,
    youtube_itag TEXT NOT NULL,
    youtube_url TEXT NOT NULL
)

''')

conn.close()