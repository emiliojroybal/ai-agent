import argparse
import os
from prompts import system_prompt
from google import genai
from google.genai import types
from dotenv import load_dotenv
import call_function


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set in environment variables.")
    
    for _ in range(20):
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[call_function.available_functions],
                system_instruction=system_prompt,
                ),
            )
        
        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)
        if response:
            if args.verbose:
                print(f"User prompt: {args.user_prompt}")
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
            if response.function_calls:
                function_call_results = []

                for function_call in response.function_calls:
                    function_call_result = call_function.call_function(function_call, args.verbose)
                    if not function_call_result.parts:
                        raise Exception("Function call parts is empty")
                    
                    if not function_call_result.parts[0].function_response:
                        raise Exception("Function response object is empty")
                    
                    if not function_call_result.parts[0].function_response.response:
                        raise Exception("Function response is empty")
                    
                    function_call_results.append(function_call_result.parts[0])
                    if args.verbose:
                        print(f"-> {function_call_result.parts[0].function_response.response}")
                messages.append(types.Content(role="user", parts=function_call_results))
            
            for part in response.candidates[0].content.parts:
                if part.text:
                    print(part.text)
                    return
        else:
            raise RuntimeError("No response received from the model.")
        
    exit(1)
        





if __name__ == "__main__":
    main()
