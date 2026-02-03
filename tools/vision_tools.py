import pyautogui
import time
import subprocess
import os
from datetime import datetime

class VisionTools:
    def __init__(self, config):
        self.config = config

    def play_first_result(self, **kwargs):
        """מפעיל מוזיקה בספארי עם אופטימיזציה לטעינה"""
        # וודוא פוקוס על ספארי
        subprocess.run(["osascript", "-e", 'tell application "Safari" to activate'])
        time.sleep(2)
        
        # לחיצה קטנה במרכז כדי להחזיר פוקוס לחלון
        width, height = pyautogui.size()
        pyautogui.click(width/2, height/2)
        
        print("⏳ ממתין לטעינת יוטיוב (8 שניות)...")
        time.sleep(8) 
        
        print("🎹 מבצע רצף נגינה אקטיבי...")
        # ניווט קל לתוצאה הראשונה ולחיצה
        pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.press('enter') 
        
        time.sleep(5) # המתנה לטעינת הווידאו עצמו
        
        # פקודות נגינה
        pyautogui.press('k') # Play/Pause
        time.sleep(1)
        pyautogui.press('f') # Fullscreen
        
        return {"success": True, "message": "Advanced Music sequence executed"}

    def type_text(self, text):
        pyautogui.write(text, interval=0.1)
        pyautogui.press('enter')
        return {"success": True, "message": f"Typed: {text}"}
        
    def capture_screen(self, label="screenshot"):
        path = os.path.expanduser(f"~/Documents/Guardian_Screenshots/{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        pyautogui.screenshot(path)
        return {"success": True, "path": path}
