import subprocess
import os

class TerminalTools:
    def __init__(self, config):
        self.config = config

    def execute_and_solve(self, command):
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return {"success": result.returncode == 0, "output": result.stdout, "error": result.stderr}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def deploy_to_tirosh(self, commit_message="Performance Optimization by Guardian"):
        """מעלה את השינויים ל-GitHub כדי שהאתר יתעדכן בלייב"""
        commands = [
            "git add .",
            f'git commit -m "{commit_message}"',
            "git push origin main"
        ]
        results = []
        for cmd in commands:
            res = self.execute_and_solve(cmd)
            results.append(res)
            if not res["success"]: break
        return {"success": all(r["success"] for r in results), "log": results}

    def update_system_code(self, file_path, new_content):
        try:
            with open(file_path, 'w') as f:
                f.write(new_content)
            return {"success": True, "message": f"Updated code in {file_path}"}
        except Exception as e:
            return {"success": False, "error": str(e)}
