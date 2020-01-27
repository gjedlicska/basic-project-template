import re
import subprocess
import sys


def validate_project_name(project_name: str):
    valid_regex = r"^[_a-zA-Z][_a-zA-Z0-9 ]+$"

    if not re.match(valid_regex, project_name):
        raise ValueError(f"ERROR: {project_name} is not a valid Python module name!")


def _convert_completion_result_to_str(completion: subprocess.CompletedProcess) -> str:
    decoded = completion.stdout.decode("UTF-8")
    return decoded.replace("\n", "")


def ensure_python_3():

    completion = subprocess.run(["python", "--version"], capture_output=True)
    python_version = _convert_completion_result_to_str(completion)

    if "Python 3." not in python_version:
        raise ValueError(f"Python 3 is required, you have {python_version}")

    print(f"Found suitable starting point with {python_version}")


def ensure_pip():

    subprocess.run(["python", "-m", "pip", "install", "-U", "pip"])
    completion = subprocess.run(["pip", "--version"], capture_output=True)

    print(f"Upgraded pip to {_convert_completion_result_to_str(completion)}")


def ensure_pipx():
    try:
        subprocess.run(["pipx", "--version"], capture_output=True)

    except FileNotFoundError:
        print("Pipx is not installed, taking care of it...")
        subprocess.run(
            ["python", "-m", "pip", "install", "--user", "pipx"], capture_output=True
        )
        subprocess.run(["python", "-m", "pipx", "ensurepath"], capture_output=True)

    finally:
        completion = subprocess.run(["pipx", "--version"], capture_output=True)
        print(
            f"You have pipx installed with version "
            f"{_convert_completion_result_to_str(completion)}"
        )


def ensure_poetry():
    try:
        subprocess.run(["poetry", "--version"], capture_output=True)
        subprocess.run(["pipx", "upgrade" "poetry"], capture_output=True)

    except FileNotFoundError:
        print("Poetry is not installed, taking care of it...")
        subprocess.run(["pipx", "install", "poetry"], capture_output=True)

    finally:
        completion = subprocess.run(["poetry", "--version"], capture_output=True)
        print(f"You have {_convert_completion_result_to_str(completion)} installed")


def ensure_pre_commit():
    try:
        subprocess.run(["pre-commit", "--version"], capture_output=True)
        subprocess.run(["pipx", "upgrade" "pre-commit"], capture_output=True)

    except FileNotFoundError:
        print("Pre-commit is not installed, taking care of it...")
        subprocess.run(["pipx", "install", "pre-commit"], capture_output=True)

    finally:
        completion = subprocess.run(["pre-commit", "--version"], capture_output=True)
        print(f"You have {_convert_completion_result_to_str(completion)} installed")


def ensure_dependencies():
    try:
        print("Ensuring you have required dependencies to bootstrap a new project.")
        ensure_python_3()
        ensure_pip()
        ensure_pipx()
        ensure_poetry()
        ensure_pre_commit()
        print("All set")

    except Exception as exc:
        print("Failed to setup dependencies")
        raise exc


project_name = "{{ cookiecutter.project_name }}"

try:
    print("Starting pre-generation script.")

    validate_project_name(project_name)
    ensure_dependencies()

    # raise ValueError("dont create")
    print("Finished pre-generation script.")
    sys.exit(0)

except Exception as ex:
    print(str(ex))
    sys.exit(1)
