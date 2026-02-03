import subprocess
import urllib.parse
import time

class AppTools:
    def __init__(self, config):
        self.config = config

    def open_app(self, app_name, url=None, search_query=None):
        """פתיחה כירורגית בספארי בלבד"""
        # אם יש שאילתת חיפוש, נבנה לינק ישיר לתוצאה הראשונה ביוטיוב
        if search_query:
            encoded_query = urllib.parse.quote(search_query)
            target_url = f"https://www.youtube.com/results?search_query={encoded_query}"
            print(f"🚀 Opening Safari with query: {search_query}")
            subprocess.run(["open", "-a", "Safari", target_url])
            return {"success": True, "message": "Safari opened with search"}
            
        if url:
            subprocess.run(["open", "-a", "Safari", url])
            return {"success": True, "message": "Opening URL in Safari"}
            
        subprocess.run(["open", "-a", "Safari"])
        return {"success": True, "message": "Safari Activated"}
