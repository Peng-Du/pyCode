import os
import azure.cognitiveservices.speech as speechsdk

# Set up the Azure Speech API configuration
speech_key = os.environ.get('AZURE_API_KEY')
service_region = 'eastus'

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
audio_config = speechsdk.audio.AudioOutputConfig(filename="hola.wav")

# Create a synthesizer using the configured settings
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

# Define the ssml to be synthesized
ssml = """
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="es-ES">
    <voice name="es-ES-ElviraNeural">
        <prosody rate="0.9">
            Hola, amigos
        </prosody>
    </voice>
</speak>
"""
# Synthesize the ssml to an wav file
result = speech_synthesizer.speak_ssml_async(ssml).get()
