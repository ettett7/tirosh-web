import sqlite3
import json
import os

class MemoryManager:
    def __init__(self, db_path="brain/guardian_memory.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        # טבלה לשיחות
        cursor.execute('''CREATE TABLE IF NOT EXISTS history 
                          (id INTEGER PRIMARY KEY, role TEXT, content TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        # טבלה לתובנות על איתן ועל תירוש
        cursor.execute('''CREATE TABLE IF NOT EXISTS insights 
                          (key TEXT PRIMARY KEY, value TEXT)''')
        conn.commit()
        conn.close()

    def store_message(self, role, content):
        conn = sqlite3.connect(self.db_path)
        conn.execute("INSERT INTO history (role, content) VALUES (?, ?)", (role, content))
        conn.commit()
        conn.close()

    def get_context_for_brain(self, limit=10):
        """שולף את השיחות האחרונות כדי שה-LLM יבין על מה מדובר"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT role, content FROM history ORDER BY id DESC LIMIT ?", (limit,))
        rows = cursor.fetchall()
        conn.close()
        
        context = ""
        for role, content in reversed(rows):
            context += f"{role}: {content}\n"
        return context

    def store_insight(self, key, value):
        conn = sqlite3.connect(self.db_path)
        conn.execute("INSERT OR REPLACE INTO insights (key, value) VALUES (?, ?)", (key, value))
        conn.commit()
        conn.close()
