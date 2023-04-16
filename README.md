# voice_br2en

O código captura o áudio em português, escreve ele em texto, traduz para inglês e reproduz o áudio resultante da tradução em tempo real. Ele utiliza a biblioteca SpeechRecognition para reconhecer a fala em português, a biblioteca googletrans para traduzir o texto para inglês e a biblioteca SoundDevice para reproduzir o áudio resultante da tradução.

![voice_br2en](https://user-images.githubusercontent.com/50224653/232333871-c0827e2c-fd98-41f1-90dd-5b06cacdbd82.gif)


## Pacotes e funções utilizadas

`speech_recognition`: uma biblioteca que permite reconhecer fala a partir de um microfone ou arquivo de áudio. Ela disponibiliza diversos serviços de reconhecimento de fala, como o Google Cloud Speech API e o CMU Sphinx.
A partir dele, foi possível utilizar a função `recognizer()`, que permite reconhecer fala a partir de um microfone ou arquivo de áudio. Ela disponibiliza diversos métodos para processar a fala e retornar o texto correspondente.

Após de converter o áudio para texto, foi utilizado a função `Translator.translate()` da biblioteca `googletrans`: uma função da biblioteca googletrans que permite traduzir um texto de um idioma para outro utilizando a API de tradução do Google Translate. (OBS: extremamente importante utilizar a versão googletrans==3.1.0a0).

E a partir do pacote `torch` (usado para treinar modelos de redes neurais) foi utilizado a função `torch.hub.load()`: uma função da biblioteca Torch que permite carregar modelos pré-treinados a partir de repositórios públicos. No código, ela é utilizada para carregar o modelo de síntese de fala Silero TTS, que é utilizado para gerar a fala resultante da tradução.

E por fim, foi utilizado a função `sounddevice.play()`: uma função da biblioteca `SoundDevice` que permite reproduzir um sinal de áudio utilizando o dispositivo de saída de áudio do computador. No código, ela é utilizada para reproduzir a fala resultante da tradução.

## Demais informações 

O arquivo 'Import_models.py' é responsável por fornecer a versão do Python e dos pacotes utilizados + a importação do modelo utilizado.  
O arquivo 'test_model_voices.py' é apenas para testar se o modelo foi importado corretamente.  
Se tudo estiver configurado certo, pode rodar o arquivo 'voice_br2en.py', responsável pela tradução de voz.

Devo um enorme agradecimento ao [Snakers4](https://github.com/snakers4/silero-models), que deixou os modelos TTS silero pré treinados! 

Se quiserem mudar a voz do modelo, tem um repositório que criei no [GoogleColab](https://colab.research.google.com/drive/1oqo8OVmQoBB2azi8wdq0lQOv4O_4bLcz?usp=sharing) para poder ouvir todas as vozes disponíveis.


