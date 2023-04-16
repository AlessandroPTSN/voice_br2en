#####################################################
#Python 3.10#########################################
import speech_recognition as sr
#pip install speech_recognition  #3.10.0
from googletrans import Translator
#pip install googletrans==3.1.0a0
import torch
#pip install torch  #2.0.0+cpu
from omegaconf import OmegaConf
#pip install omegaconf  #2.3.0
import sounddevice as sd
#pip install sounddevice  #0.4.6

torch.hub.download_url_to_file('https://raw.githubusercontent.com/snakers4/silero-models/master/models.yml',
                               'latest_silero_models.yml',
                               progress=False)
models = OmegaConf.load('latest_silero_models.yml')


model = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                     model='silero_tts',
                                     language='en',
                                     speaker='v3_en', verbose=False)[0]
model.to(torch.device('cpu'))  # gpu or cuda





