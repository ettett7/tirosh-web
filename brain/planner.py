import json, re, os
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class PlanStep:
    action: str
    parameters: Dict[str, Any]
    description: str

class Planner:
    def __init__(self, llm_router, config):
        self.llm = llm_router
        self.config = config

    def load_context(self):
        try:
            if os.path.exists("brain/context.json"):
                with open("brain/context.json", "r") as f:
                    return json.load(f)
        except: pass
        return {}

    def create_plan(self, user_request, memory_context=""):
        user_data = self.load_context()
        system_prompt = f"""You are Guardian-OS, the elite performance partner for {user_data.get('user_name', 'Eitan')}.
        Brand: {user_data.get('brand_name', 'Tirosh')}.
        
        STRICT JSON RULES:
        - Use action "run_web_audit" for site checks.
        - Use "open_app" (Safari) + "press_play" for music.
        - NEVER output text outside the JSON.
        
        JSON Structure:
        {{
            "answer": "Hebrew response",
            "plan": [
                {{"action": "action_name", "parameters": {{}}, "description": "desc"}}
            ]
        }}"""
        
        response = self.llm.generate(user_request, system_prompt)
        try:
            json_match = re.search(r'\{.*\}', response, re.DOTALL)
            if not json_match:
                raise ValueError("No JSON found")
            
            data = json.loads(json_match.group())
            steps = [PlanStep(s['action'], s.get('parameters', {}), s.get('description', '')) for s in data.get("plan", [])]
            return data.get("answer", "מבצע..."), steps
        except Exception as e:
            print(f"❌ Error: {e} | Raw: {response}")
            return "איתן, המוח שלי קצת הסתבך, בוא ננסה שוב פשוט יותר.", []
