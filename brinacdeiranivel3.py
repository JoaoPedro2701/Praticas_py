import pygame

print(10 * '---')
print('Responda com seu humor')
print(10 * '---')
print('Exemplo: Triste, Alegre, Desanimado ou Motivado ')
print(10 * '---')

pergunta = input('Como você esta hoje? ')

if pergunta == 'Triste' or pergunta == 'triste':

    # Essa função é usada para inicializar o subsistema de áudio do Pygame.
    pygame.mixer.init()

    # é usada para inicializar todos os módulos e subsistemas necessários para
    # que o Pygame funcione.
    pygame.init()

    # carregar um arquivo de música no mixer de música do Pygame.
    pygame.mixer.music.load('Brincando_com_python/musica/1.mp3')
    # Esta função oferece a capacidade de controlar a reprodução da música de
    # várias maneiras, usando os seguintes parâmetros:
    pygame.mixer.music.play(loops=0, start=0.0)

    # loops: Este parâmetro define quantas vezes a música será repetida.
    # start: Este parâmetro define o ponto de início da reprodução da música,
    # medido em segundos a partir do início da faixa.

    # Essa função bloqueia a execução do programa até que um evento ocorra.
    # Quando um evento ocorre
    pygame.event.wait()
    # entrada do teclado, cliques do mouse, fechamento de janelas, entre outros

elif pergunta == 'Alegre' or pergunta == 'alegre':
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('Brincando_com_python/musica/2.mp3')
    pygame.mixer.music.play(loops=0, start=0.0)
    pygame.event.wait()

elif pergunta == 'Desanimado' or pergunta == 'desanimado':
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('Brincando_com_python/musica/3.mp3')
    pygame.mixer.music.play(loops=0, start=0.0)
    pygame.event.wait()

elif pergunta == 'Motivado' or pergunta == 'motivado':
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('Brincando_com_python/musica/4.mp3')
    pygame.mixer.music.play(loops=0, start=0.0)
    pygame.event.wait()
