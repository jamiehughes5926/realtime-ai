import openai
from api_secrets import API_KEY_OPENAI

openai.api_key = API_KEY_OPENAI

def ask_computer(prompt, conversation_history):
    # Combine the conversation history and the new prompt
    full_prompt = ' '.join(conversation_history) + f' {prompt}'
    
    # Use GPT-3 to generate a response
    res = openai.Completion.create(
        engine="text-davinci-002",
        prompt=full_prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return res["choices"][0]["text"].strip()