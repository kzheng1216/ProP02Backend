from main.cmd.exec_wsl_cmd import run_wsl_command
from main.utils.singleton import singleton


@singleton
class CmdService:

    def run_cmd(self, command: str):
        if not command:
            return "Command is empty"
        output = self.run_wsl_cmd(command)
        return output

    def run_wsl_cmd(self, command: str):
        # command = "ansible-playbook /home/mystic/ansible_test/playbook_exec_shell.yml"
        output = run_wsl_command(command)
        if output:
            print("WSL 命令输出：")
            print(output)
        return output