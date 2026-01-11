import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    working_dir_abs = os.path.abspath(working_directory)
    file_path_abs = os.path.abspath(os.path.join(working_dir_abs, file_path))

    if not os.path.commonpath([working_dir_abs, file_path_abs]) == working_dir_abs:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(file_path_abs):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    
    if not file_path_abs.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file'
    
    command = ["python", file_path_abs]
    if args:
        command.extend(args)
    completed_process = subprocess.run(command, cwd=working_dir_abs, text=True, capture_output=True, timeout=30)
    if completed_process.returncode != 0:
        return f"Process exited with code {completed_process.returncode}"
    if not completed_process.stdout and not completed_process.stderr:
        return f"No output produced"
    return f"STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file in the specified path",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path of the file to run, relative to the working directory (default is the working directory itself)",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="Optional arguments to add to the running of the file",
            ),
        },
    ),
)