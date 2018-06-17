import subprocess

def run_command(cmd):
    cmd = cmd.split()
    new_cmd = []
    for word in cmd:
        new_cmd.append(str(word))
    result = subprocess.check_output([new_cmd])
    print(result)

run_command("git")
