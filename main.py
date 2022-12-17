import os
import sys
from random import randint
import pygame

# Изображение не получится загрузить
# без предварительной инициализации pygame
pygame.init()
SIZE = WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode(SIZE)
BACKGROUND = 'white'
COUNT_BOMBS = 50



def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

all_sprites = pygame.sprite.Group()
for _ in range(COUNT_BOMBS):
    bomb = pygame.sprite.Sprite(all_sprites)
    bomb.image = load_image('bomb.png')
    bomb.rect = bomb.image.get_rect()
    bomb.rect.x = randint(0, WIDTH)
    bomb.rect.y = randint(0, HEIGHT)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BACKGROUND)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()