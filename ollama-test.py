import ollama

# Simple chat completion working, start model from terminal, ollama run gemma4:e2b then check from here 
response = ollama.chat(
    model='gemma4:e2b',
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': 'Explain Python virtual environments.'},
    ]
)
print(response['message']['content'])   