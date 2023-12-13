import os
from openai import OpenAI

# Replace 'YOUR_API_KEY' with your actual API key
api_key = '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'
client = OpenAI(api_key=api_key)

stream = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Write a random essay"}],
    stream=True,
)

base_file_name = "new_file"
counter = 1

while True:
    file_name = f"{base_file_name}{counter}.doc"

    if not os.path.exists(file_name):
        break

    counter += 1

with open(file_name, "w") as file:
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            # file.write(f"It didn't exist before, but now it does.\n")
            print(chunk.choices[0].delta.content, end="")
    


