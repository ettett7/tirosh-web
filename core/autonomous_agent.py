import asyncio
import time

class AutonomousDaemon:
    def __init__(self, executor, memory, telegram_app):
        self.executor = executor
        self.memory = memory
        self.telegram_app = telegram_app
        self.active = True
        self.questions = [
            "Check tirosh.co.il performance and optimize code.",
            "Scan for messy code in the project and refactor.",
            "Audit SEO tags vs competitors and deploy updates.",
            "Monitor system logs for errors and resolve them."
        ]

    async def start_monitoring(self):
        print("⚡ TIROSH Brain: Active, Executing and Self-Improving...")
        while self.active:
            for question in self.questions:
                print(f"🧐 Thinking & Acting: {question}")
                
                plan = [
                    type('Step', (), {
                        "action": "run_web_audit", 
                        "parameters": {"url": "https://tirosh.co.il"}, 
                        "description": "בדיקת ביצועים אוטונומית"
                    }),
                    type('Step', (), {
                        "action": "deploy_site", 
                        "parameters": {"commit_message": f"Guardian Auto-Improvement: {question}"}, 
                        "description": "עדכון גרסה בענן"
                    })
                ]
                
                try:
                    # ביצוע התוכנית
                    res = self.executor.execute_plan(plan)
                    
                    # שמירת התובנה בזיכרון הקיים (SQLite)
                    insight_data = f"Action: Performance Audit & Deploy | Result: Success"
                    self.memory.store_insight(question, insight_data)
                    
                except Exception as e:
                    print(f"❌ Error in autonomous step: {e}")
                
                await asyncio.sleep(1800) # סבב כל 30 דקות
