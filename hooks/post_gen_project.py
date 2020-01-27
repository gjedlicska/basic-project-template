import subprocess
import sys


def install_pre_commit_script():
    print("Pre-commit init")
    subprocess.run(["pre-commit", "install"], capture_output=True)
    subprocess.run(["pre-commit", "run", "--all-files"], capture_output=True)


def init_git_repo():
    print("Git init")
    subprocess.run(["git", "init"], capture_output=True)
    subprocess.run(["git", "flow", "init", "-d"], capture_output=True)


def init_project_venv():
    print("Poetry init")
    subprocess.run(["poetry", "install"])


try:
    print("Starting post-generation script.")
    init_git_repo()
    install_pre_commit_script()
    init_project_venv()
    print("Finished pre-generation script.")

    sys.exit(0)

except Exception as ex:
    print(str(ex))
    sys.exit(1)
