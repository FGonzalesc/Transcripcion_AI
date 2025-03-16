from transcripcion import Transcriber
from procesamiento.openai_processor import OpenAIProcessor
import config
import os
import json
import re

# Inicializar transcriptor y procesador OpenAI
transcriber = Transcriber(config.SPEECH_KEY, config.SPEECH_REGION, config.LANGUAGE)
openai_processor = OpenAIProcessor()

# Pedir la ruta del archivo de audio
audio_path = input("📂 Ingresa la ruta del archivo de audio: ")

if os.path.exists(audio_path):
    transcription = transcriber.transcribe_with_diarization(audio_path)
    if transcription:
        print("\n🔊 Transcripción con hablantes separados:")
        print(transcription)

        # Extraer insights con OpenAI
        insights = openai_processor.extract_insights(transcription)

        if insights:
            try:
                insights = insights.strip()  # Eliminar espacios en blanco y saltos de línea

                # Si OpenAI devuelve un bloque de código JSON, eliminar los delimitadores json ...
                insights = re.sub(r"^json\n|\n$", "", insights)

                insights_json = json.loads(insights)
                
                print("\n📊 Insights extraídos:")
                print(json.dumps(insights_json, indent=4, ensure_ascii=False))

            except json.JSONDecodeError as e:
                print(f"⚠️ Error al convertir la respuesta de OpenAI en JSON: {e}")
                print("🔹 Respuesta recibida de OpenAI:")
                print(repr(insights)) 
        else:
            print("❌ OpenAI no devolvió ninguna respuesta. Revisa tu API Key y cuota disponible.")

    else:
        print("❌ No se pudo obtener la transcripción.")
else:
    print("❌ Archivo no encontrado. Verifica la ruta.")