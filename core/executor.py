from tools.file_tools import FileTools
from tools.app_tools import AppTools
from tools.system_tools import SystemTools
from tools.code_tools import CodeTools
from tools.vision_tools import VisionTools
from tools.web_audit_tool import WebAuditTool
from tools.terminal_tools import TerminalTools
import os

class Executor:
    def __init__(self, config):
        self.config = config
        self.file_tools = FileTools(config)
        self.app_tools = AppTools(config)
        self.system_tools = SystemTools()
        self.code_tools = CodeTools(config)
        self.vision_tools = VisionTools(config)
        self.web_audit = WebAuditTool(config)
        self.terminal = TerminalTools(config)
        
        self.tools = {
            "open_app": self.app_tools.open_app,
            "write_pine_script": self.code_tools.write_pine_script,
            "audit_code": self.code_tools.audit_tirosh_code,
            "capture_screen": self.vision_tools.capture_screen,
            "press_play": self.vision_tools.play_first_result,
            "get_system_info": self.system_tools.get_system_info,
            "run_web_audit": self.web_audit.run_performance_check,
            "terminal_cmd": self.terminal.execute_and_solve,
            "update_code": self.terminal.update_system_code, "deploy_site": self.terminal.deploy_to_tirosh
        }

    def execute_plan(self, steps):
        results = []
        for step in steps:
            if step.action in self.tools:
                try:
                    res = self.tools[step.action](**step.parameters)
                    res['description'] = step.description
                    results.append(res)
                except Exception as e:
                    results.append({"success": False, "error": str(e)})
        return results
