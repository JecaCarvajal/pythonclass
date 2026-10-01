import os
import openai
from dotenv import load_dotenv


load_dotenv(override=True)

client = openai.OpenAI(
    base_url=os.environ["BASE_URL"],
    api_key=os.environ["GEMINI_API_KEY"],    
)

response = client.chat.completions.create(
    model="models/gemini-3-flash-preview",
      temperature=0.7,
      messages=[
          {"role": "system", "content": "Eres un experto jugador de Subnautica que responde solo preguntas de este juego para encontrar minerales" },
          {"role": "user", "content": "Escribe donde se encuentra oro en el juego" }
      ], 
)

print(response.choices[0].message.content)
