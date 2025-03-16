import openai
import config

class OpenAIProcessor:
    """Clase para procesar la transcripción y extraer insights usando OpenAI."""

    def __init__(self):
        """Inicializa la configuración de OpenAI."""
        openai.api_key = config.OPENAI_API_KEY

    def extract_insights(self, transcription):
        """Envía la transcripción a OpenAI y extrae información clave."""

        prompt = f"""
        Eres un asistente de análisis de conversaciones de ventas.
        Tu tarea es analizar la conversación entre un asesor financiero y un cliente para extraer información clave y estructurarla en un JSON para generación de leads.

        📌 **Devuelve el JSON con la siguiente estructura:**
        - **"cliente"**: Información del cliente (nombre, perfil, hijos, parientes enfermos, mascotas).
        - **"situacion_financiera"**: Estado actual, dificultades, deudas, ingresos.
        - **"negocio"**: Si tiene negocio, en qué estado está y qué necesita.
        - **"eventos_importantes"**: Cambios en su vida (viajes, mudanza, problemas familiares).
        - **"intereses"**: Lista de temas que parecen ser importantes para el cliente.
        - **"posibles_necesidades"**: Lista de soluciones financieras que podrían interesarle.
        - **"prioridad_cliente"**: Cuál es el tema más importante para el cliente y su nivel de urgencia.

        📌 **IMPORTANTE:**  
        - **Si un dato no se menciona, no lo pongas en el JSON.**
        - **Extrae información del cliente (Speaker-Guest-2), no del asesor (Speaker-Guest-1).**
        - **NO agregues explicaciones, solo responde con un JSON válido.**

        **Transcripción:**
        {transcription}

        Devuelve únicamente un JSON válido sin comentarios ni texto adicional.
        """

        try:
            client = openai.OpenAI(api_key=config.OPENAI_API_KEY) 
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Eres un experto en análisis de conversaciones."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3
            )

            insights = response.choices[0].message.content 
            return insights

        except Exception as e:
            print(f"⚠️ Error al procesar con OpenAI: {str(e)}")
            return None