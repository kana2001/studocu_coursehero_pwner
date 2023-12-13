from openai import OpenAI

# Replace 'YOUR_API_KEY' with your actual API key
api_key = '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'
client = OpenAI(api_key=api_key)

def chat_with_gpt(prompt):
    response = client.completions.create(
        model="text-davinci-002",
        prompt=prompt,
        max_tokens=4000  # Set a large max_tokens value
    )
    return response.choices[0].text

# Your concise prompt
prompt = "Nowadays, it is almost impossible to imagine our lives without technology. We use it at home, at work, when we travel, when we communicate with friends and family. It has become an integral part of our lives."

# Make a single API call to generate the full essay
essay_response = chat_with_gpt(f"You: {prompt}\n")

# Print or save the complete essay response
print("Complete Essay:")
print(essay_response)