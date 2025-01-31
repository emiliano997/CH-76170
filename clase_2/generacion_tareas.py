from openai import OpenAI
import google.generativeai as genai

import os
import json
from env import API_KEY

client = OpenAI(api_key=API_KEY)

def generar_tarea_para_evento_gemini(tipo_evento):
  prompt = f"Genera una tarea pendiente para el evento de {tipo_evento} sin introducción"
  model = genai.GenerativeModel("gemini-1.5-flash")
  response = model.generate_content(prompt)

  return response.text

def generar_tarea_para_evento(tipo_evento):
  prompt = f"Genera una tarea pendiente para el evento de {tipo_evento} sin introducción"

  response = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {
          "role": "user",
         "content": prompt
        }
    ]
  )

  tarea_pendiente = response.choices[0].message.content

  return tarea_pendiente

if __name__ == "__main__":
  tipo_evento = input("Introduce el tipo de evento: ")
  tarea_pendiente = generar_tarea_para_evento(tipo_evento)

  archivo = "tareas_evento.json"

  # Chequear si el archivo existe
  if os.path.isfile(archivo) == False:
    with open(archivo, "w+") as f:
      json.dump([], f, indent=2, ensure_ascii=False)

  with open(archivo, "r+", encoding="utf-8") as f:
    
    tareas = f.read()

    if len(tareas) != 0:
      tareas = json.loads(tareas)
    else:
      tareas = []

    tarea = {
      "tarea": tarea_pendiente,
      "evento": tipo_evento
    }

    tareas.append(tarea)

    # Rewrite file
    f.seek(0)
    f.truncate()
    json.dump(tareas, f, indent=2, ensure_ascii=False)

  
      
