import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("API_KEY")
client = OpenAI(api_key=api_key)

stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Write a random essay"}],
    stream=True,
)

essay_content = ""
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
        essay_content += chunk.choices[0].delta.content

# essays will be saved in essays/
script_directory = os.path.dirname(__file__)
subfolder = 'essays'  
directory = os.path.join(script_directory, subfolder)
if not os.path.exists(directory):
    os.makedirs(directory)
    
lines = essay_content.strip().split('\n')
title = lines[0].strip()  # Remove leading and trailing spaces
# Replace any characters in the title that are not allowed in filenames
title = "".join(c if c.isalnum() or c.isspace() else "_" for c in title)
file_name = f"{title}.doc"
file_path = os.path.join(directory, file_name)

with open(file_path, "w") as file:
    file.write(essay_content)
print(f"\n\nThe essay has been saved to {file_path}")
