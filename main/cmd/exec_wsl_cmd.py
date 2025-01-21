import subprocess


def run_wsl_command(command):
    """
    在 WSL 中运行命令并返回输出。
    :param command: 要在 WSL 中运行的命令（字符串或列表形式）
    :return: 命令的输出结果
    """
    # 构造完整的 WSL 命令
    if isinstance(command, str):
        full_command = f"wsl {command}"
    else:
        full_command = ["wsl"] + command

    try:
        # 使用 subprocess.run 执行命令
        result = subprocess.run(full_command, capture_output=True, text=True, check=True)
        return result.stdout.strip()  # 返回命令的输出
    except subprocess.CalledProcessError as e:
        print(f"命令执行失败: {e}")
        return None

# 示例：运行一个简单的 WSL 命令
if __name__ == "__main__":
    command = "ansible-playbook /home/mystic/ansible_test/playbook_exec_shell.yml"  # 示例命令：列出 Linux 根目录的内容
    output = run_wsl_command(command)
    if output:
        print("WSL 命令输出：")
        print(output)