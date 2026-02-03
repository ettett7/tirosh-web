import os

class KnowledgeTools:
    def __init__(self, config):
        self.config = config
        self.scripts_dir = os.path.expanduser("~/Documents/Guardian_Scripts")

    def read_existing_scripts(self):
        """סורק את כל קבצי ה-Pine Script ומחזיר את התוכן שלהם לניתוח"""
        if not os.path.exists(self.scripts_dir):
            return {"success": False, "error": "No scripts directory found"}
        
        scripts_summary = []
        for file in os.listdir(self.scripts_dir):
            if file.endswith(".pine"):
                with open(os.path.join(self.scripts_dir, file), 'r') as f:
                    content = f.read()
                    scripts_summary.append(f"File: {file}\nContent: {content[:500]}...") # לוקח התחלה לניתוח
        
        return {"success": True, "scripts": scripts_summary, "count": len(scripts_summary)}
