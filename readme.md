## Create transcription of audio file in Serbian language example

In this example, you will find a very simple app that allows you to create transcription of audio file utilising OpenAI `whisper-1` model.

### Running the example
- Ensure you have Python 3 and pip installed on your machine.

- Obtain your API key from OpenAI nad place it in `.env` file.
https://platform.openai.com/settings/organization/api-keys


- Create a Python virtual environment:

```bash
# Create virtual environment (-m is for python module)
mkdir -p .venv
python -m venv .venv
```

- Activate the Python virtual environment:

```bash
# Activate virtual environment
source .venv/bin/activate
```

- Install Python dependencies:

```bash
# Install dependecies from requirements.txt
pip install -r requirements.txt
```
- You can install dependencies manually:

```bash
# Dotenv dotenv reads key-value pairs from a .env file and can set them as environment variables
pip install python-dotenv

# Install dependecies from requirements.txt
pip install openai
```

- Create a .env file in the project root
```bash
# You have an example of env file name .env.dist you can start from it
cp .env.dist .env
```

### Running the scripts

1. Run the transcribe.py script

This script asks create trenscription and output it in subtitles (srt) format. It will output subtitles.srt file in the project root:

```bash
# Running the script
./transcribe.py
```


###### HAPPY CODING!