import asyncio
import time

class AutonomousDaemon:
    def __init__(self, executor, memory, telegram_app):
        self.executor = executor
        self.memory = memory
        self.telegram_app = telegram_app
        self.active = True
        self.questions = [
            "Perform Technical Audit on tirosh.co.il",
            "Optimize Index.jsx for performance",
            "Update SEO metadata in GitHub"
        ]

    async def start_monitoring(self):
        print("⚡ TIROSH Brain: High-Performance Mode (No Music Loop)")
        while self.active:
            for question in self.questions:
                # הזרקה ישירה של פקודות טכניות בלבד
                plan = [
                    type('Step', (), {"action": "run_web_audit", "parameters": {"url": "https://tirosh.co.il"}, "description": "Technical Audit"}),
                    type('Step', (), {"action": "deploy_site", "parameters": {"commit_message": "Guardian: Technical Optimization"}, "description": "Cloud Update"})
                ]
                self.executor.execute_plan(plan)
                self.memory.store_insight(question, "Task executed without music interference")
                await asyncio.sleep(1800)
