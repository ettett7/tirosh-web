import psutil, platform
class SystemTools:
    def get_system_info(self):
        return {"success": True, "cpu": psutil.cpu_percent(), "mem": psutil.virtual_memory().percent}
