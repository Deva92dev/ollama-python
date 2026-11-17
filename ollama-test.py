import ollama

# Simple chat completion
response = ollama.chat(
    model='gemma4:e2b',
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': 'Explain Python virtual environments.'},
    ]
)
print(response['message']['content'])   