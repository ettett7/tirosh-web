import json
import os

class BrainMemory:
    def __init__(self, file_path="brain_memory.json"):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump({"insights": [], "actions_taken": 0}, f)

    def record_learning(self, question, action_summary, result):
        with open(self.file_path, 'r+') as f:
            data = json.load(f)
            data["insights"].append({
                "question": question,
                "action": action_summary,
                "result": result,
                "timestamp": time.time()
            })
            data["actions_taken"] += 1
            f.seek(0)
            json.dump(data, f, indent=4)
