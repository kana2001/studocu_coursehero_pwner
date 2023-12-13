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

# Split the essay content into lines
lines = essay_content.strip().split('\n')

# Extract the title from the first line
title = lines[0].strip()  # Remove leading and trailing spaces

# Replace any characters in the title that are not allowed in filenames
title = "".join(c if c.isalnum() or c.isspace() else "_" for c in title)

# Create a doc file with the extracted title as the filename
file_name = f"{title}.doc"

with open(file_name, "w") as file:
    file.write(essay_content)
print(f"\nThe essay has been saved to {file_name}")
