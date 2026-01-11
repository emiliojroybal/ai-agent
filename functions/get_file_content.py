import config
import os
from google.genai import types

def get_file_content(working_directory, file_path):
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    if not os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    with open(target_file, 'r') as file:
        file_content_string = file.read(config.MAX_CHARS)
        if file.read(1):
            file_content_string += f'[...File "{file_path}" truncated at {config.MAX_CHARS} characters]'
    return file_content_string

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads a file from the specified path",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path of the file to read, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)