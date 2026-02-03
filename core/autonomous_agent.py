import asyncio
import time
from core.brain_memory import BrainMemory

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
                        "description": "Running Performance Audit"
                    }),
                    type('Step', (), {
                        "action": "deploy_site", 
                        "parameters": {"commit_message": f"Guardian Auto-Improvement: {question}"}, 
                        "description": "Deploying improvements to GitHub"
                    })
                ]
                
                res = self.executor.execute_plan(plan)
                self.memory.record_learning(question, "Performance Audit & Deploy", "Success")
                
                await asyncio.sleep(1800)
