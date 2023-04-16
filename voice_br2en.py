#####################################################
import speech_recognition as sr
from googletrans import Translator
import torch
import sounddevice as sd



# Função responsável por ouvir e reconhecer a fala
def ouvir_microfone():
    model = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                         model='silero_tts',
                                         language='en',
                                         speaker='v3_en', verbose=False)[0]
    translator = Translator()
    # Habilita o microfone
    microfone = sr.Recognizer()
    
    with sr.Microphone() as source:
        # Chama a função de redução de ruído disponível na speech_recognition
        microfone.adjust_for_ambient_noise(source)       
        # Avisa ao usuário que está pronto para ouvir
        print("Diga alguma coisa: ")
        # Armazena a informação de áudio na variável
        audio = microfone.listen(source) 
    
    try:
        # Passa o áudio para o reconhecedor de padrões do speech_recognition
        frase = microfone.recognize_google(audio, language='pt-BR')
        # Após alguns segundos, retorna a frase falada
        frase = frase.replace("espaço", ",")
        frase = frase.replace("Espaço", ",")
        frase = frase.replace("pergunta", "?")
        print("pt-br: " + frase)
        frase = translator.translate(frase,src='pt',dest='en').text
        print("en-en: " + frase)
        frase = frase+',  ,'
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
        return frase
    except sr.UnknownValueError:
        # Caso não tenha reconhecido o padrão de fala, exibe esta mensagem
        print('unknown voice')


import keyboard

def meu_codigo():
    while True:
        if keyboard.is_pressed('spacebar'):
            ouvir_microfone()
        
        if keyboard.is_pressed('esc'):
            break

# inicia a execução do código quando a tecla "spacebar" for pressionada
keyboard.add_hotkey('spacebar', meu_codigo)

# aguarda a tecla "esc" ser pressionada para encerrar o programa
keyboard.wait('esc')
###################################################################
 