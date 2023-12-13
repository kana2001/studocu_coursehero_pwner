import os
from openai import OpenAI

# Replace 'YOUR_API_KEY' with your actual API key
api_key = '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'
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


# Get the directory path of the current script
script_directory = os.path.dirname(__file__)

# Define the subfolder where you want to save the file
subfolder = 'essays'  # Replace with the name of your subfolder

# Create the full path to the subfolder within the script directory
directory = os.path.join(script_directory, subfolder)

# Ensure the subfolder exists, create it if necessary
if not os.path.exists(directory):
    os.makedirs(directory)

# Ensure the directory exists, create it if necessary
if not os.path.exists(directory):
    os.makedirs(directory)
    
# Split the essay content into lines
lines = essay_content.strip().split('\n')

# Extract the title from the first line
title = lines[0].strip()  # Remove leading and trailing spaces

# Replace any characters in the title that are not allowed in filenames
title = "".join(c if c.isalnum() or c.isspace() else "_" for c in title)

# Create a doc file with the extracted title as the filename
file_name = f"{title}.doc"

# Create the full path to the file
file_path = os.path.join(directory, file_name)

with open(file_path, "w") as file:
    file.write(essay_content)
print(f"\nThe essay has been saved to {file_path}")
