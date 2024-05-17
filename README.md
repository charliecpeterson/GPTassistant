# Interactive GPT  Assistant

## Overview

This project provides a command-line interface (CLI) for interacting with Google's Generative AI model using Python. The script allows users to read file contents, execute shell commands, and interact with the Generative AI model, seamlessly integrating these functionalities to create a dynamic interactive experience.

## Features

- **File Content Reading**: Replace placeholders with the content of specified files.
- **Command Execution**: Replace placeholders with the output of specified shell commands.
- **Generative AI Interaction**: Send processed input to Google's Generative AI model and display the response.

## Requirements

- Python 3.x
- Google Generative AI Python client library (`google.generativeai`)
- `colorama` library for colored terminal output

## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/charliecpeterson/GPTassistant.git
    cd GPTassistant
    ```

2. **Install Required Libraries**:

    ```bash
    pip install google-generativeai colorama
    ```

3. **Set Up Google API Key**:

    Ensure you have a valid Google API key and set it as an environment variable:

    ```bash
    export GOOGLE_API_KEY=<your-google-api-key>
    ```

## Usage

Run the script using Python:
```bash
python GPTassistant.py
```

## Interactive Mode

1. Reading File Content:

- Use the placeholder <filelocation path/to/your/file> in your input.
- Example: Read the content of <filelocation /path/to/file.txt>

2. Running Commands:

- Use the placeholder <runcommand your-command> in your input.
- Example: Run the following command <runcommand ls -la>
- Interacting with GPT:

3. Enter any text to send it directly to the Generative AI model.

- Example: Tell me a joke

4. Exit the Program:

- Type exitgpt to terminate the interactive session.

## Example Session

```bash
Interactive GPT
Enter: Summarize this code <filelocation /path/to/file.txt>
GPT Response: [File summary is displayed here]

Enter: Can you discribe the files that I have if I run <runcommand ls -la>
Command: ls -la
Output: [Command output is displayed here]

Enter: Tell me a story about a brave knight.
GPT Response: [Generated story]

Enter: exitgpt
Exiting the program...
```

