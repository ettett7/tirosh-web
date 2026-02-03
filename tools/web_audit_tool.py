import subprocess
import json
import os

class WebAuditTool:
    def __init__(self, config):
        self.config = config

    def run_performance_check(self, url="https://tirosh.co.il"):
        """מריץ בדיקת Lighthouse ושולח דו"ח ביצועים"""
        print(f"🚀 Analyzing Tirosh Performance: {url}")
        report_path = os.path.expanduser("~/Documents/tirosh_audit.json")
        
        # הרצת Lighthouse מהטרמינל
        cmd = f"lighthouse {url} --output json --output-path {report_path} --chrome-flags='--headless'"
        subprocess.run(cmd, shell=True, capture_output=True)
        
        if os.path.exists(report_path):
            with open(report_path, 'r') as f:
                data = json.load(f)
                score = data['categories']['performance']['score'] * 100
                return {"success": True, "score": score, "message": f"Tirosh Perf Score: {score}%"}
        return {"success": False, "error": "Audit failed"}
