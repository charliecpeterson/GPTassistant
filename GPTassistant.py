import os
import subprocess
import google.generativeai as genai
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Configure Google API key
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Initialize the Generative Model and chat session
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        return f"Error reading file: {e}"

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

def interact_with_google(prompt):
    response = chat.send_message(prompt)
    return response.text

def process_input(user_input):
    while True:
        # Replace '<filelocation file>' with file content
        if '<filelocation ' in user_input:
            start_index = user_input.find('<filelocation ') + len('<filelocation ')
            end_index = user_input.find('>', start_index)
            if end_index == -1:
                break
            file_location = user_input[start_index:end_index].strip()
            file_content = read_file(file_location)
            user_input = user_input.replace(f'<filelocation {file_location}>', file_content)

        # Replace '<runcommand command>' with command and command output/error
        if '<runcommand ' in user_input:
            start_index = user_input.find('<runcommand ') + len('<runcommand ')
            end_index = user_input.find('>', start_index)
            if end_index == -1:
                break
            command = user_input[start_index:end_index].strip()
            command_output = run_command(command)
            user_input = user_input.replace(f'<runcommand {command}>', f'Command: {command}\nOutput: {command_output}')
        
        # Break if there are no more replacements
        if '<filelocation ' not in user_input and '<runcommand ' not in user_input:
            break

    return user_input

def main():
    print("Interactive GPT")
    while True:
        user_input = input(Fore.CYAN + "Enter: " + Style.RESET_ALL)
        
        # Check for exit condition
        if 'exitgpt' in user_input.lower():
            print("Exiting the program...")
            break
        
        processed_input = process_input(user_input)
        
        google_response = interact_with_google(processed_input)
        print("\n\n" + Fore.GREEN + "GPT Response: " + Style.RESET_ALL + f"{google_response}")

if __name__ == "__main__":
    main()

