"""Synthesizes speech from the input string of text or ssml.
Make sure to be working in a virtual environment.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech

# Instantiates a client
client = texttospeech.TextToSpeechClient()


text = """
This paper proposes a domain adaptation method for accurate object detection from in-vehicle FIR camera images. Many accurate detection models are proposed in the visible-light domain. It is, however, heavily affected by weather and lighting conditions. In contrast, FIR images are less affected by them. The proposed method projects visible-light-domain detection results onto far-infrared images, and uses them as pseudo labels for training an FIR-domain detection model. Experiments show that the proposed method improves the detection accuracy and is comparable to a reference method using manually-labeled data. The framework demonstrates the effectiveness of visible-light-to-far-infrared domain adaptation for robust FIR-domain object detection. Please come to our poster and let’s discuss in more details.
"""

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text=text)

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open("output.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')