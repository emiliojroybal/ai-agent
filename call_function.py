from google.genai import types
import functions.get_files_info as get_files_info_py
import functions.run_python_file as run_python_file_py
import functions.write_file as write_file_py
import functions.get_file_content as get_file_content_py

available_functions = types.Tool(
    function_declarations=[
        get_files_info_py.schema_get_files_info, 
        run_python_file_py.schema_run_python_file, 
        write_file_py.schema_write_file, 
        get_file_content_py.schema_get_file_content],
)

def call_function(function_call, verbose=False):
    if verbose:
        print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(f" - Calling function: {function_call.name}")

    function_map = {
        "get_files_info": get_files_info_py.get_files_info,
        "run_python_file": run_python_file_py.run_python_file,
        "write_file": write_file_py.write_file,
        "get_file_content": get_file_content_py.get_file_content
    }

    function_name = function_call.name or ""

    if function_name not in function_map:
        return types.Content(
            roles="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    
    args = dict(function_call.args) if function_call.args else {}
    args["working_directory"] = "./calculator"

    function_result = function_map[function_name](**args)
    
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result}
            )
        ]
    )