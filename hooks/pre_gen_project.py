import re
import sys
import subprocess

def validate_project_name(project_name: str):
    valid_regex = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

    if not re.match(valid_regex, project_name):
        raise ValueError(f"ERROR: {project_name} is not a valid Python module name!")


def _convert_comletion_result_to_str(completion: subprocess.CompletedProcess) -> str:
    decoded = completion.stdout.decode("UTF-8") 
    return decoded.replace("\n", "")


def ensure_python_3():
    completion = subprocess.run(["python", "--version"], capture_output=True)
    pyhon_version = _convert_comletion_result_to_str(completion)

    if "Python 3." not in pyhon_version:
        raise ValueError(f"Python 3 is reqiured, you have {python_version}")

    print(f"Found suitable starting point with {pyhon_version}")


def ensure_pip():

    upgrade = subprocess.run(["python", "-m", "pip", "install", "-U", "pip"])
    completion = subprocess.run(["pip", "--version"], capture_output=True)

    print(f"Upgraded pip to {_convert_comletion_result_to_str(completion)}")



def ensure_pipx():
    try:
        completion = subprocess.run(["pipx", "--version"], capture_output=True)

    except FileNotFoundError as fn:
        print("Pipx is not installed, taking care of it...")
        completion = subprocess.run(["python", "-m", "pip", "install", "--user", "pipx"], capture_output=True)
        completion = subprocess.run(["python", "-m", "pipx", "ensurepath"], capture_output=True)


    finally:
        completion = subprocess.run(["pipx", "--version"], capture_output=True)
        print(f"You have pipx installed with version {_convert_comletion_result_to_str(completion)}")


def ensure_poetry():
    try:
        completion = subprocess.run(["poetry", "--version"], capture_output=True)

    except FileNotFoundError as fn:
        print("Poetry is not installed, taking care of it...")
        completion = subprocess.run(["pipx", "install", "poetry"], capture_output=True)

        completion = subprocess.run(["poetry", "--version"], capture_output=True)
        print(completion.returncode)


    finally:
        completion = subprocess.run(["poetry", "--version"], capture_output=True)
        print(f"You have {_convert_comletion_result_to_str(completion)} installed")


def ensure_dependecies():
    try:
        print("Ensuring you have required dependecies to bootstrap a new project.")
        ensure_python_3()
        ensure_pip()
        ensure_pipx()
        ensure_poetry()
        print("All set")

    except Exception as ex:
        print("Failed to setup dependencies")
        raise ex
    


project_name = "{{ cookiecutter.project_name }}"

try:
    print("Starting pre-generation stript.")
    
    validate_project_name(project_name)
    ensure_dependecies()


    # raise ValueError("dont create")
    print("Finished pre-generation stript.")
    sys.exit(0)

except Exception as ex:
    print(str(ex))
    sys.exit(1)
