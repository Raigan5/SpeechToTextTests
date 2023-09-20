import torchaudio
import torch
import sounddevice as sd
import numpy as np
import soundfile as sf

#https://github.com/facebookresearch/seamless_communication/tree/main
#https://seamless.metademolab.com/demo

# # Parameters for audio recording
# sample_rate = 44100  # Samples per second
# duration = 2  # Recording duration in seconds
#
# print("Recording...")
#
# # Record audio
# audio_data = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=1, device=1)
# sd.wait()  # Wait for the recording to finish
#
# # Convert the recorded audio to int16 data type
# audio_data = audio_data.astype(np.int16)
#
# # Save the recorded audio to a WAV file using soundfile
# sf.write("recorded_audio.wav", audio_data, sample_rate)

#https://huggingface.co/facebook/seamless-m4t-unity-small-s2t#inference
#Load the saved audio using torchaudio
audio_input, _ = torchaudio.load("Television.wav")

s2t_model = torch.jit.load("unity_on_device_s2t.ptl")  # Load exported S2T model
with torch.no_grad():
    text = s2t_model(audio_input, tgt_lang='eng')  # Forward call with tgt_lang specified for ASR or S2TT
print(text)  # Show text output
