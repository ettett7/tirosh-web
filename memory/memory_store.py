import sqlite3
import json
from datetime import datetime

class MemoryStore:
    def __init__(self, db_path="memory/guardian_os.db"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self._init_db()

    def _init_db(self):
        cursor = self.conn.cursor()
        # טבלת חוויות (מה קרה)
        cursor.execute('''CREATE TABLE IF NOT EXISTS episodes 
            (id INTEGER PRIMARY KEY, request TEXT, plan TEXT, result TEXT, success BOOLEAN, timestamp DATETIME)''')
        # טבלת למידה (תובנות לשיפור עצמי)
        cursor.execute('''CREATE TABLE IF NOT EXISTS insights 
            (id INTEGER PRIMARY KEY, pattern TEXT, advice TEXT, success_rate REAL)''')
        self.conn.commit()

    def store_episode(self, request, plan, result, success):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO episodes (request, plan, result, success, timestamp) VALUES (?, ?, ?, ?, ?)",
                       (request, json.dumps(plan), json.dumps(result), success, datetime.now()))
        self.conn.commit()
        # אם נכשלנו, נרשום לעצמנו ללמוד מזה
        if not success:
            self._update_insights(request, "Failed execution - logic check needed")

    def _update_insights(self, pattern, advice):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO insights (pattern, advice, success_rate) VALUES (?, ?, ?)", (pattern, advice, 0.0))
        self.conn.commit()

    def get_context_for_brain(self):
        # מחזיר את 5 הפעולות האחרונות כדי שה-AI ידע איפה הוא אוחז
        cursor = self.conn.cursor()
        cursor.execute("SELECT request, success FROM episodes ORDER BY timestamp DESC LIMIT 5")
        history = cursor.fetchall()
        return "\n".join([f"Req: {h[0]} (Success: {h[1]})" for h in history])
