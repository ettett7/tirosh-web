import asyncio
import logging
from telegram.ext import ApplicationBuilder, MessageHandler, filters
from core.executor import Executor
from brain.planner import Planner
from brain.llm_router import LLMRouter
from brain.memory_manager import MemoryManager
from core.autonomous_agent import AutonomousDaemon
import yaml

class GuardianOS:
    def __init__(self):
        with open("config/config.yaml", "r") as f:
            self.config = yaml.safe_load(f)
        
        self.llm = LLMRouter(self.config)
        self.memory = MemoryManager()
        self.planner = Planner(self.llm, self.config)
        self.executor = Executor(self.config)

    async def start_daemon(self, app):
        """הפעלת המנוע האוטונומי של תירוש"""
        self.daemon = AutonomousDaemon(self.executor, self.memory, app)
        # הפעלה כמשימה נפרדת שלא חוסמת את הבוט
        asyncio.create_task(self.daemon.start_monitoring())
        print("🚀 TIROSH Autonomous Engine is LIVE")

    async def handle_message(self, update, context):
        user_msg = update.message.text
        mem_context = self.memory.get_context_for_brain()
        
        answer, plan = self.planner.create_plan(user_msg, mem_context)
        await update.message.reply_text(answer)
        
        if plan:
            results = self.executor.execute_plan(plan)
            # שליחת תוצאות (צילומי מסך וכו')
            for res in results:
                if res.get('success') and 'path' in res:
                    await update.message.reply_photo(photo=open(res['path'], 'rb'))
                elif not res.get('success'):
                    await update.message.reply_text(f"❌ שגיאה: {res.get('error')}")

if __name__ == '__main__':
    guardian = GuardianOS()
    token = "8352539237:AAHJmvfoPoDFylR96rE5q1t0imgafadIpaQ"
    app = ApplicationBuilder().token(token).build()
    
    # חיבור הדימון ללופ של הבוט
    loop = asyncio.get_event_loop()
    loop.create_task(guardian.start_daemon(app))
    
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), guardian.handle_message))
    print("🚀 Guardian-OS v4 (Full Integration) is LIVE")
    app.run_polling()
