# projec-ultimate: Reconhecimento de Fala com Python

Este projeto utiliza bibliotecas de áudio e processamento de fala para gravar, processar e reconhecer comandos de voz. Ele também executa ações com base no reconhecimento de fala, como abrir o YouTube.

## Funcionalidades

- **Gravação de Áudio:** Grava um áudio de 5 segundos usando a biblioteca `sounddevice`.
- **Redução de Ruído:** Processa o áudio gravado para reduzir ruídos com a biblioteca `noisereduce`.
- **Reconhecimento de Fala:** Utiliza o `SpeechRecognition` para transcrever o áudio em texto.
- **Execução de Comandos:** Abre o YouTube automaticamente ao detectar o comando "abrir youtube".

---

## Tecnologias Utilizadas

- Python 3.11
- [sounddevice](https://python-sounddevice.readthedocs.io/en/latest/) - Para gravar áudio.
- [scipy](https://scipy.org/) - Para manipulação de arquivos de áudio.
- [noisereduce](https://pypi.org/project/noisereduce/) - Para redução de ruído em arquivos de áudio.
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) - Para reconhecimento de fala.
- Google Colab - Para execução e interação com o navegador.

---

## Pré-requisitos

Certifique-se de que você tem as dependências instaladas no seu ambiente. No Google Colab, basta rodar os comandos abaixo:

```bash
!apt-get install -y libportaudio2
!pip install sounddevice scipy SpeechRecognition noisereduce
