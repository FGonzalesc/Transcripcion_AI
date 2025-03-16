# 🎙️ Transcripcion_AI: Transcribe y Analiza Conversaciones con Azure y OpenAI

📌 **Transcripcion_AI** es un sistema avanzado que convierte audios en texto con **Azure Speech-to-Text**, identifica diferentes hablantes con **diarización** y analiza la conversación con **OpenAI** para extraer información clave en formato JSON.

---

## 🚀 Características principales
✅ **Transcripción de audio** con Microsoft Azure  
✅ **Diarización de hablantes** para separar quién dice qué  
✅ **Análisis de insights** con OpenAI (GPT)  
✅ **Generación de JSON estructurado** con información clave  
✅ **Código modular y escalable** para integraciones futuras  

---

## 🏗️ Tecnologías utilizadas
- 🟢 **Python** - Lenguaje principal del proyecto  
- 🔷 **Azure Cognitive Services** - Para Speech-to-Text  
- 🤖 **OpenAI API** - Para análisis de texto e insights  
- 🗄️ **JSON** - Para almacenar resultados estructurados  

---

## 📂 Estructura del Proyecto
```yaml
Transcripcion_AI/
│── transcripcion/
│   ├── __init__.py
│   ├── transcriber.py
│
│── procesamiento/
│   ├── __init__.py
│   ├── openai_processor.py
│
│── app.py
│── config.py            # Archivo de configuración (usa el config.example.py)
│── requirements.txt
│── Audio.wav
│── README.md
│── LICENSE.txt
```
---

## 🎯 Casos de Uso
🔹 **Centros de llamadas:** Automatización del análisis de conversaciones  
🔹 **Empresas financieras:** Detección de necesidades de clientes  
🔹 **Atención al cliente:** Extracción de insights para mejorar el servicio  

---

## 🛠️ Instalación y Configuración


### 1️⃣ Clona el repositorio:  
Abre una terminal y ejecuta los siguientes comandos para clonar el repositorio y acceder a la carpeta del proyecto:

```bash
git clone https://github.com/TU-USUARIO/Transcripcion_AI.git
cd Transcripcion_AI
```

### 2️⃣ Instala las dependencias:
Ejecuta el siguiente comando:
```bash
pip install -r requirements.txt
```

### 3️⃣ Configura las claves en config.py:
Abre el archivo config.py y reemplaza las claves con las tuyas:
```python
SPEECH_KEY = "TU_AZURE_KEY"
SPEECH_REGION = "eastus"
OPENAI_API_KEY = "TU_OPENAI_KEY"
```
### 4️⃣ Ejecuta el programa::
Ejecuta el siguiente comando para iniciar la transcripción:
```bash
python app.py
```
