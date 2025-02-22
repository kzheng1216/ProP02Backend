from enum import Enum
import json
import subprocess

TESTCASES_DIR = 'main/testcases'
TESTCASES_CASE_DIR = f"{TESTCASES_DIR}/case"
REPORT_HTML = f"{TESTCASES_DIR}/report/report.html"
REPORT_JSON = f"{TESTCASES_DIR}/report/report.json"

class ReportType(Enum):
    HTML = "html"
    JSON = "json"

class RunTestService:

    def run_tests(self, mark_type: str, report_type: str=ReportType.HTML.value):
        print("Run mark_type: ", mark_type, " report_type: ", report_type)
        command = [
            'pytest',
            TESTCASES_CASE_DIR,
            '-m', mark_type,
            f"--html={REPORT_HTML}"
        ]
        
        if report_type == ReportType.JSON.value:
            command = [
                'pytest',
                TESTCASES_CASE_DIR,
                '-m', mark_type,
                f"--json={REPORT_JSON}"
            ]
        
        result = self.run_cmd(command)
        if result.returncode != 0:
            print("Error running pytest")
            return {
                "status": "error",
                "message": "Error when running PyTest"
            }
    
        return self.result(report_type)
    
    def run_cmd(self, command):
        print("#------ command: ", command)
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("#------ result: ", result)     
        return result
    
    def result(self, report_type):
        if report_type == ReportType.JSON.value:
            with open(REPORT_JSON, 'r') as f:
                json_output = json.load(f)
                print(json.dumps(json_output, indent=4))
                return json_output
        with open(REPORT_HTML, 'r', encoding='utf-8') as file:
            html_content = file.read()
            return html_content

