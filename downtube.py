from pytube import YouTube
from pytube.cli import on_progress

def baixa_video():
    url =  input('Cole aqui a URL: ')
    yt = YouTube(url, on_progress_callback= on_progress)

    print('Baixando...')

    video = yt.streams.get_highest_resolution()
    video.download(output_path='./downtube')

    print('Arquivo baixado com sucesso!')
    print()

def extrai_audio():
    url =  input('Cole aqui a URL: ')

    yt = YouTube(url, on_progress_callback= on_progress)

    print('Baixando áudio...')

    stream = yt.streams.filter(only_audio=True)
    audio = stream.get_by_itag(140)
    audio.download(output_path='./audio-mp3')

    print('Áudio baixado com sucesso!')
    print()


while True:
    opcao = input("""Escolha uma opção ou pressione s para sair: 
    1 - Baixar o vídeo completo
    2 - Extrair apenas o audio
    """)

    if opcao == '1':
        #chama a função para baixar o video
        baixa_video()
    elif opcao == '2':
        #chama a função para extrair apenas o audio
        extrai_audio()
    elif opcao == 's':
        break