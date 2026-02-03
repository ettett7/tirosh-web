import os

class CodeTools:
    def __init__(self, config):
        self.config = config
        self.project_path = "tirosh_web"

    def audit_tirosh_code(self, **kwargs):
        """סורק את קבצי האתר של תירוש ומחפש שיפורי ביצועים"""
        if not os.path.exists(self.project_path):
            return {"success": False, "error": f"Directory {self.project_path} not found. Run mkdir first."}
            
        findings = []
        for root, dirs, files in os.walk(self.project_path):
            for file in files:
                if file.endswith((".jsx", ".js")):
                    with open(os.path.join(root, file), 'r') as f:
                        content = f.read()
                        # האקינג של ביצועים: בדיקה אם יש Lazy Loading
                        if "lazy" not in content.lower() and "Suspense" not in content:
                            findings.append(f"Performance Optimization needed in {file}: Missing Suspense/Lazy.")
                        # בדיקת SEO
                        if "Helmet" not in content and "Index" in file:
                            findings.append(f"SEO Warning in {file}: Missing Metadata/Helmet.")
        
        return {
            "success": True, 
            "findings": findings if findings else ["Code is high-performance and SEO ready!"],
            "description": "Code Audit for TIROSH"
        }

    def write_pine_script(self, script_name, content):
        """שמירת קבצי Pine Script לטריידינג"""
        path = os.path.expanduser(f"~/Documents/Guardian_Scripts/{script_name}.pine")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            f.write(content)
        return {"success": True, "path": path}
