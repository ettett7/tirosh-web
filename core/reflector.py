import json
import logging

class Reflector:
    def __init__(self, memory):
        self.memory = memory
        self.logger = logging.getLogger(__name__)

    def analyze_and_improve(self, request, logs, success):
        """מנתח הצלחות וכישלונות כדי לשפר את ה-Prompt העתידי"""
        insight = {
            "timestamp": str(self.memory.conn.execute("SELECT datetime('now')").fetchone()[0]),
            "request": request,
            "success": success,
            "lesson": "Analysis of logs suggests optimization needed" if not success else "Path successful"
        }
        
        # שמירת התובנה בבסיס הנתונים
        cursor = self.memory.conn.cursor()
        cursor.execute("INSERT INTO insights (pattern, advice, success_rate) VALUES (?, ?, ?)", 
                       (request, f"Lesson from logs: {str(logs[-1:])}", 1.0 if success else 0.0))
        self.memory.conn.commit()
        
        return insight
