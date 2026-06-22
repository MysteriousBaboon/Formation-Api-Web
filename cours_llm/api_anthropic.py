import os
from pathlib import Path

import anthropic
from dotenv import load_dotenv

# Charger le .env qui se trouve à côté de ce fichier
load_dotenv(Path(__file__).resolve().parent / ".env")

LLM_API_KEY = os.getenv("LLM_API_KEY")


client = anthropic.Anthropic(
    api_key=LLM_API_KEY or "non-utilise",
)

# reponse = client.messages.create(
#     model="claude-sonnet-4-6",
#     messages=[        
#         {"role": "user", "content": input('Pose moi une question')}],
#     max_tokens=1000,
# )

# print(reponse.content[0].text)

message_history = []

while True:
    user_message = input()

    message_history.append({"role": "user", "content": f"{user_message}"})
    with client.messages.stream(
        max_tokens=4096,
        system='Tu es un expert analyste du language humain. Tu va determiner, comment se sent l\'utilisateur a partir de son message ',
        messages=message_history,
        model="claude-sonnet-4-6",
        output_config={
                "format": {
                    "type": "json_schema",
                    "schema": {
                        "type": "object",
                        "properties": {
                            "sujet": {"type": "string"},
                            "friendliness": {"type": "string"},
                            "emotions": {"type": "array", "items": {"type": "string"}},
                        },
                        "required": ["sujet", "friendliness", "emotions"],
                        "additionalProperties": False,
                    }
                }
            },

        ) as stream:
        ai_message = ''
        for text in stream.text_stream:
            ai_message += text
            print(text, end="", flush=True)
        print(f"\n Message final {ai_message}\n")
        message_history.append({'role': 'assistant', 'content': ai_message})
    print(message_history)
