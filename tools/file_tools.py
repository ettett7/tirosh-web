import os, shutil, logging
from pathlib import Path
class FileTools:
    def __init__(self, config):
        self.config = config
        self.downloads_path = os.path.expanduser(config['system']['downloads_folder'])
    def organize_downloads(self):
        downloads = Path(self.downloads_path)
        categories = {"Images": [".jpg", ".png", ".jpeg"], "Documents": [".pdf", ".docx", ".txt"], "Code": [".py", ".js"]}
        moved = 0
        for file in downloads.iterdir():
            if file.is_file() and not file.name.startswith('.'):
                for cat, exts in categories.items():
                    if file.suffix.lower() in exts:
                        (downloads / cat).mkdir(exist_ok=True)
                        shutil.move(str(file), str(downloads / cat / file.name))
                        moved += 1
                        break
        return {"success": True, "message": f"Organized {moved} files"}
    def create_folder(self, path, folder_name):
        full_path = Path(os.path.expanduser(path)) / folder_name
        full_path.mkdir(exist_ok=True, parents=True)
        return {"success": True, "path": str(full_path)}
