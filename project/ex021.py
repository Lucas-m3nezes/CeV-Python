"""Faça um programa em python que abra e reproduza o aúdio de um arquivo MP3."""


import pygame

def reproduzir_mp3(caminho_arquivo):
    # Inicialize o pygame
    pygame.init()

    # Inicialize o mixer de áudio do pygame
    pygame.mixer.init()

    try:
        # Carregue o arquivo MP3
        pygame.mixer.music.load('ex021.mp3')

        # Reproduza o arquivo MP3
        pygame.mixer.music.play()

        # Mantenha o programa em execução até que a música termine
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except pygame.error as e:
        print(f"Erro ao reproduzir o arquivo MP3: {e}")
    finally:
        # Encerre o mixer de áudio do pygame
        pygame.mixer.quit()
        # Encerre o pygame
        pygame.quit()

# Substitua o caminho abaixo pelo caminho real do seu arquivo MP3
caminho_do_arquivo_mp3 = r"C:\Users\Lucas\PROJETOS-DIO\Curso em vídeo\Python início\project"
reproduzir_mp3(caminho_do_arquivo_mp3)