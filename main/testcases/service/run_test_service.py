from enum import Enum
import json
import os
import subprocess

TESTCASES_DIR = os.path.join('main', 'testcases')
TESTCASES_CASE_DIR = os.path.join(TESTCASES_DIR, 'case')
TESTCASES_REPORT_DIR = os.path.join(TESTCASES_DIR, 'report')
REPORT_HTML = os.path.join(TESTCASES_REPORT_DIR, 'report.html')
REPORT_JSON = os.path.join(TESTCASES_REPORT_DIR, 'report.json')
TESTCASES_RESULTS_DIR = os.path.join(TESTCASES_DIR, 'results')
TESTCASES_ALLURE_REPORT_DIR = os.path.join(TESTCASES_DIR, 'allure-report')

class ReportType(Enum):
    HTML = "html"
    JSON = "json"

class RunTestService:
    
    def run_cmd(self, command):
        print("#------ command: ", command)
        result = subprocess.run(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("#------ result: ", result)
        return result
    
    def run_tests(self, mark_type: str, report_type: str=ReportType.HTML.value):
        print("Run mark_type: ", mark_type, " report_type: ", report_type)
        command = [
            'pytest',
            TESTCASES_CASE_DIR,           
            f"--html={REPORT_HTML}",
            f"--alluredir={TESTCASES_RESULTS_DIR}",
            '-m', mark_type
        ]
        
        if report_type == ReportType.JSON.value:
            command = [
                'pytest',
                TESTCASES_CASE_DIR,            
                f"--json={REPORT_JSON}",
                f"--alluredir={TESTCASES_RESULTS_DIR}",
                '-m', mark_type
            ]
        # allure generate temps --clean -o allure-report
        result = self.run_cmd(command)
        if result.returncode != 0:
            print("Error running pytest")
            return {
                "status": "error",
                "message": "Error when running PyTest"
            }
            
        #-- Optional preocess: Generate allure report
        self.generate_allure_report()
           
        result_data = self.handle_result(report_type)        
        return result_data
    
    def handle_result(self, report_type):
        if report_type == ReportType.JSON.value:
            with open(REPORT_JSON, 'r') as f:
                json_output = json.load(f)
                print(json.dumps(json_output, indent=4))
                return json_output
        with open(REPORT_HTML, 'r', encoding='utf-8') as file:
            html_content = file.read()
            return html_content
        
    def generate_allure_report(self):
        # allure generate temps --clean -o allure-report
        self.run_cmd([
            'allure',
            'generate',
            TESTCASES_RESULTS_DIR,
            '--clean',
            '-o', TESTCASES_ALLURE_REPORT_DIR
        ])
        # Run this command in path: /Users/zys/myworkspace/ProP02Backend/main/testcases to view allure report
        # allure open allure-report
