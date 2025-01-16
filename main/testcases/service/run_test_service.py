import json
import subprocess

TESTCASES_DIR = 'main/testcases'
TESTCASES_CASE_DIR = f"{TESTCASES_DIR}/case"
TESTCASES_REPORT = TESTCASES_DIR + '/report/report.html'
RESULTS_FILE = '.report.json'


class RunTestService:

    def run_tests(self, mark_type: str):
        print("Run mark_type: ", mark_type)
        # command = ['pytest', '--html='+TESTCASES_REPORT, TESTCASES_DIR, '-m', mark_type]
        command = ['pytest', TESTCASES_CASE_DIR, '-m', mark_type, f"--json-report"]
        print('Command: ', command)

        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("result: ", result)
        if result.returncode != 0:
            print("Error running pytest")
            return {
                "status": "error",
                "message": "Error running pytest"
            }

        with open(RESULTS_FILE, 'r') as f:
            json_output = json.load(f)
            print("JSON报告:")
            print(json.dumps(json_output, indent=4))
            return json_output
