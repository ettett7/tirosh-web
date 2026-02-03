import requests
import json

class LLMRouter:
    def __init__(self, config):
        self.config = config

    def generate(self, prompt, system_prompt=None):
        """מנתב את הבקשה ל-DeepSeek Cloud או ל-Ollama מקומי"""
        try:
            url = f"{self.config['llm']['deepseek']['base_url']}/chat/completions"
            headers = {
                "Authorization": f"Bearer {self.config['llm']['deepseek']['api_key']}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "deepseek-chat",
                "messages": [
                    {"role": "system", "content": system_prompt or "You are Guardian-OS."},
                    {"role": "user", "content": prompt}
                ],
                "stream": False
            }
            response = requests.post(url, headers=headers, json=payload, timeout=15)
            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"Cloud Router Error: {e}")

        # Fallback ל-Ollama אם הענן לא זמין
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
            return "איתן, המוח שלי לא זמין כרגע. וודא ש-Ollama עובד או שיש אינטרנט."
