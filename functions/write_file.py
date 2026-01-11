import os
from google.genai import types

def write_file(working_directory, file_path, content):
    working_dir_abs = os.path.abspath(working_directory)
    target_path_abs = os.path.abspath(os.path.join(working_dir_abs, file_path))

    if not os.path.commonpath([working_dir_abs, target_path_abs]) == working_dir_abs:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if os.path.isdir(target_path_abs):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    
    os.makedirs(os.path.dirname(target_path_abs), exist_ok=True)
    with open(target_path_abs, 'w') as file:
        file.write(content)
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes a file with the specified content",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path of the file to write, relative to the working directory (default is the working directory itself)",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file",
            ),
        },
    ),
)