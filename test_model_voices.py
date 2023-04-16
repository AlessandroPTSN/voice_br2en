#############################################################################
import speech_recognition as sr
from googletrans import Translator
import torch
from omegaconf import OmegaConf
import sounddevice as sd

model = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                     model='silero_tts',
                                     language='en',
                                     speaker='v3_en', verbose=False)[0]

frase = 'Unable to determine this model’s library. Check the docs'
#frase = frase.replace(" ", ", ,")
audio = model.apply_tts(text=frase,
                        speaker='en_13',
                        sample_rate=24000,#[8000, 24000, 48000]
                        put_accent=True,
                        put_yo=True)
# carregar áudio e taxa de amostragem
audio_data = audio.numpy()
# tocar áudio
sd.play(audio_data, 22000)
sd.wait()
