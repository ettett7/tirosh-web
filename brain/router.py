import json
import requests

class LLMRouter:
    def __init__(self, config):
        self.config = config

    def generate(self, prompt, system_prompt=None):
        # הגדרות ה-API
        api_key = self.config['llm']['deepseek'].get('api_key', '').strip().replace('"', '')
        url = "https://api.deepseek.com/chat/completions"
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        
        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": system_prompt or "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            "stream": False
        }

        try:
            # בדיקה בענן
            response = requests.post(url, headers=headers, json=payload, timeout=15)
            
            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
            elif response.status_code == 401:
                print(f"❌ שגיאת הרשאה (401): וודא שאין רווחים במפתח והחשבון טעון בקרדיט.")
            else:
                print(f"⚠️ שגיאת API: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"🌐 בעיית חיבור לענן: {e}")

        # אם נכשלנו - עוברים למקומי
        print("🔄 עובר למודל מקומי (Ollama)...")
        try:
            local_url = f"{self.config['llm']['ollama']['base_url']}/api/generate"
            local_payload = {
                "model": self.config['llm']['ollama']['model'],
                "prompt": f"System: {system_prompt}\nUser: {prompt}",
                "stream": False
            }
            res = requests.post(local_url, json=local_payload, timeout=30)
            return res.json().get("response")
        except:
            return "מצטער איתן, גם המודל המקומי לא מגיב. וודא ש-Ollama פתוח."
