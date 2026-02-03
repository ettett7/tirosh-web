import sys, os, yaml
from brain.router import LLMRouter
from brain.planner import Planner
from core.executor import Executor
from memory.memory_store import MemoryStore
from core.logger import setup_logging

class GuardianAssistant:
    def __init__(self):
        with open("config/config.yaml", 'r') as f: self.config = yaml.safe_load(f)
        setup_logging(self.config['assistant']['debug'])
        self.router = LLMRouter(self.config)
        self.planner = Planner(self.router, self.config)
        self.executor = Executor(self.config)
        self.memory = MemoryStore()

    def run(self):
        print("\n🛡️ Guardian Assistant MVP מופעל!")
        while True:
            try:
                req = input("\n🤖 Guardian> ")
                if req.lower() in ['exit', 'quit']: break
                if not req: continue
                
                plan = self.planner.create_plan(req)
                if not plan:
                    print("🤔 לא הצלחתי ליצור תוכנית פעולה.")
                    continue
                
                results = self.executor.execute_plan(plan)
                
                for res in results:
                    if res.get('success'):
                        # בדיקה אם חזרו נתוני מערכת
                        data = res.get('result', res)
                        if 'cpu' in data:
                            print(f"📊 CPU: {data['cpu']}% | Memory: {data['mem']}%")
                        else:
                            print(f"✅ הצלחתי: {res.get('description', 'בוצע')}")
                    else:
                        print(f"❌ תקלה: {res.get('error')}")
                
                self.memory.save_conversation(req, None, results, True)
            except Exception as e:
                print(f"⚠️ שגיאה: {e}")

if __name__ == "__main__":
    GuardianAssistant().run()
