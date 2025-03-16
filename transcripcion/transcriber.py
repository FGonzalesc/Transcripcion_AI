import azure.cognitiveservices.speech as speechsdk
import os
import time

class Transcriber:
    """Clase para manejar la transcripción de audio con Azure Speech y diarización."""

    def __init__(self, speech_key, speech_region, language):
        """Inicializa la configuración de Azure Speech."""
        self.speech_key = speech_key
        self.speech_region = speech_region
        self.language = language

        # Configurar el servicio de voz
        self.speech_config = speechsdk.SpeechConfig(subscription=self.speech_key, region=self.speech_region)
        self.speech_config.speech_recognition_language = self.language

    def transcribe_with_diarization(self, audio_file_path):
        """Transcribe el audio con diarización de hablantes usando ConversationTranscriber."""
        try:
            # Configurar el audio
            audio_config = speechsdk.audio.AudioConfig(filename=audio_file_path)

            # Crear el transcriptor de conversación
            transcriber = speechsdk.transcription.ConversationTranscriber(self.speech_config, audio_config)

            print("⏳ Procesando audio con diarización...")

            # Lista para almacenar la transcripción con hablantes
            full_transcription = []
            last_speaker = None
            speaker_text = []
            last_timestamp = None

            def transcribed_callback(evt):
                """Maneja los eventos de transcripción y reduce 'Speaker-Unknown'."""
                nonlocal last_speaker, speaker_text, last_timestamp

                if evt.result.reason == speechsdk.ResultReason.RecognizedSpeech:
                    speaker_id = getattr(evt.result, "speaker_id", "Desconocido")
                    text = evt.result.text.strip()
                    timestamp = evt.result.offset / 10_000_000  # Convertimos nanosegundos a segundos

                    # Si la transcripción está vacía, ignoramos la entrada
                    if not text:
                        return

                    # Si hay una pausa menor a 2 segundos, mantenemos el mismo hablante
                    if last_speaker == speaker_id and last_timestamp and (timestamp - last_timestamp < 2):
                        speaker_text.append(text)
                    else:
                        # Guardamos la oración anterior antes de cambiar de hablante
                        if speaker_text:
                            full_transcription.append(f"Speaker-{last_speaker}: {' '.join(speaker_text)}")
                            speaker_text = []

                        # Cambiamos de hablante
                        last_speaker = speaker_id
                        speaker_text.append(text)

                    # Actualizamos el timestamp
                    last_timestamp = timestamp

            # Conectar el callback
            transcriber.transcribed.connect(transcribed_callback)

            # Iniciar la transcripción de manera asíncrona
            transcriber.start_transcribing_async().get()

            # Esperar a que termine la transcripción (ajustar según la duración del audio)
            time.sleep(60)  # Ajusta este tiempo según el audio

            # Detener la transcripción
            transcriber.stop_transcribing_async().get()

            # Guardar la última transcripción pendiente
            if speaker_text:
                full_transcription.append(f"Speaker-{last_speaker}: {' '.join(speaker_text)}")

            if full_transcription:
                return "\n".join(full_transcription)
            else:
                print("❌ No se detectaron hablantes.")
                return None

        except Exception as e:
            print(f"⚠️ Error en la transcripción: {str(e)}")
            return None